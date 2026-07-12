import requests
from datetime import datetime, timedelta

URL = "https://waterwebservices.rijkswaterstaat.nl/ONLINEWAARNEMINGENSERVICES_DBO/OphalenLaatsteWaarnemingen"


def get_water():

    eind = datetime.utcnow()
    begin = eind - timedelta(hours=1)

    body = {
        "LocatieLijst": [
            {
                "Code": "VLIS",
                "X": 541518.7459,
                "Y": 5699254.9643
            }
        ],
        "AquoPlusWaarnemingMetadataLijst": [
            {
                "AquoMetadata": {
                    "Compartiment": {
                        "Code": "OW"
                    },
                    "Grootheid": {
                        "Code": "WATHTE"
                    }
                }
            }
        ]
    }

    try:

        response = requests.post(URL, json=body, timeout=15)

        data = response.json()

        waarde = (
            data["WaarnemingenLijst"][0]
            ["MetingenLijst"][0]
            ["Meetwaarde"]["Waarde_Numeriek"]
        )

        tijd = (
            data["WaarnemingenLijst"][0]
            ["MetingenLijst"][0]
            ["Tijdstip"]
        )

        return {
            "waterlevel": f"{waarde:.2f} m NAP",
            "high": "--:--",
            "low": "--:--",
            "update": tijd
        }

    except Exception as fout:

        print(fout)

        return {
            "waterlevel": "--",
            "high": "--",
            "low": "--",
            "update": "--"
        }
