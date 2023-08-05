import requests
from bs4 import BeautifulSoup
import utils.variables as var
from datetime import datetime
from utils.requestfunc import requetfunc


states = [state for state in var.states.keys()]
crime = var.crimesList

state_set = set(states)
crime_set = set(crime)

status = True


# scrap one page
def sahara_scrape_all_documents():
    page = 1
    date = datetime.now()
    print(date)

    while True:

        print("--------------- {} started -------------".format(page))

        # check scraping status
        if not status:
            break

        saharareporters_request = requests.get(
            "https://saharareporters.com/crime?page={}".format(page), timeout=10).text

        saharareporters_request_soup = BeautifulSoup(
            saharareporters_request, "lxml")

        newsData = saharareporters_request_soup.find_all(
            'h2', class_="title is-3")

        # dates = saharareporters_request_soup.find_all(
        #     'div', class_="card-content-bottom")

        # check if news found
        if len(newsData) == 0:
            break

        # search for state in the headlind of each new

        for state in states:
            headlins = [headline for headline in newsData]

            for headline in headlins:

                State = ""
                Lga = ""
                Crime = ""
                Date = ""

                headlineTxt = str(headline.text.lower()).replace(
                    "nigerian", " ").replace("nigerias", " ").replace("nigeria", " ")

                # print(len(headlines))

                # print(headlines)
                if state.lower() in headlineTxt:

                    crime = [crime for crime in var.crimesList if crime.lower()
                             in headline.text.lower()]

                    if crime:
                        content = ""

                        # print(headline)

                        try:
                            link = headline.find_all("a")
                        except Exception as e:
                            print(e)

                        news_req = requests.get(
                            "https://saharareporters.com"+link[0].get('href'), timeout=10).text

                        soup_req = BeautifulSoup(news_req, "lxml")

                        text = [req.text for req in soup_req.find_all(
                            "div", property="schema:text")]

                        dates = soup_req.find_all(
                            'div', class_="column is-3 group-left")

                        content = content.join(e.lower() for e in text)

                        for lga in var.states[state]:

                            if lga.lower() in content:

                                Date = str(dates[0].find_all("div")[
                                    0].text).replace(",", "").strip().replace(" ", "-")

                                Lga = lga
                                State = state
                                Crime = crime
                                Source = "sahara"

                                # format date
                                newdate = datetime.strptime(Date, '%B-%d-%Y')

                                # send date to database
                                # print(newdate)
                                print(content)
                                # print(text)
                                # requetfunc(newdate, State, Lga, Crime, Source)

                                break

        print("--------------- {} ended -------------".format(page))
        page += 1


# scrap all documents
def sahara_scrape_one_page():
    page = 1

    while True:

        print("--------------- {} started -------------".format(page))

        saharareporters_request = requests.get(
            "https://saharareporters.com/crime?page={}".format(page), timeout=10).text

        saharareporters_request_soup = BeautifulSoup(
            saharareporters_request, "lxml")

        newsData = saharareporters_request_soup.find_all(
            'h2', class_="title is-3")

        dates = saharareporters_request_soup.find_all(
            'div', class_="card-content-bottom")

        # check if news found
        if len(newsData) == 0:
            break

        # search for state in the headlind of each new

        for state in states:
            headlins = [headline for headline in newsData]

            for id, healine in enumerate(headlins):

                State = ""
                Lga = ""
                Crime = ""
                Date = ""

                headlines = str(healine.text.lower()).replace(
                    "nigerian", " ").replace("nigerias", " ").replace("nigeria", " ")

                # print(headlines)
                if state.lower() in headlines:

                    crime = [crime for crime in var.crimesList if crime.lower()
                             in healine.text.lower()]

                    if crime:
                        content = ""

                        try:
                            link = healine.find_all("a")
                        except Exception as e:
                            print(e)

                        news_req = requests.get(
                            "https://saharareporters.com"+link[0].get('href'), timeout=10).text

                        soup_req = BeautifulSoup(news_req, "lxml")

                        text = [req.text for req in soup_req.find_all(
                            "div", property="schema:text")]

                        content = content.join(e.lower() for e in text)

                        for lga in var.states[state]:

                            if lga.lower() in content:

                                Date = str(dates[id].find_all("div")[
                                    0].text).replace(",", "").strip().replace(" ", "-")

                                Lga = lga
                                State = state
                                Crime = crime
                                Source = "sahara"

                                # format date
                                newdate = datetime.strptime(Date, '%B-%d-%Y')

                                # send date to database
                                requetfunc(newdate, State, Lga, Crime, Source)

                                break

        print("--------------- {} ended -------------".format(page))
        page += 1
