import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the Flask app
import importlib.util
import sys

# Add the CODE directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'CODE'))

# Import the Flask app using importlib to handle the space in the directory name
spec = importlib.util.spec_from_file_location(
    "app", 
    os.path.join(os.path.dirname(__file__), 'CODE', 'FRONT END', 'app.py')
)
app_module = importlib.util.module_from_spec(spec)
sys.modules["app"] = app_module
spec.loader.exec_module(app_module)
application = app_module.app

if __name__ == "__main__":
    application.run()
