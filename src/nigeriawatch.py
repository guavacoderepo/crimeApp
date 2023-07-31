import requests
from bs4 import BeautifulSoup
import utils.variables as var
from utils.requestfunc import requetfunc
from datetime import datetime


states = [state for state in var.states.keys()]
crime = var.crimesList

state_set = set(states)
crime_set = set(crime)

dateformat = datetime


url = "https://www.nigeriawatch.org/index.php?urlaction=evtView&id_evt="


# scrap first page
# def nigeriawatch_one_page():
#     page = 1


#     print("--------------- {} started -------------".format(page))

#     nigeriawatchReq = requests.get("{}{}".format(url,3), timeout=10).text

#     nigeriawatch_request_soup = BeautifulSoup(
#         nigeriawatchReq, "lxml")

#     newsData = nigeriawatch_request_soup.find_all(
#         'td', class_="val_champs_form")

#     # search for state in the headlind of each new
#     headlines = [head.text for head in newsData]

#     print(headlines)


#     # print(len(headlins))
#     for state in states:

#         for healine in headlins:

#             State = ""
#             Lga = ""
#             Crime = ""
#             Date = ""

#             headlines = str(healine.text.lower()).replace(
#                 "nigerian", " ").replace("nigerias", " ").replace("nigeria", " ")

#             if state.lower() in headlines:

#                 crime = [crime for crime in var.crimesList if crime.lower()
#                             in healine.text.lower()]

#                 if crime:
#                     content = ""

#                     try:
#                         link = healine.get("href")
#                     except Exception as e:
#                         print(e)

#                     news_req = requests.get(
#                         str(link).strip(), timeout=10).text

#                     soup_req = BeautifulSoup(news_req, "lxml")

#                     date = soup_req.find_all("div", class_="date")[0].text

#                     text = [req.text for req in soup_req.find_all("p")]

#                     content = content.join(e.lower() for e in text)

#                     for lga in var.states[state]:

#                         if lga.lower() in content:

#                             d = str(date).strip().split(" ")

#                             Date = "{}-{}-{}".format(d[0],d[1],d[2])

#                             Lga = lga
#                             State = state
#                             Crime = crime
#                             Source = "guardian"

#                             newdate = dateformat.strptime(Date, '%d-%B-%Y')

#                             # send date to database
#                             requetfunc(newdate, State, Lga, Crime, Source)

#                             break


#     print("--------------- {} ended -------------".format(page))


# scrap all pages
def nigeriawatch_scrape_all_document():
    page = 1

    while True:

        print("--------------- {} started -------------".format(page))

        # check if news exceed a value
        # if len(newsData) == 0:
        #     break

        nigeriawatchReq = requests.get(
            "{}{}".format(url, page), timeout=10).text

        nigeriawatch_request_soup = BeautifulSoup(
            nigeriawatchReq, "lxml")

        newsData = nigeriawatch_request_soup.find_all(
            'td', class_="val_champs_form")

        # search for state in the headlind of each new
        headlines = [head.text for head in newsData]

        # print(headlines)

        # check if news is valid
        if len(headlines) > 3:
            # check the state
            State = headlines[1].split(
                " ")[-1].replace("(", "").replace(")", "")

            Lga = headlines[-1]

            Crime = headlines[1].split(" ")[:-1]

            date = headlines[3]

            Source = headlines[-2].strip()

            place = "{}, {}".format(headlines[6], Lga)

            d = str(date).strip().split("-")

            Date = "{}-{}-{}".format(d[2], d[1], d[0])

            newdate = dateformat.strptime(Date, '%d-%m-%Y')

            # send date to database
            requetfunc(newdate, State, Lga, Crime, Source)

            pass
        else:
            print("no news data")

        print("--------------- {} ended -------------".format(page))
        page += 1


nigeriawatch_scrape_all_document()
