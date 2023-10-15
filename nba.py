import requests
import json
import csv

###########WARNING: THIS CODE IS MEANT TO RUN ONCE################################
info = []
# looping though 52 pages as api call was limit to 100 per page
for i in range(0,53,1):
    url = "https://free-nba.p.rapidapi.com/players"

    querystring = {"page":"{varname}".format(varname=i),"per_page":"5000"}

    headers = {
        #enter your own api key
        "X-RapidAPI-Key": "",
        "X-RapidAPI-Host": "free-nba.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    #converting response to text
    tojson = response.text
    # load it into reponse
    response = json.loads(response.text)
    # adding it into info
    info.append(response)
# to verify that this works
print(info)
#creating a new json file and loading that data
with open('nbainfo.json') as f:
    data = json.load(f)

# creating a csv file
with open('nba.csv', 'w', newline='') as f:
    w = csv.writer(f)
    # writing first row for column
    w.writerow(['Player ID', 'First Name', 'Last Name', 'Postion', 'Team Name'])
    #go though the pages
    for j in data:
        # go though each name info from each page
        for i in j['data']:
            # writing a new row each time
            w.writerow([i['id'], i['first_name'], i['last_name'], i['position'], i['team']['full_name']])

print('ran successfully')




# print(data[0]['data'][1]['id'])
# for j in data:
#     for i in j['data']:
#         print(i['id'], i['first_name'], i['last_name'], i['position'], i['team']['full_name'])
#         count = count + 1

# print(count)




# for j in info:
#     for i in [j]['data']:
#         #print(i)
#         print(i['id'], i['first_name'], i['last_name'], i['position'], i['team']['full_name'])


# for i in range(0,53,1):
#     print(info[i]['data']['id'])
#     count =count +1
# print(count)

