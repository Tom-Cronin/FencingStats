# Import the necessary modules from Flask
from flask import Flask, render_template

# Create a Flask app instance
app = Flask(__name__)

# Define a route for the root URL ("/") and associate it with a function
@app.route('/')
def index():
    # Render the index.html template and return the resulting HTML
    return render_template('index.html')

# Start the Flask development server if this script is run directly
if __name__ == '__main__':
    app.run(debug=True)
