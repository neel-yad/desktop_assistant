from operator import imod
from geopy.geocoders import Nominatim





def get_location():
     # calling the Nominatim tool
    loc = Nominatim(user_agent="GetLoc")
 
    # entering the location name
    getLoc = loc.geocode("kerakat")
 
    # printing address
    print(getLoc.address)
    co_ordinate="Latitude="+str(getLoc.latitude)+"Longitude="+str(getLoc.longitude)
    print(co_ordinate)
    # printing latitude and longitude
    # print("Latitude = ", getLoc.latitude, "\n")
    # print("Longitude = ", getLoc.longitude)

get_location()   