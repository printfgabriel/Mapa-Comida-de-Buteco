
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


    response = requests.get(f"http://nominatim.openstreetmap.org/search", params=params, headers=headers).json()

    lon = response[0]["lon"]
    lat = response[0]["lat"]
        
    # ATENÇÃO, MAPS USA (lat, lon)
    return (lon,lat)



def testando():

    (X, Y) = getCoordinates("Rua Itauninha 631 Santa Cruz")

    print(f"Coordenada ({X},{Y})")
    print(f"coordenada pra pesquisar no MAPS: ({Y},{X})")
    
    
    
