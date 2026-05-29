import requests


# =========================================
# API KEY
# =========================================

API_KEY = "9b5069023429134e43f62d0ebffb9c5f"



# =========================================
# SIMPLE WEATHER
# =========================================

def get_weather(lat, lon):

    try:

        url = (

            f"https://api.openweathermap.org/data/2.5/weather?"

            f"lat={lat}"

            f"&lon={lon}"

            f"&appid={API_KEY}"

            f"&units=metric"
        )


        response = requests.get(url)

        data = response.json()


        temperature = data['main']['temp']

        humidity = data['main']['humidity']

        condition = data['weather'][0]['main']


        rainfall = 0

        if 'rain' in data:

            rainfall = data['rain'].get(
                '1h',
                0
            )


        return (

            temperature,
            humidity,
            rainfall,
            condition
        )

    except Exception as e:

        print("Weather Error:", e)

        return (

            25,
            60,
            0,
            "Clear"
        )



# =========================================
# DETAILED WEATHER
# =========================================

def get_detailed_weather(lat, lon):

    try:

        url = (

            f"https://api.openweathermap.org/data/2.5/weather?"

            f"lat={lat}"

            f"&lon={lon}"

            f"&appid={API_KEY}"

            f"&units=metric"
        )


        response = requests.get(url)

        data = response.json()


        rainfall = 0

        if 'rain' in data:

            rainfall = data['rain'].get(
                '1h',
                0
            )


        return {

            "temperature":
            data['main']['temp'],

            "humidity":
            data['main']['humidity'],

            "pressure":
            data['main']['pressure'],

            "rainfall":
            rainfall,

            "condition":
            data['weather'][0]['main'],

            "description":
            data['weather'][0]['description'],

            "wind_speed":
            data['wind']['speed'],

            "city":
            data.get('name', 'Unknown')
        }

    except Exception as e:

        print("Detailed Weather Error:", e)

        return {

            "temperature": 25,

            "humidity": 60,

            "pressure": 1000,

            "rainfall": 0,

            "condition": "Clear",

            "description": "clear sky",

            "wind_speed": 0,

            "city": "Unknown"
        }