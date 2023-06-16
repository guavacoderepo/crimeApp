from geopy.geocoders import Nominatim


def geoCoder(loc="Adamawa Adamawa"):
    geolocator = Nominatim(timeout=10, user_agent="Krukarius")

    location = geolocator.geocode(loc)

    lat = location.latitude
    lng = location.longitude
    addr =  location

    if location != None:
        return {"formattedAddress":addr, "lat":lat, "lng":lng}
    else:
        return {"formattedAddress":loc, "lat":"", "lng":""}
# geoCoder()