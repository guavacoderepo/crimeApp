from geopy.geocoders import Nominatim


def geoCoder(loc=""):
    geolocator = Nominatim(timeout=10, user_agent="Krukarius")

    location = geolocator.geocode(loc)

    try:
        lat = location.latitude
        lng = location.longitude
        addr = location

        if location != None:
            return {"formattedAddress": addr, "lat": lat, "lng": lng}
        else:
            return {"formattedAddress": loc, "lat": 0.000000, "lng": 0.000000}
    except:
        return {"formattedAddress": loc, "lat": 0.000000, "lng": 0.000000}


# geoCoder()
