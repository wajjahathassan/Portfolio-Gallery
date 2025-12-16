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
    # Converts the pandas DataFrame into a list of dictionaries (records)
    # 'records' format looks like: [{'id': 1, 'title': 'Forest'...}, {'id': 2...}]
    # This makes it easy for the HTML page to loop through each item
    projects = df.to_dict('records')

    # Renders the HTML template and passes the project data to it
    # verifying the data transfer by naming the variable 'projects' for the template
    return render_template("index.html", projects=projects)


# Checks if this script is executed directly (not imported)
# This is the standard entry point for Python scripts
if __name__ == "__main__":
    # Starts the Flask development server
    # debug=True allows me to see errors in real-time
    app.run(debug=True)
