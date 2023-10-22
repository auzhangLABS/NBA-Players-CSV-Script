import requests
import json
import csv


## This run the API call first to see the amount of pages 

info = []
count =0
url = "https://free-nba.p.rapidapi.com/players"

querystring = {"page":"1","per_page":"5000"}

headers = {
    #enter you own API key here
    "X-RapidAPI-Key": "",
    "X-RapidAPI-Host": "free-nba.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
#get the reponse and checking if server is up
if response.status_code == 200:
    # return to user services is ok
    print('Server ok')

    response = json.loads(response.text)
    # append to info
    info.append(response)
    # create a variable with the totatl limit
    total_limit = info[0]['meta']['total_pages'] +1
    #create another loop that loop though the pages to the limit starting at the second page
    for i in range(2,total_limit,1):
        url = "https://free-nba.p.rapidapi.com/players"
        #page number will change depending on I
        querystring = {"page":"{varname}".format(varname=i),"per_page":"5000"}

        headers = {
            #enter your own api key
            "X-RapidAPI-Key": "",
            "X-RapidAPI-Host": "free-nba.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        response = json.loads(response.text)
        # add that to info
        info.append(response)
        # creating a csv file to write
        with open('nba.csv', 'w', newline='') as f:
            w = csv.writer(f)
            # writing first row for column
            w.writerow(['Player ID', 'First Name', 'Last Name', 'Postion', 'Team Name'])
            #go though the pages
            for j in info:
                # go though each name info from each page
                for i in j['data']:
                    # writing a new row each time
                    w.writerow([i['id'], i['first_name'], i['last_name'], i['position'], i['team']['full_name']])
        print('CSV file created successfully')

# if server is not responding 
else:
    print('Server down')


