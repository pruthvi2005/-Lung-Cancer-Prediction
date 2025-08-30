import sys
import os
from serverless_http import handle_request
from flask import Flask

# Add the CODE/FRONT_END directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'CODE', 'FRONT_END'))

# Import your Flask app
from app import app as flask_app

# Create a handler for Netlify Functions
handler = handle_request(flask_app)

# For local testing
if __name__ == '__main__':
    flask_app.run(debug=True)
