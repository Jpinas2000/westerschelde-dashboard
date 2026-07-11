import requests

def wind_direction(degrees):

    directions = [
        "N",
        "NO",
        "O",
        "ZO",
        "Z",
        "ZW",
        "W",
        "NW"
    ]

    index = round(degrees / 45) % 8

    return directions[index]
def get_weather():

    url = (
        "https://api.open-meteo.com/v1/forecast?"
        "latitude=51.442&"
        "longitude=3.573&"
        "current=temperature_2m,relative_humidity_2m,"
        "pressure_msl,wind_speed_10m,wind_direction_10m"
    )

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        current = data["current"]

        return {
            "temperature": current["temperature_2m"],
            "wind": current["wind_speed_10m"],
            "direction": wind_direction(current["wind_direction_10m"]),
            "pressure": current["pressure_msl"],
            "humidity": current["relative_humidity_2m"]
        }

    except Exception as e:

        print("Weerdata fout:", e)

        return {
            "temperature": "-",
            "wind": "-",
            "direction": "-",
            "pressure": "-",
            "humidity": "-"
        }
