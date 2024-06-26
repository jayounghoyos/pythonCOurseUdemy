class Cordenadas:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __eq__(self, otro):#Ya solo con "eq" infiere cual sería lo contrario
        return self.lat == otro.lat and self.lon == otro.lon
    # def __ne__(self, otro):
    #     return self.lat != otro.lat or self.lon != otro.lon

    def __lt__(self,otro):#less than este también infiere lo contrario
        return self.lat + self.lon < otro.lat + otro.lon

    def __le__(self,otro):
        return self.lat + self.lon <= otro.lat + otro.lon
    
coords = Cordenadas(45,43)
coords2 = Cordenadas(45,43)

print(coords != coords2)
print(coords < coords2)
print(coords >= coords2)