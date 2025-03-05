import math

from Services.JsonFetcher import JsonFetcher

class ShortestRouter:
    def __init__(self):
        self.json = JsonFetcher()

    def chooseWalkOrTaxi(self, userLat:float, userLon:float):
        stop = self.findTargetStop(userLat, userLon)
        
        distance = math.sqrt((stop[1] - userLat)**2 + (stop[2] - userLon)**2)
        #1km = 0.00312 birim
        if(distance/0.00312 < 3):
            return False
        else:
            return True
    
    def findTargetStop(self, userLat:float, userLon:float):
        nearestStop = None
        minDistance = float("inf")
        for id, lat, lon in self.json.getAllLatLon():
            distance = math.sqrt((lat - userLat)**2 + (lon - userLon)**2)
            if distance < minDistance:
                minDistance = distance
                nearestStop = (id,lat,lon)
        return nearestStop        