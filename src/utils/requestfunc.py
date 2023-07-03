# add scr. on all utils

from modules.mongo import insert_item
from utils.geocode import geoCoder
from utils.categories import categorize
from datetime import datetime

dateformat = datetime


def requetfunc(newdate, State, Lga, Crime, Source):

    try:

        loc = geoCoder(loc="{} {}, {}".format(Lga, State, "nigeria"))
        
        # get crime category 
        category = categorize(Crime)

        # insert into mongo 
        insert_item({"state": State, "lga": Lga, "crime": category, "date": newdate, "source": Source, 
                        "geoCode": {
                        "formattedAddress":str(loc["formattedAddress"]),
                        "lng":loc["lng"],
                        "lat":loc["lat"]
                    }})

    except Exception as e:
        print(e)