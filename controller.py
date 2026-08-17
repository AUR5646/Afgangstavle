from datetime import datetime, timedelta
import requests 



class DepartureBoardController:
    def __init__(self, view, model):
        self.view = view
        self.model = model 

    def getSchedule(self):
        response = self.model.request()
        self.processingData(response)

    def processingData(self, response):
        departureList = response.json()['Departure']
        processed = []

        for departure in departureList:
            name = departure.get("name")
            stop = departure.get("stop")
            time = departure.get("time")
            date = departure.get("date")
            rtTime = departure.get("rtTime")
            rtDate = departure.get("rtDate")
    
    #Hvis bussen ikke er forsinket skal forventet tid være planmæssig tid
            if rtTime == None:
                rtTime = time
                rtDate = date

            depTime = datetime.strptime(rtTime, "%H:%M:%S").time()
            depDate = datetime.strptime(rtDate,"%Y-%m-%d").date()
            rtDep = datetime.combine(depDate, depTime)
            now = datetime.now().replace(microsecond=0)
            timeDelta = rtDep-now
            timeDelta = max(timeDelta, timedelta())
            direction = departure.get("direction")

            if stop == "Carl Jacobsens Vej (Gammel Køge Landevej)":
                processed.append({
                    "name": name,
                    "direction": direction,
                    "scheduled": time,
                    "actual": rtTime,
                    "within": str(timeDelta)
                })

        self.view.display(processed)

               

        



     