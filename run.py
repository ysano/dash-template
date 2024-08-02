"""
Entry point for the Dash application.
"""

from app.main import app

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8080)
