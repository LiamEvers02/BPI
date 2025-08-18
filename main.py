from reader import Reader
from person import *
from country import Country

if __name__ == "__main__":
    reader = Reader()
    Country.set_country_df(reader.getCountryDataFrame())
    participants = reader.get_participants()
    print(participants[3])
    print(participants[7])
    print(participants[3].getCountry().calculateDistance(participants[7].getCountry()))