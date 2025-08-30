import sys
import os
from aws_wsgi import make_lambda_handler
from flask import Flask, request, jsonify

# Add the CODE/FRONT_END directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'CODE', 'FRONT_END'))

# Import your Flask app
from app import app as flask_app

# Create a handler for Netlify Functions
handler = make_lambda_handler(flask_app)

def lambda_handler(event, context):
    return handler(event, context)

# For local testing
if __name__ == '__main__':
    flask_app.run(debug=True)
