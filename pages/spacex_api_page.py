import requests

class SpaceXApiPage:

    def __init__(self):
        # Base URL
        self.base_url = "https://api.spacexdata.com/v4"

    # Method to fetch the latest launch details.
    def get_latest_launch(self):
        url = f"{self.base_url}/launches/latest"
        response = requests.get(url)
        return response