from flask import Flask,render_template,request,url_for,redirect
import parsing

app = Flask(__name__)
City = ['Minsk']
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


if __name__ == "__main__":
    app.run()