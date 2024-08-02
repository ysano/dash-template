"""
Configuration settings for the Dash application.
"""

import os

APP_NAME = "Weather Data Dashboard"
ENVIRONMENT = os.environ.get("ENVIRONMENT", "development")
GCP_PROJECT = os.environ.get("GCP_PROJECT")
PORT = int(os.environ.get("PORT", 8080))
