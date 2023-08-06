import requests
from bs4 import BeautifulSoup
import utils.variables as var
from utils.requestfunc import requetfunc
from datetime import datetime

states = [state for state in var.states.keys()]

crime = var.crimesList
state_set = set(states)
crime_set = set(crime)

# set count to break for no news
count = 0

url = "https://www.nigeriawatch.org/index.php?urlaction=evtView&id_evt="


# scrap new pages
def nigeriawatch_scrape_new_document():
    page = 1473
    # start iteration
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
            title = headlines[1].lower().replace(
                "(", "").replace(")", "").replace(",", "")

            print(title)

            # check if state exit
            State = [state for state in states if state.lower() in title]

            # if state is empty look out for lga in title
            if not State:
                # get all lgas for filter
                for k, v in var.states.items():
                    lgaValue = [lga for lga in v if lga.lower() in title]
                    if lgaValue:
                        # set state to index 0 of state list
                        State = [k]
                        break

            # check if state found
            if not State:
                print("no state found.....")
                page += 1
                continue

            # extract lga, crime, date and source
            Lga = headlines[-1]

            crime = [crime for crime in var.crimesList if crime.lower()
                     in title]

            # check if crime exit
            if not crime:
                page += 1
                print("no crime found.........")
                continue

            date = headlines[3]

            Source = "".join(headlines[-2].split())

            # place = "{}, {}".format(headlines[6], Lga)

            d = str(date).strip().split("-")

            Date = "{}-{}-{}".format(d[2], d[1], d[0])

            newdate = datetime.strptime(Date, '%d-%m-%Y')

            # send date to database
            requetfunc(newdate, State[0], Lga, crime, Source)

            pass
        else:
            print("no news data")

        print("--------------- {} ended -------------".format(page))
        page += 1


# scrap all pages
def nigeriawatch_scrape_all_document():
    page = 1

    # start iteration
    while True:

        print("--------------- {} started -------------".format(page))

        # check if "no news" exceed a value "20"
        if count > 20:
            break

        # add and get last index
        f = open("index.txt", "r")

        page = int(f.read())

        # print(page)
        # page index

        nigeriawatchReq = requests.get(
            "{}{}".format(url, page), timeout=10).text

        nigeriawatch_request_soup = BeautifulSoup(
            nigeriawatchReq, "lxml")

        newsData = nigeriawatch_request_soup.find_all(
            'td', class_="val_champs_form")

        # search for state in the headlind of each new
        headlines = [head.text for head in newsData]

        # check if news is valid
        if len(headlines) > 3:
            # reset count to zero when news found
            count = 0

            # check the state
            title = headlines[1].lower().replace(
                "(", "").replace(")", "").replace(",", "")

            print(title)

            # check if state exit
            State = [state for state in states if state.lower() in title]

            # if state is empty look out for lga in title
            if not State:
                # get all lgas for filter
                for k, v in var.states.items():
                    lgaValue = [lga for lga in v if lga.lower() in title]
                    if lgaValue:
                        # set state to index 0 of state list
                        State = [k]
                        break

            # check if state found
            if not State:
                print("no state found.....")
                page += 1
                f = open("index.txt", "w")
                f.write(str(page))
                f.close()
                continue

            # extract lga, crime, date and source
            Lga = headlines[-1]

            crime = [crime for crime in var.crimesList if crime.lower()
                     in title]

            # check if crime exit
            if not crime:
                page += 1
                f = open("index.txt", "w")
                f.write(str(page))
                f.close()
                print("no crime found.........")
                continue

            date = headlines[3]

            Source = "".join(headlines[-2].split())

            # place = "{}, {}".format(headlines[6], Lga)

            d = str(date).strip().split("-")

            Date = "{}-{}-{}".format(d[2], d[1], d[0])

            newdate = datetime.strptime(Date, '%d-%m-%Y')

            # send date to database
            requetfunc(newdate, State[0], Lga, crime, Source)

            pass
        else:
            # add count if no news data found
            count += 1
            print("no news data")

        print("--------------- {} ended -------------".format(page))
        page += 1

        f = open("index.txt", "w")
        f.write(str(page))
        f.close()


nigeriawatch_scrape_all_document()
