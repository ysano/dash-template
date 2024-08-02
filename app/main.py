"""
Main module for initializing and configuring the Dash application.
"""

from dash import Dash
from app.layout import create_layout
from app.callbacks import register_callbacks

app = Dash(__name__)
app.layout = create_layout()
register_callbacks(app)
server = app.server
