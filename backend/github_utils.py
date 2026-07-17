import requests


def get_repository_metadata(api_url):
    """
    Fetch repository metadata from GitHub.
    """

    response = requests.get(api_url)

    if response.status_code != 200:
        return None

    return response.json()


def get_repository_contents(api_url, path=""):
    """
    Fetch repository contents for a given path.
    """

    contents_url = f"{api_url}/contents/{path}"

    response = requests.get(contents_url)

    if response.status_code != 200:
        return []

    return response.json()