from app import app
from db import db

db.init_app(app)


#create a table if it's not exist
@app.before_first_request
def create_tables():
    db.create_all()