import requests
from datetime import datetime, timedelta

class AutomyClient:
    def __init__(self):
        self.base_url = "https://appsaccess.automy.com.br"
        self.token = None
        self.token_expiry = None

    def authenticate(self):
        response = requests.post(
            f"{self.base_url}/login",
            json={"username": "fldoaogopdege", "password": "ygalepsm"}
        )
        self.token = response.json()["token"]
        self.token_expiry = datetime.now() + timedelta(minutes=14)
        return self.token

    def get_races(self, email):
        if not self.token or datetime.now() >= self.token_expiry:
            self.authenticate()
            
        query = f"""
        SELECT * FROM desafio.cadastro_baterias_desafio 
        WHERE email = '{email}'
        """
        
        response = requests.post(
            f"{self.base_url}/api/api/desafio/custom/do/query",
            headers={"Authorization": f"Bearer {self.token}"},
            json={"query": query, "db": "desafio"}
        )
        return response.json()