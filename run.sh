#!/bin/bash
# Citizen Feedback on Road Maintenance - Run Script for Mac/Linux

echo ""
echo "========================================"
echo "Starting Road Maintenance Portal..."
echo "========================================"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "ERROR: Virtual environment not found!"
    echo "Please run setup.sh first"
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

echo "Activating virtual environment..."
echo ""
echo "Starting Flask development server..."
echo ""
echo "The application will be available at:"
echo "  http://localhost:5000"
echo ""
echo "Admin Login:"
echo "  Email: admin@example.com"
echo "  Password: admin123"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""
echo ""

python app.py
