import json
class JsonFetcher:
    def __init__(self):
        with open("veriseti.json", "r", encoding="utf-8") as f:
            self.data = json.load(f)
    
    
    def getAllLatLon(self):
        latLonList = []
        for stop in self.data["duraklar"]:
            latLonList.append((stop["id"], stop["lat"], stop["lon"]))
        return latLonList
    
    def getLatLonById(self, stopId:str):
        for stop in self.data["duraklar"]:
            if(stop["id"] == stopId):
                return stop["lat"], stop["lon"]
        return None
    
    
    def getNextStopsById(self, stopId:str):
        for stop in self.data["duraklar"]:
            if(stop["id"] == stopId):
                return [next_stop["stopId"] for next_stop in stop.get("nextStops", [])]
        return None
    
    
    def getTimeByStops(self, stopId:str, nextStopID:str):
        for stop in self.data["duraklar"]:
            if stop["id"] == stopId:
                for nextStop in stop.get("nextStops", []):
                    if nextStop["stopId"] == nextStopID:
                        return nextStop["sure"]
        return None
    
    
    def isLastStopById(self, stopId:str):
        for stop in self.data["duraklar"]:
            if stop["id"] == stopId:
                return stop["sonDurak"]
        return None

