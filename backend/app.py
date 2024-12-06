from flask import Flask, Response, render_template, request, jsonify, stream_with_context
from flask_cors import CORS
from tinydb import Query, TinyDB
from math import ceil
import re

from manage import changeRating, setSaved
from new_main import start_search_scraping

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "PATCH", "DELETE", "OPTIONS"]}})

db = TinyDB('./db.json')
Property = Query()
##https://tinydb.readthedocs.io/en/latest/getting-started.html#installing-tinydb
# Example JSON data (Python dictionary list)
data = db.all()


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


# Function to sort data based on column and direction
def sort_data(data, column, direction):
    if column == 'clicked':
        # Ensure 'Nope' is treated as False and 'Visualizzato' as True
        return sorted(data, key=lambda x: (x.get(column, 'Nope') == 'Visualizzato'), reverse=(direction == "desc"))
    elif column == 'formattedValue':
        # Special handling for formattedValue, convert to integer for sorting
        return sorted(data, key=lambda x: parse_formatted_value(x[column]), reverse=(direction == "desc"))
    else:
        return sorted(data, key=lambda x: x[column], reverse=(direction == "desc"))

def parse_formatted_value(value):
    # Remove any non-numeric characters except for commas or periods
    value = re.sub(r'[^\d,\.]', '', value)  # Remove currency symbols (like €)
    value = value.replace('.', '')  # Remove thousands separators (periods)
    value = value.replace(',', '')  # Remove commas (for thousands, if used)
    return int(value) if value else 0  # Convert to integer


@app.route('/get-data')
def getData():
    data = db.all()
    return data
    
@app.route('/')
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

if __name__ == '__main__':
    app.run(debug=True)