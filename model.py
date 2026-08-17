import requests 
from datetime import datetime, timedelta



class DepartureBoardModel:
    def __init__(self):
        self.accessId = "5dfc0766-1dc9-4dcb-889e-a6ae170952a5"
        self.stopID = "000000005454"
        self.basePoint ='https://www.rejseplanen.dk/api/'
        self.endPoint = "departureBoard"
    
    def request(self):
        now = datetime.now()

        # Formatér til "YYYY-MM-DD"
        current_date = now.strftime("%Y-%m-%d")

        # Formatér til "HH:MM"
        current_time = now.strftime ("%H:%M")
        params = {
            "accessId" : self.accessId,
            "id": self.stopID,
            "date" : current_date,
            "time" : current_time,
            "format": "json",
            "useBus": "0"
            }
        url = self.basePoint+self.endPoint
        return requests.get(url,params=params)
    


