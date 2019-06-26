import requests
from bs4 import BeautifulSoup
def weather(city):
    """Данная функция парсит информацию о погоде с api.openweathermap.org и возвращает словарь с элементами 'city','temp' и 'icon'"""
    appid = '8d5b972c005f158708ee7dcff89ee7ed'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=' + appid

    res = requests.get(url.format(city)).json() # Получение и преобразование информации в json формат
    city_info = {
        'city': city,# Название город
        'temp': res["main"]["temp"], # Температура в Цельсиях
        'icon': res["weather"][0]["icon"]# Иконка погоды
    }
    return city_info

def courses():
    """Данная функция парсит информацию о курсах доллара и евро с nbrb.by и возвращает словарь с элементами 'USD' и'EUR' """
    result = []
    url = "http://www.nbrb.by/API/ExRates/Rates/145"
    response = requests.get(url).json()# Получение и преобразование информации в json формат
    result.append(response)
    url = "http://www.nbrb.by/API/ExRates/Rates/292"
    response = requests.get(url).json()# Получение и преобразование информации в json формат
    result.append(response)
    courses ={"USD":result[0]["Cur_OfficialRate"],
              "EUR":result[1]["Cur_OfficialRate"]}
    return courses



def get_html(url):
    """Данная функция возвращает весь html код по введённому url"""
    r = requests.get(url)
    return r.text

def get_data(html):
    """Данная функция парсит полученный html код(парсер lxml) и возвращает необходимые данные"""
    soup = BeautifulSoup(html,'lxml')
    h1 = soup.find('div',{'class':'branding'}).find('div',{'class':'branding-w'}).find('div',{'class':'popular_event grey-bg'}).find('a',{'class':'name'}).text
    return h1

def films():
    """Данная функция парсит afisha.tut.by/film/ и возвращает данные о идущем фильме"""
    url = 'https://afisha.tut.by/film/'
    return get_data(get_html(url))


