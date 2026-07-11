import requests


def get_water():

    try:

        url = (
            "https://waterwebservices.rijkswaterstaat.nl/"
            "METADATASERVICES/OphalenMeetlocaties/"
        )

        response = requests.get(url, timeout=10)

        # tijdelijke testcontrole
        if response.status_code != 200:
            raise Exception("Rijkswaterstaat niet bereikbaar")


        return {

            "waterlevel": "live koppeling actief",

            "location": "Vlissingen",

            "high": "-",

            "low": "-"

        }


    except Exception as e:

        print("Waterdata fout:", e)

        return {

            "waterlevel": "-",

            "location": "Vlissingen",

            "high": "-",

            "low": "-"

        }
