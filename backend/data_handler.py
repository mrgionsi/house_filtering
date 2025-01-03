import json
from tinydb import TinyDB, Query
db = TinyDB('./db.json')
User = Query()
##https://tinydb.readthedocs.io/en/latest/getting-started.html#installing-tinydb
# Parse JSON data
# Count the number of entries
entry_count = len(db.all())

#print("Number of entries:", entry_count)
  
def addEntry(row):
    db = TinyDB('db.json')
    Entry = Query()
    # Convert the object to a dictionary before querying and inserting
    row_dict = row.to_dict()
    
    
    # Check if an entry with the same ID already exists
    if not db.search(Entry.id == row_dict['id']):  # TinyDB works with dictionaries
        db.insert(row_dict)
        yield f"New Entry, inserting -> Title: {row_dict['title']}, Price: {row_dict['price']}, Link: {row_dict['link']}\n"
    else:
        yield f"Already exist, skipping -> Title: {row_dict['title']}, Price: {row_dict['price']}, Link: {row_dict['link']}\n"

        
def setSaved(id, value):
    db = TinyDB('db.json')
    Item = Query()
    item = db.search(Item.id == id)
    # If the item is not found, return an error
    if not item:
        return ({"error": "Item not found"}), 404

    # There should only be one item with that ID, so we'll update it
    item = item[0]  # Get the first (and only) item
    item['saved'] = value  # Update the 'saved' field

    # Update the item in TinyDB
    db.update(item, Item.id == id)
    return ({"message": "Updated successfully"}), 201


def changeRating(id, value):
    db = TinyDB('db.json')
    Item = Query()
    item = db.search(Item.id == id)
    # If the item is not found, return an error
    if not item:
        return ({"error": "Item not found"}), 404

    # There should only be one item with that ID, so we'll update it
    item = item[0]  # Get the first (and only) item
    item['rating'] = value  # Update the 'saved' field

    # Update the item in TinyDB
    db.update(item, Item.id == id)
    return ({"message": "Updated successfully"}), 201






class JsonObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
    
    def to_dict(self):
        return self.__dict__
    
    def to_json(self):
        return json.dumps(self.__dict__)