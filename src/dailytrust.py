import requests
from bs4 import BeautifulSoup
import src.utils.variables as var
from datetime import datetime
from src.utils.requestfunc import requetfunc
from src.utils.checkpoint import updatecheckpoint, opencheckpoint


states = [state for state in var.states.keys()]
crime = var.crimesList

state_set = set(states)
crime_set = set(crime)

dateformat = datetime

cp = "checkpoints/dailytrust_cp.txt"

# scrap one page document
def dailytrust_scrape_one_page():
    page = 1

    print("--------------- {} started -------------".format(page))

    dailynews_request = requests.get(
        "https://dailytrust.com/topics/crime/page/{}/".format(page), timeout=10).text

    dailynews_request_soup = BeautifulSoup(
        dailynews_request, "lxml")

    newsData = dailynews_request_soup.find_all(
        'div', class_="list_card")

    # search for state in the headlind of each new

    headlins = [head for head in newsData]

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

                    news_req = requests.get(
                        str(link[0].get('href')).strip(), timeout=10).text

                    soup_req = BeautifulSoup(news_req, "lxml")

                    date = soup_req.find_all("div", class_="post-time")[0].text

                    text = [req.text for req in soup_req.find_all("p")]

                    content = content.join(e.lower() for e in text)

                    for lga in var.states[state]:

                        if lga.lower() in content:

                            d = str(date).replace(",", "").strip().split(" ")

                            Date = "{}-{}-{}".format(d[1], d[2], d[3])

                            Lga = lga
                            State = state
                            Crime = crime
                            Source = "dailytrust"

                            newdate = dateformat.strptime(Date, '%d-%b-%Y')

                            # send date to database
                            requetfunc(newdate, State, Lga, Crime, Source)

                            break

        print("--------------- {} ended -------------".format(page))


# scrap all documents
def dailytrust_scrape_all_docx():
    page = 1

    while True:

        print("--------------- {} started -------------".format(page))

        dailynews_request = requests.get(
            "https://dailytrust.com/topics/crime/page/{}/".format(page), timeout=10).text

        dailynews_request_soup = BeautifulSoup(
            dailynews_request, "lxml")

        newsData = dailynews_request_soup.find_all(
            'div', class_="list_card")

        # check if news found
        if len(newsData) == 0:
            break

        # add and get last index
        f = opencheckpoint(cp)
        page = int(f.read())

        # search for state in the headlind of each new

        headlins = [head for head in newsData]

        # print(len(headlins))
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

                        news_req = requests.get(
                            str(link[0].get('href')).strip(), timeout=10).text

                        soup_req = BeautifulSoup(news_req, "lxml")

                        date = soup_req.find_all(
                            "div", class_="post-time")[0].text

                        text = [req.text for req in soup_req.find_all("p")]

                        content = content.join(e.lower() for e in text)

                        for lga in var.states[state]:

                            if lga.lower() in content:

                                d = str(date).replace(
                                    ",", "").strip().split(" ")

                                Date = "{}-{}-{}".format(d[1], d[2], d[3])

                                Lga = lga
                                State = state
                                Crime = crime
                                Source = "dailytrust"

                                newdate = dateformat.strptime(Date, '%d-%b-%Y')

                                # send date to database
                                requetfunc(newdate, State, Lga, Crime, Source)

                                break

        print("--------------- {} ended -------------".format(page))
        page += 1
        updatecheckpoint(cp, page)
