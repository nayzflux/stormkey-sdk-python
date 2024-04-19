import requests, json

class StormKey:
    def __init__(self, appId:str, serviceKey:str, host:str = ""):
        self.appId = appId
        self.serviceKey = serviceKey
        self.host = host
        self.headers = {"X-API-Key": self.serviceKey, "Content-Type": "application/json"}

    def create(self, name:str, ownerId:str):
        data = json.dumps({"name": name, "ownerId": ownerId})

        response = requests.post(f"{self.host}/api/v1/apps/{self.appId}/keys", data = data, headers = self.headers)
        return response.json()["key"]

    def update(self, name:str, ownerId:str):
        data = json.dumps({"name": name, "ownerId": ownerId})

        response = requests.patch(f"{self.host}/api/v1/apps/{self.appId}/keys", data = data, headers = self.headers)
        return response.json()["key"]
    
    def verify(self, key:str):
        data = json.dumps({"key": key})

        response = requests.post(f"{self.host}/api/v1/apps/{self.appId}/keys/verify", data = data, headers = self.headers)
        return response.json()

    def delete(self, name:str):
        data = json.dumps({"name": name})

        response = requests.delete(f"{self.host}/api/v1/apps/{self.appId}/keys", data = data, headers = self.headers)
        return response.json()["key"]