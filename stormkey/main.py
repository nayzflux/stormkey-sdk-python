import requests, json

class Stormkey:
    def __init__(self, appId:str, serviceKey:str, host:str = ""):
        self.appId = appId
        self.serviceKey = serviceKey
        self.host = host
        self.headers = {"X-API-Key": self.serviceKey, "Content-Type": "application/json"}

    def create(self, name:str, ownerId:str):
        """Create a new API key.

        Args:
            name (str) -- the name of the API key
            ownerId (str) -- key owner Id

        Returns:
            key (dict) -- Key object
        """

        data = json.dumps({"name": name, "ownerId": ownerId})

        response = requests.post(f"{self.host}/api/v1/apps/{self.appId}/keys", data = data, headers = self.headers)
        return response.json()["key"]

    def update(self, key_id:str, name:str, ownerId: str):
        """Update the API key.

        Args:
            key_id (str) -- the id of the key
            name (str) -- the name of the API key
            ownerId (str) -- key owner Id

        Returns:
            key (dict) -- Key object
        """

        data = json.dumps({"name": name, "ownerId": ownerId})

        response = requests.patch(f"{self.host}/api/v1/apps/{self.appId}/keys/{key_id}", data = data, headers = self.headers)
        return response.json()["key"]

    def delete(self, key_id:str, name:str):
        """Delete the API key.
        
        Args:
            key_id (str) -- the id of the key
            name (str) -- the name of the API key

        Returns:
            key (dict) -- Key object
        """

        data = json.dumps({"name": name})

        response = requests.delete(f"{self.host}/api/v1/apps/{self.appId}/keys/{key_id}", data = data, headers = self.headers)
        return response.json()["key"]
    
    def verify(self, key:str):
        """Verify the Api key.

        Args:
            key (str) -- your secret API key

        Returns:
            {
                "valid": valid (bool) -- the validity of the key
                "expired": expired (bool) -- True if the key is expired
                "key": key (dict) -- Key object
            }
        """
        data = json.dumps({"key": key})

        response = requests.post(f"{self.host}/api/v1/apps/{self.appId}/keys/verify", data = data, headers = self.headers)
        return response.json()