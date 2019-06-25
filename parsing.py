import requests
from bs4 import BeautifulSoup
def weather(city):
    appid = '8d5b972c005f158708ee7dcff89ee7ed'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=' + appid

    res = requests.get(url.format(city)).json()
    city_info = {
        'city': city,
        'temp': res["main"]["temp"],
        'icon': res["weather"][0]["icon"]
    }
    return city_info

def courses():
    result = []
    url = "http://www.nbrb.by/API/ExRates/Rates/145"
    response = requests.get(url).json()
    result.append(response)
    url = "http://www.nbrb.by/API/ExRates/Rates/292"
    response = requests.get(url).json()
    result.append(response)
    courses ={"USD":result[0]["Cur_OfficialRate"],
              "EUR":result[1]["Cur_OfficialRate"]}
    return courses



def get_html(url):
    r = requests.get(url)
    return r.text

def get_data(html):
    soup = BeautifulSoup(html,'lxml')
    h1 = soup.find('div',{'class':'branding'}).find('div',{'class':'branding-w'}).find('div',{'class':'popular_event grey-bg'}).find('a',{'class':'name'}).text
    return h1

def films():
    url = 'https://afisha.tut.by/film/'
    return get_data(get_html(url))


