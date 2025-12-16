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
    # Gets the data from the URL (the form)
    # If the user didn't type anything, these will be None (empty)
    query = request.args.get('query')
    category = request.args.get('category')

    # Starts with the full dataset
    # I created a copy here so the original data isn't messed up
    filtered_df = df.copy()

    # Applies Category Filter (if selected)
    if category:
        # Keeps only the rows where the 'category' column matches the user's choice
        filtered_df = filtered_df[filtered_df['category'] == category]

    # Applies Keyword Search (if typed)
    if query:
        # Searches in both 'title' and 'description' columns
        # case=False means "Nature" and "nature" are treated the same
        filtered_df = filtered_df[filtered_df['title'].str.contains(
            query, case=False) | filtered_df['description'].str.contains(query, case=False)]

    # Converts the (potentially filtered) data to a dictionary
    projects = filtered_df.to_dict('records')

    # Sends the result to the browser
    return render_template('index.html', projects=projects)


    # Checks if this script is executed directly (not imported)
    # This is the standard entry point for Python scripts
if __name__ == "__main__":
    # Starts the Flask development server
    # debug=True allows me to see errors in real-time
    app.run(debug=True)
