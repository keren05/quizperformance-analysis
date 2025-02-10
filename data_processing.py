import requests
import pandas as pd

QUIZ_ENDPOINT = "https://api.jsonserve.com/rJvd7g"
QUIZ_SUBMISSION = "https://api.jsonserve.com/XgAgFJ"
HISTORICAL_DATA = "https://www.jsonkeeper.com/b/LLQT"

def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

def fetch_and_process_data():
    submission_data = fetch_data(QUIZ_SUBMISSION)
    historical_data = fetch_data(HISTORICAL_DATA)

    # Ensure the data is converted into a DataFrame
    if submission_data and isinstance(submission_data, list):
        submission_data = pd.DataFrame(submission_data)
    else:
        submission_data = pd.DataFrame([submission_data])  # Convert single dict to DataFrame

    if historical_data and isinstance(historical_data, list):
        historical_data = pd.DataFrame(historical_data)
    else:
        historical_data = pd.DataFrame([historical_data])  # Convert single dict to DataFrame

    return submission_data, historical_data
