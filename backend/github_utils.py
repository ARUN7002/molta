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


def get_all_repository_files(api_url, path=""):
    """
    Recursively traverse every folder in a GitHub repository.
    Returns every file and folder.
    """

    all_items = []

    contents = get_repository_contents(api_url, path)

    for item in contents:

        all_items.append(item)

        if item["type"] == "dir":

            sub_items = get_all_repository_files(
                api_url,
                item["path"]
            )

            all_items.extend(sub_items)

    return all_items