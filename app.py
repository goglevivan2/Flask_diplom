from flask import Flask,render_template,request,url_for,redirect
import parsing
import sql_operations

app = Flask(__name__)
City = ['Minsk']
Date = ['1.6.2019']
@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/movies")
def movies():
    name_movie = parsing.films()
    return render_template('movies.html', film=name_movie)

@app.route("/courses")
def courses():
    result = parsing.courses()
    return render_template('courses.html',result =result)

@app.route("/weather" ,methods=['GET'])
def weather():
    w = parsing.weather(City[-1])
    return render_template('weather.html',weather_info = w)

@app.route("/add_weather",methods=['POST'])
def add_weather():
    City.append(request.form['inputCity'])
    return redirect(url_for('weather'))

@app.route("/archives")
def archives():
    date_info=[]
    date = Date[-1]
    date_info.append(sql_operations.m_sql(date))
    date_info.append(sql_operations.w_sql(date))
    date_info.append(sql_operations.c_sql(date))
    return render_template('archives.html',date_info = date_info)

@app.route("/add_archives")
def add_archives():
    Date.append(request.form['inputDate'])
    return redirect(url_for('archives'))
if __name__ == "__main__":
    app.run()