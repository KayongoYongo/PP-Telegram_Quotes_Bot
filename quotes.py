import os
from dotenv import load_dotenv
import requests

# load environmental variables
load_dotenv()

def get_quotes(mode_or_category):
    """
    Description:
        This function interacts with the appropriate API to retrieve information
        about a quote based on the mode or category provided.

    Args:
        mode_or_category: This can be 'random', 'today', 'image', or a category for the quote.

    Return:
        A JSON response or an image
    """
    if mode_or_category in ['random','today','image']:
        # Base url for zenquotes.io API
        url = f"https://zenquotes.io/api/{mode_or_category}"

        # The response
        response = requests.get(url)

        # Check if the response is successful
        if response.status_code == 200:
            # Handle a separate instance of an image argument
            if mode_or_category == 'image':
                return response.content
            else:
                return response.json()
        else:
            return f"There is an error in the request to zenquotes.io"
    else:
        # The api key for api-ninjas
        API_KEY = os.getenv('API_KEY')

        # Base Url for api-ninjas.com API
        url = f'https://api.api-ninjas.com/v1/quotes?category={mode_or_category}'

        # The response
        response = requests.get(url, headers={'X-Api-Key': API_KEY})

        # Check if the response is successful
        if response.status_code == 200:
            return response.json()
        else:
            return f"There is an error in the request to api-ninjas.com"