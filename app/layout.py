"""
Module for defining the layout of the Dash application.
"""

from dash import html, dcc


def create_layout():
    """
    Create and return the layout for the Dash application.
    """
    return html.Div(
        [
            html.H1("Weather Data"),
            dcc.Graph(id="graph"),
            html.Button("Update", id="button", n_clicks=0),
        ]
    )
