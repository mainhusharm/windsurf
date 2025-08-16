#!/usr/bin/env python3
"""
Production runner for Trading Journal Flask App
"""
import os
import sys
from pathlib import Path

# Add the project directory to Python path
project_dir = Path(__file__).parent
sys.path.insert(0, str(project_dir))

# Load environment variables
from dotenv import load_dotenv
load_dotenv('.env')

# Set Flask environment
os.environ['FLASK_ENV'] = 'production'

# Import and run the application
from journal import create_production_app

app = create_production_app()

if __name__ == "__main__":
    # For development testing
    app.run(host='0.0.0.0', port=5000, debug=False)
