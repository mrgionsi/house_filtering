import json
from tinydb import TinyDB, Query
db = TinyDB('./db.json')
User = Query()
##https://tinydb.readthedocs.io/en/latest/getting-started.html#installing-tinydb
print(db.all())
# Parse JSON data
# Count the number of entries
entry_count = len(db.all())

print("Number of entries:", entry_count)
  
def addEntry(row):
    db = TinyDB('db.json')
    Entry = Query()
    # Convert the object to a dictionary before querying and inserting
    row_dict = row.to_dict()
    
    # Check if an entry with the same ID already exists
    if not db.search(Entry.id == row_dict['id']):  # TinyDB works with dictionaries
        db.insert(row_dict)
        print(row_dict)
        
        

class JsonObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
    
    def to_dict(self):
        return self.__dict__
    
    def to_json(self):
        return json.dumps(self.__dict__)