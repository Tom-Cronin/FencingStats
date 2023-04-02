# Import the necessary modules from Flask
from flask import Flask, render_template, request
from excel_reader import read_excel_file
from fencing_analysis import two_proportion_test
import os

# Create a Flask app instance
app = Flask(__name__)

# Set the path to the Excel file in the /data directory
data_directory = 'data'
excel_file1 = 'pool_round_1.xlsx'  # Replace with the name of your first Excel file
excel_file2 = 'pool_round_2.xlsx'  # Replace with the name of your second Excel file
file_path1 = os.path.join(data_directory, excel_file1)
file_path2 = os.path.join(data_directory, excel_file2)

# Define a route for the root URL ("/") and associate it with a function
@app.route("/", methods=["GET", "POST"])
def index():
    # Render the index.html template and return the resulting HTML
    if request.method == "POST":
        pool1_df = read_excel_file(file_path1)
        pool2_df = read_excel_file(file_path2)
        result_df = two_proportion_test(pool1_df, pool2_df)

        result_table = result_df.to_html(classes="table table-striped table-hover", index=False)
        return render_template("index.html", result_table=result_table)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

# Start the Flask development server if this script is run directly
if __name__ == '__main__':
    app.run(debug=True)
