"""
Utility functions for the Dash application.
"""

import os
import json
import logging

from google.cloud import bigquery
from google.cloud import bigquery_storage
from google.cloud import secretmanager_v1 as secretmanager
from google.auth.exceptions import DefaultCredentialsError
from google.api_core.exceptions import PermissionDenied

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


ENVIRONMENT = os.environ.get("ENVIRONMENT", "development")


def get_bigquery_clients():
    """
    Initialize and return a BigQuery client based on the environment.
    """
    try:

        if ENVIRONMENT == "production":
            secret_client = secretmanager.SecretManagerServiceClient()
            secret_name = f"projects/{os.environ['GCP_PROJECT']}/secrets/bigquery-credentials/versions/latest"
            response = secret_client.access_secret_version(
                request={"name": secret_name}
            )
            credentials_json = json.loads(response.payload.data.decode("UTF-8"))
            bigquery.Client.from_service_account_info(credentials_json)
            bqstorage_client = (
                bigquery_storage.BigQueryReadClient.from_service_account_info(
                    credentials_json
                )
            )
        else:
            bq_client = bigquery.Client()
            bqstorage_client = bigquery_storage.BigQueryReadClient()
        return bq_client, bqstorage_client
    except DefaultCredentialsError as e:
        error_message = f"Failed to create BigQuery clients: {str(e)}"
        logger.error(error_message)
        return None, None


BQ_CLIENT, BQSTORAGE_CLIENT = get_bigquery_clients()


def get_data():
    """
    Fetch weather data from BigQuery.
    """
    if BQ_CLIENT is None:
        logger.error("BigQuery client is not initialized")
        return None

    query = """
    SELECT *
    FROM `bigquery-public-data.samples.gsod`
    WHERE year = 2010 AND station_number = 725030
    LIMIT 1000
    """

    try:
        # First, try to use BigQuery Storage API
        if BQSTORAGE_CLIENT:
            try:
                df = (
                    BQ_CLIENT.query(query)
                    .result()
                    .to_dataframe(bqstorage_client=BQSTORAGE_CLIENT)
                )
                logger.info("Successfully used BigQuery Storage API")
                return df
            except PermissionDenied:
                logger.warning(
                    "Permission denied for BigQuery Storage API, falling back to standard API"
                )

        # Fallback to standard BigQuery API
        df = BQ_CLIENT.query(query).result().to_dataframe()
        logger.info("Successfully used standard BigQuery API")
        return df
    except DefaultCredentialsError as e:
        error_message = f"Error executing BigQuery query: {str(e)}"
        logger.error(error_message)
        return None
