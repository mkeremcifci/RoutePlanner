import json
class JsonFetcher:
    def __init__(self):
        with open("veriseti.json", "r", encoding="utf-8") as f:
            self.data = json.load(f)
            
    def getLatLonById(self, id:str):
        for stop in self.data["duraklar"]:
            if(stop["id"] == id):
                return stop["lat"], stop["lon"]
        return None
    
    def getNextStopsById(self, id:str):
        for stop in self.data["duraklar"]:
            if(stop["id"] == id):
                return [next_stop["stopId"] for next_stop in stop.get("nextStops", [])]
        return None
    
    def isLastStopById(self, id:str):
        for stop in self.data["duraklar"]:
            if stop["id"] == id:
                return stop["sonDurak"]
        return None
        
