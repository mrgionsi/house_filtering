import json
from flask import Flask, Response, render_template, request, jsonify, stream_with_context
from flask_cors import CORS
from tinydb import Query, TinyDB
from math import ceil
import re
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.date import DateTrigger
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
import requests
import brotlicffi
from bs4 import BeautifulSoup

import datetime
import logging

from data_handler import changeRating, setSaved
from utilities import start_search_scraping

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "PATCH", "DELETE", "OPTIONS"]}})

# Setup logging for APScheduler
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


db = TinyDB('./db.json')
Property = Query()
##https://tinydb.readthedocs.io/en/latest/getting-started.html#installing-tinydb
# Example JSON data (Python dictionary list)
data = db.all()

# Log events for job execution and errors
def job_listener(event):
    if event.exception:
        logger.error(f"Job {event.job_id} failed")
    else:
        logger.info(f"Job {event.job_id} completed successfully")

scheduler = BackgroundScheduler()
scheduler.start()

scheduler.add_listener(job_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)

@app.route('/set-clicked', methods=['PATCH'])
def set_clicked():
    item_id = request.json.get('id')
    if item_id is None:
        return jsonify({'error': 'No ID provided'}), 400

    # Update the 'clicked' field for the matching item
    db.update({'clicked': True}, Property.id == item_id)
    response = {
        "status": 200,
        "message": "Clicked status updated', 'id'",
        "data": {"id": item_id}
    }
    return jsonify(response), 200

@app.route('/search', methods=['GET'])
def search_endpoint():
    @stream_with_context
    def generate_logs():
        yield from start_search_scraping()
    return Response(generate_logs(), content_type='text/plain')


@app.route('/api/item/<int:item_id>/save', methods=['PATCH'])
def toggle_saved(item_id):
    # Get the new 'saved' state from the request body
    request_data = request.get_json()


    # Get the new saved value from the request (e.g., true or false)
    saved_value = request_data.get('saved', None)

    return setSaved(item_id, saved_value)

@app.route('/api/item/<int:item_id>/rating', methods=['PATCH'])
def change_rating(item_id):
    # Get the new 'saved' state from the request body
    request_data = request.get_json()


    # Get the new saved value from the request (e.g., true or false)
    rating = request_data.get('rating', None)

    return changeRating(item_id, rating)



@app.route('/get-data')
def getData():
    data = db.all()
    return data
    
""" @app.route('/')
def index():
    data = db.all()
    # Get page number, column, and sort direction from query string
    page = request.args.get('page', 1, type=int)
    column = request.args.get('column', 'id')  # Default to sorting by 'id'
    direction = request.args.get('direction', 'asc')  # Default to ascending order
    
    per_page = 20  # Results per page
    start = (page - 1) * per_page
    end = start + per_page

    # Sort the data based on the selected column and direction
    sorted_data = sort_data(data, column, direction)
    
    # Slice the data to get the correct page of results
    paginated_data = sorted_data[start:end]

    # Calculate total pages
    total_pages = ceil(len(data) / per_page)

    # Pass the page, total_pages, column, and direction to the template
    return render_template('index.html', data=paginated_data, page=page, total_pages=total_pages, column=column, direction=direction)
 """


@app.route('/api/scheduled-jobs', methods=['GET'])
def get_scheduled_jobs():
    try:
        # Get all jobs from the scheduler
        jobs = scheduler.get_jobs()

        # Format job details
        job_list = []
        for job in jobs:
            job_details = {
                'id': job.id,
                'next_run_time': job.next_run_time.isoformat() if job.next_run_time else None,
                'trigger': str(job.trigger),  # Trigger type and information
                'name': job.name,  # Job name (if any)
            }
            job_list.append(job_details)

        # Return the list of scheduled jobs
        return jsonify({'jobs': job_list}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Endpoint to schedule the task
@app.route('/api/schedule-task', methods=['POST'])
def schedule_task():
    data = request.get_json()
    scheduled_time_str = data.get('time')

    if not scheduled_time_str:
        return jsonify({'error': 'No time provided'}), 400

    try:
        scheduled_time = datetime.datetime.fromisoformat(scheduled_time_str)
    except ValueError:
        return jsonify({'error': 'Invalid time format'}), 400

    if scheduled_time < datetime.datetime.now(datetime.timezone.utc):
        return jsonify({'error': 'Scheduled time must be in the future'}), 400

    try:
        trigger = DateTrigger(run_date=scheduled_time)
        job = scheduler.add_job(call_start_search, trigger)
        return jsonify({'message': f'Task scheduled for {job.next_run_time}'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def call_start_search():
    try:
        for result in start_search_scraping():
            logger.info(result)  # Process each yielded value (e.g., log or store it)
    except Exception as e:
        logger.error(f"Error in start_search_scraping: {e}")



if __name__ == '__main__':
    app.run(debug=True)
    
    
