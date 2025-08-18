import math
class Country:
    country_df = None  # Class variable to hold the DataFrame

    @classmethod
    def set_country_df(cls, df):
        cls.country_df = df
    
    @classmethod
    def get_country_by_name(cls, name):
        if cls.country_df is None:
            raise ValueError("Country DataFrame is not set.")
        for _, row in cls.country_df.iterrows():
            if row['name'] == name:
                return Country(
                    country=row['country'],
                    latitude=row['latitude'],
                    longitude=row['longitude'],
                    name=row['name']
                )
        return None

    def __init__(self, country, latitude, longitude, name):
        self.country = country
        self.latitude = latitude
        self.longitude = longitude
        self.name = name
    
    def getCountry(self):
        return self.country
    
    def getLatitude(self):
        return self.latitude
    
    def getLongitude(self):
        return self.longitude
    
    def getName(self):
        return self.name
    
    def setCountry(self, country):
        self.country = country

    def setLatitude(self, latitude):
        self.latitude = latitude

    def setLongitude(self, longitude):
        self.longitude = longitude

    def setName(self, name):
        self.name = name

    def calculateDistance(self, other):
        """
        Calculate the distance to another country based on latitude and longitude.
        This is a placeholder for actual distance calculation logic.
        """
        if(type(other) is not Country):
            raise TypeError("The other object must be of type Country")
        r = 6378  # Radius of the Earth in kilometers
        lat1 = math.radians(self.latitude)
        lon1 = math.radians(self.longitude)
        lat2 = math.radians(other.latitude)
        lon2 = math.radians(other.longitude)

        # I found this formula on Wikipedia, Haven't tested it yet.
        dlat = lat2-lat1
        dlon = lon2-lon1

        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        return r * c
    
    def __str__(self):
        return f"Country: {self.country}, Name: {self.name}, Coordinates: ({self.latitude}, {self.longitude})"
    