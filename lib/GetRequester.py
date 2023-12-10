import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.content
        except requests.RequestException as e:
            print(f"error fetching response: {e}")
            return None
        
    def load_json(self):
        data = self.get_response_body()
        if data:
            try:
                return json.loads(data)
            except json.JSONDecodeError as e:
                # Handle JSON decoding errors
                print(f"Error decoding JSON: {e}")
                return None
        return None