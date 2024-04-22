import requests

def get_quote(mode):
    """
    Description:
        This function interacts with the api to retirieve information
        about a word

    Args:
        word: The target word we want
        whatToGet: This can be information about the word such as synonyms,
                antonyms, definitions etc.
    
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
    
mode = "random"
print(f"{get_quote(mode)}")
