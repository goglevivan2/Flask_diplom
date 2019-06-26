from flask import Flask,render_template,request,url_for,redirect
import parsing
import sql_operations

app = Flask(__name__)
City = ['Minsk']
Date = ['1.6.2019']
'''В данном файле основная работа'''
@app.route("/")
def hello():
    '''Отображение главной страницы'''
    return render_template('index.html')

@app.route("/movies")
def movies():
    '''Отображение страницы с фильмом'''
    name_movie = parsing.films()# Парсим фильмы с afisha.tut.by/film/
    return render_template('movies.html', film=name_movie)

@app.route("/courses")
def courses():
    '''Отображение страницы с курсом валюты'''
    result = parsing.courses()# Парсим информацию о курсах валют с nbrb.by/API
    return render_template('courses.html',result =result)

@app.route("/weather" ,methods=['GET'])
def weather():
    '''Отображение страницы с погодой'''
    """Дефолтное значение города: Minsk"""
    try:
        w = parsing.weather(City[-1])# Парсим погоду с api.openweathermap.org. Берём последний записаный город
    except:
        w = parsing.weather('Minsk')# При ошибочном вводе названия города- показываем минскую погоду
    return render_template('weather.html',weather_info = w)

@app.route("/add_weather",methods=['POST'])
def add_weather():
    """Обновление страницы с погодоц (после нажатия кнопки и ввода нужного города)"""
    City.append(request.form['inputCity'])# Получаем название города из формы
    return redirect(url_for('weather'))# Обновление страницы с погодой

@app.route("/archives")
def archives():
    """Отображение страницы с архивом записей от 10 апреля до 10 июня 2019.(информация о фильме,температуре в Минске и курсах валют)"""
    """Дефолтное значение даты:1.6.2019"""
    date_info=[]
    date = Date[-1]
    try:
        date_info.append(sql_operations.m_sql(date))
        date_info.append(sql_operations.w_sql(date))
        date_info.append(sql_operations.c_sql(date))
    except:
        date_info.append(sql_operations.m_sql('1.6.2019'))
        date_info.append(sql_operations.w_sql('1.6.2019'))
        date_info.append(sql_operations.c_sql('1.6.2019'))
        # Если ошибка - ввод информашии за 1.6.2019
    return render_template('archives.html',date_info = date_info)

@app.route("/add_archives",methods=['POST'])
def add_archives():
    """Обновление страницы архива (после нажатия кнопки и ввода нужной даты)"""
    Date.append(request.form['inputDate']) # Получаем дату из формы из формы
    return redirect(url_for('archives'))# Обновление страницы архива
if __name__ == "__main__":
    app.run()