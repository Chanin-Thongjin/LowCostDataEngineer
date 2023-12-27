# The lines `import base64`, `import datetime`, and `import os` are importing Python modules that
# provide additional functionality to the code.
import base64
import datetime
import os

# The line `import requests` is importing the `requests` module, which is a Python library used for
# making HTTP requests. It allows the code to send HTTP requests to a specified URL and retrieve the
# response.
import requests
from google.cloud import bigquery


class Config:
    dataset_id = os.environ.get("dataset_id")
    table_name = os.environ.get("table_name")
    url = os.environ.get("url")


def get_data(url: str) -> dict:
    """Get data via REST API call using requests package

    Args:
        url (str): The URL of target endpoint.
    
    Returns:
        Dictionary of API response
    """
    response = requests.get(url)
    return response.json()


def insert_data(event, context):
    """Background Cloud Function to be triggered by Pub/Sub.
    Args:
         event (dict): The dictionary with data specific to this type of event.
         context (google.cloud.functions.Context): The Cloud Functions event metadata.
    """
    client = bigquery.Client()
    dataset_ref = client.dataset(Config.dataset_id)

    raw = get_data(Config.url)

    #Order of record should suit with Order Column in BQ
    record = [(
        raw["time"]["updatedISO"], 
        raw["bpi"]["THB"]["rate_float"], 
        raw["bpi"]["USD"]["rate_float"]
        )]
    
    table_ref = dataset_ref.table(Config.table_name)
    table = client.get_table(table_ref)
    result = client.insert_rows(table, record)
    return result