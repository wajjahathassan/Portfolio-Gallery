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
    # Defines a status message to verify the server is running
    system_status = "System Online: Gallery App is Running"

    # Returns the variable to the browser so the user can see it
    return system_status


# Checks if this script is executed directly (not imported)
# This is the standard entry point for Python scripts
if __name__ == "__main__":
    # Starts the Flask development server
    # debug=True allows me to see errors in real-time
    app.run(debug=True)
