import sqlite3
import requests
con = sqlite3.connect('D:/Flask_diplom/archives.db')
cur = con.cursor()
cur.close()
con.close()
DATE_ARRAY =[[10,4],[11,4],[12,4],[13,4],[14,4],[15,4],[16,4],[17,4],[18,4],[19,4],[20,4],
            [21,4],[22,4],[23,4],[24,4],[25,4],[26,4],[27,4],[28,4],[29,4],[30,4],
             [1,5],[2,5],[3,5],[4,5],[5,5],[6,5],[7,5],[8,5],[9,5],[10,5],[11,5],[12,5],
             [13,5],[14,5],[15,5],[16,5],[17,5],[18,5],[19,5],[20,5],
            [21,5],[22,5],[23,5],[24,5],[25,5],[26,5],[27,5],[28,5],[29,5],[30,5],[31,5],
            [1,6],[2,6],[3,6],[4,6],[5,6],[6,6],[7,6],[8,6],[9,6],[10,6]
             ]
for i in DATE_ARRAY:
    con = sqlite3.connect('D:/Flask_diplom/archives.db')
    cur = con.cursor()
    dt= str(i[0])+'.'+str(i[1])+'.2019'
    print(dt)
    result = []
    url = "http://www.nbrb.by/API/ExRates/Rates/145?onDate=2019-"+str(i[1])+'-'+str(i[1])
    response = requests.get(url).json()
    result.append(response)
    url = "http://www.nbrb.by/API/ExRates/Rates/292?onDate=2019-" + str(i[1]) + '-' + str(i[1])
    response = requests.get(url).json()
    result.append(response)
    usd =result[0]["Cur_OfficialRate"]
    eur =result[1]["Cur_OfficialRate"]
    cur.execute('insert into "courses"("USD","EUR","DATE") values("'+str(usd)+'","'+str(eur)+'","'+dt+'");')
    res = cur.fetchall()
    con.commit()
    cur.close()
    con.close()