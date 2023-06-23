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



# scrap first page
def guardian_scrape_one_page():
    page = 1


    print("--------------- {} started -------------".format(page))

    guardian_request = requests.get("https://guardian.ng/?s=nigeria+crime&page={}".format(page+1), timeout=10).text
    
    guardian_request_soup = BeautifulSoup(
        guardian_request, "lxml")

    newsData = guardian_request_soup.find_all(
        'div', class_="headline")

    # search for state in the headlind of each new
    headlins = [head.a for head in newsData]


    # print(len(headlins))
    for state in states:

        for healine in headlins:

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
                        link = healine.get("href")
                    except Exception as e:
                        print(e)


                    news_req = requests.get(
                        str(link).strip(), timeout=10).text
                    
                    soup_req = BeautifulSoup(news_req, "lxml")

                    date = soup_req.find_all("div", class_="date")[0].text

                    text = [req.text for req in soup_req.find_all("p")]
                    
                    content = content.join(e.lower() for e in text)

                    for lga in var.states[state]:

                        if lga.lower() in content:

                            d = str(date).strip().split(" ")

                            Date = "{}-{}-{}".format(d[0],d[1],d[2])

                            Lga = lga
                            State = state
                            Crime = crime
                            Source = "guardian"

                            newdate = dateformat.strptime(Date, '%d-%B-%Y')

                            # send date to database
                            requetfunc(newdate, State, Lga, Crime, Source)

                            break



    print("--------------- {} ended -------------".format(page))




# scrap all pages 
def guardian_scrape_all_document():
    page = 1

    while True:

        print("--------------- {} started -------------".format(page))

        guardian_request = requests.get("https://guardian.ng/?s=nigeria+crime&page={}".format(page+1), timeout=10).text
        
        guardian_request_soup = BeautifulSoup(
            guardian_request, "lxml")

        newsData = guardian_request_soup.find_all(
            'div', class_="headline")
        
        # check if news found
        if len(newsData) == 0:
            break
            
        # search for state in the headlind of each new
        headlins = [head.a for head in newsData]

        
        # print(len(headlins))
        for state in states:

            for healine in headlins:

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
                            link = healine.get("href")
                        except Exception as e:
                            print(e)


                        news_req = requests.get(
                            str(link).strip(), timeout=10).text
                        
                        soup_req = BeautifulSoup(news_req, "lxml")

                        date = soup_req.find_all("div", class_="date")[0].text

                        text = [req.text for req in soup_req.find_all("p")]
                        
                        content = content.join(e.lower() for e in text)

                        for lga in var.states[state]:

                            if lga.lower() in content:

                                d = str(date).strip().split(" ")

                                Date = "{}-{}-{}".format(d[0],d[1],d[2])

                                Lga = lga
                                State = state
                                Crime = crime
                                Source = "guardian"

                                newdate = dateformat.strptime(Date, '%d-%B-%Y')

                                # send date to database
                                requetfunc(newdate, State, Lga, Crime, Source)
                                
                                break



        print("--------------- {} ended -------------".format(page))
        page += 1