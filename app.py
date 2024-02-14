# Import flask and other modules
from flask import Flask, render_template_string, request

# Create a flask app
app = Flask(__name__)

# Define a global variable
global_var = False

# Define a route for the home page
@app.route('/')
def index():
    # Push an app context
    with app.app_context():
        # Render the HTML from a string with the global variable
        return render_template_string('''
        <!doctype html>
        <html>
            <head>
                <title>Flask App</title>
            </head>
            <body>
                <h1>Flask App</h1>
                <p>The global variable is {{ global_var }}</p>
                <form action="/toggle" method="POST">
                    <button type="submit">Toggle</button>
                </form>
            </body>
        </html>
        ''', global_var=global_var)

# Define a route for the toggle button
@app.route('/toggle', methods=['POST'])
def toggle():
    # Access the global variable
    global global_var
    # Toggle the global variable
    global_var = not global_var
    # Redirect to the home page
    return index()
