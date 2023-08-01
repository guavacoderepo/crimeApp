# add scr. on all utils

from modules.mongo import insert_item
from utils.geocode import geoCoder
from utils.categories import categorize
from datetime import datetime
import pandas as pd


dateformat = datetime


def requetfunc(newdate, State, Lga, Crime, Source):

    try:

        loc = geoCoder(loc="{} {}, {}".format(Lga, State, "nigeria"))

        # get crime category
        category = categorize(Crime)


################################################# Start CSV ##################################################

        # create a csv
        # data = {
        #     "state": [State],
        #     "lga": [Lga],
        #     "crime": [category],
        #     "date": [newdate],
        #     "source": [Source],
        #     "formattedAddress": [str(loc["formattedAddress"])],
        #     "lng": [loc["lng"]],
        #     "lat": [loc["lat"]]
        # }

        # # Make data frame of above data

        # df = pd.DataFrame(data)

        # # append data frame to CSV file

        # df.to_csv('data.csv', mode='a', index=False, header=False)

############################################ End CSV #######################################################
        # print message
        print("Data appended successfully.")

        # insert into mongo
        # insert_item({"state": State, "lga": Lga, "crime": category, "date": newdate, "source": Source,
        #              "geoCode": {
        #                  "formattedAddress": str(loc["formattedAddress"]),
        #                  "lng": loc["lng"],
        #                  "lat": loc["lat"]
        #              }})

    except Exception as e:
        print(e)
