# Imports necessary tools from the flask library
from flask import Flask, render_template, request

# Imports pandas to handle data (my CSV file)
import pandas as pd

# Initializes the Flask application
app = Flask(__name__)

# Loads the data from the CSV file into a pandas DataFrame
df = pd.read_csv('data.csv')


# Defines the route for the homepage (the root URL '/')
# This tells Flask: "When someone visits the main page, run this function."
@app.route("/")
def homepage():
    # Renders the HTML template
    # This tells Flask: "Go find index.html in the templates folder and show it."
    return render_template("index.html")


# Checks if this script is executed directly (not imported)
# This is the standard entry point for Python scripts
if __name__ == "__main__":
    # Starts the Flask development server
    # debug=True allows me to see errors in real-time
    app.run(debug=True)
