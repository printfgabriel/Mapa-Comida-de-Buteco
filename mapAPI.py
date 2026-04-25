
import requests


# Coloca o endereço e recebe as coordenadas
def getCoordinates(query: str):

    params = {
        "q": query,
        "format": "json",
        "polygon": 1,
        "addressdetails": 1,
    }

    headers = {
        "User-Agent": "comida-di-buteco/1.0 ()"
    }


    response = requests.get(f"https://nominatim.openstreetmap.org/search", params=params, headers=headers).json()

    if not response:
        return None

    lon = float(response[0]["lon"])
    lat = float(response[0]["lat"])
        
    # ATENÇÃO, ISSO É (Y,X) PQ MAPS USA (lat, lon), MAS PODE PRECISAR INVERTER 
    return (lat,lon)



def testando():

    (X, Y) = getCoordinates("Rua Itauninha 631 Santa Cruz")

    print(f"Coordenada ({X},{Y})")
    print(f"coordenada pra pesquisar no MAPS: ({Y},{X})")
    
    
    
