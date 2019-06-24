from flask import Flask,render_template,request,url_for,redirect
import parsing

app = Flask(__name__)
City = ['Minsk']
@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/movies")
def movies():
    return render_template('movies.html')

@app.route("/courses")
def courses():
    result = parsing.courses()
    return render_template('courses.html',result =result)
'''
@app.route("/weather")
def weather():
    _city = ''
    try:
        _city = request.form['inputCity']
    except:
        pass
    if _city !='':
        w = parsing.weather(_city)
    else:
        w = parsing.weather("Minsk")
    print(_city)
    return render_template('weather.html',weather_info = w)
'''
@app.route("/weather" ,methods=['GET'])
def weather():
    w = parsing.weather(City[-1])
    return render_template('weather.html',weather_info = w)

@app.route("/add_weather",methods=['POST'])
def add_weather():
    City.append(request.form['inputCity'])
    return redirect(url_for('weather'))


if __name__ == "__main__":
    app.run()