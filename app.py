from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def hello_world():
    return 'This bot is made by fk team e'

# Run the application
if __name__ == '__main__':
    app.run()
