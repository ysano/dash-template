"""
Module for defining callbacks for the Dash application.
"""

from dash import Input, Output
import plotly.express as px
from app.utils import get_data


def register_callbacks(app):
    """
    Register all callbacks for the Dash application.
    """

    @app.callback(
        Output("graph", "figure"),
        Input("button", "n_clicks"),
    )
    def update_graph(_):
        """
        Update the graph based on button clicks.
        """
        dataframe = get_data()
        fig = px.scatter(
            dataframe, x="month", y="max_temperature", title="Max Temperature"
        )
        return fig
