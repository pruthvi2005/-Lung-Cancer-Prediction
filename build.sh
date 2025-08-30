#!/bin/bash

# Print Python version for debugging
python --version

# Install dependencies
pip install -r requirements.txt

# Create necessary directories
mkdir -p netlify/functions/app

# Copy required files to the functions directory
cp -r CODE/FRONT_END/* netlify/functions/app/

# Make the build script executable
chmod +x build.sh
