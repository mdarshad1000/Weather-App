from flask import Flask, render_template, request
import requests


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        city_name = request.form.get('city')

        # Takes the Json data
        r = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city_name + "&appid=bd13a5e4c2c7bd4b68f4fd1d2b96db76")

        # Reads the json object
        json_obj = r.json()

        # Attributes to display on the webapp
        temp = float(json_obj['main']['temp'])  # in kelvin
        pressure = float(json_obj['main']['pressure'])
        humidity = float(json_obj['main']['humidity'])
        in_celsius = temp-273.15  # converts in Celsius
        temperature = "{:.2f}".format(in_celsius)  # displays result up to 2 decimal places
        wind = int(json_obj['wind']['speed'])

        return render_template('weather.html', wind=wind, temperature=temperature, pressure=pressure, humidity=humidity, city_name=city_name)
    else:
        return render_template('weather.html')


if __name__ == '__main__':
    app.run(debug=True)
