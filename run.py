# run.py

from app import create_app, db
from app.models import User, Task

app = create_app()

with app.app_context(): # to ensure that the application context is active when we create the database tables
    db.create_all()  # Create the database tables if they don't exist

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, private, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

if __name__ == '__main__':
    app.run(debug=True)