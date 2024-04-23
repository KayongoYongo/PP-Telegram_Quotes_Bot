import requests

def get_quotes(mode):
    """
    Description:
        This function interacts with the api to retrieve information
        about a quote

    Args:
        mode: This can be random, today or image
    
    Return:
        A JSON response
    """
    # Base url
    url = f"https://zenquotes.io/api/{mode}"

    # The response
    response = requests.get(url)
    # print(dir(response))

    if response.status_code == 200:
        return response.json()
    else:
        return f"There is an error in the request"