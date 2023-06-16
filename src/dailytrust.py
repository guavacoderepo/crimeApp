import requests
from bs4 import BeautifulSoup
import utils.variables as var
from modules.mongo import insert_item
from utils.geocode import geoCoder
from datetime import datetime

states = [state for state in var.states.keys()]
crime = var.crimesList

state_set = set(states)
crime_set = set(crime)

dateformat = datetime

def scrape():
    page = 0

    while True:

        print("--------------- {} started -------------".format(page))

        dailynews_request = requests.get(
            "https://dailytrust.com/topics/crime/page/{}/".format(page), timeout=10).text

        dailynews_request_soup = BeautifulSoup(
            dailynews_request, "lxml")
    

        newsData = dailynews_request_soup.find_all(
            'div', class_="list_card")


        # search for state in the headlind of each new

        headlins = [head for head in newsData]

        print(len(headlins))
        for state in states:

            for id, healine in enumerate(headlins):

                State = ""
                Lga = ""
                Crime = ""
                Date = ""

                headlines = str(healine.text.lower()).replace(
                    "nigerian", " ").replace("nigerias", " ").replace("nigeria", " ")

               
                if state.lower() in headlines:

                       
                    crime = [crime for crime in var.crimesList if crime.lower()
                             in healine.text.lower()]

                    if crime:
                        content = ""

                        try:
                            link = healine.find_all("a")
                        except Exception as e:
                            print(e)


                        print("Pulse")

                        news_req = requests.get(
                            str(link[0].get('href')).strip(), timeout=10).text

                        soup_req = BeautifulSoup(news_req, "lxml")

                        date = soup_req.find_all("div", class_="post-time")[0].text

                        print(Date)

                        text = [req.text for req in soup_req.find_all("p")]
                        
                        content = content.join(e.lower() for e in text)

                        for lga in var.states[state]:
                                

                            if lga.lower() in content:

                                d = str(date).replace(",", "").strip().split(" ")

                                Date = "{}-{}-{}".format(d[1],d[2],d[3])

                                Lga = lga
                                State = state
                                Crime = crime

                                try:
                                    print(Date, State, Lga, Crime, "\n\n")
                                    
                                    loc = geoCoder(loc="{} {}, {}".format(Lga, State, "nigeria"))
                                    
                                    newdate = dateformat.strptime(Date, '%d-%b-%Y')

                                    # print(newdate)

                                    print(loc["formattedAddress"])

                                    insert_item({"state": State, "lga": Lga, "crime": Crime, "date": newdate, "geoCode": {
                                       "formattedAddress":str(loc["formattedAddress"]),
                                       "lng":loc["lng"],
                                       "lat":loc["lat"]
                                    }})

                                except Exception as e:
                                    print(e)

                                break



        print("--------------- {} ended -------------".format(page))
        page += 1


scrape()
