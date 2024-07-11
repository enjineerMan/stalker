import requests

API_KEY = "AIzaSyBgPLxvCygoZhQZyQSZrSQBISEtbbwQkAk"
CX = "667cf32ad39e644dd"
def google_search(search_string):
    ENDPOINT = "https://customsearch.googleapis.com/customsearch/v1?key={}&cx={}&q={}".format(API_KEY, CX, search_string)
    try:
        response = requests.get(ENDPOINT, params=None)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        # Handle any errors that occur during the request
        print(f"An error occurred: {e}")
        return None