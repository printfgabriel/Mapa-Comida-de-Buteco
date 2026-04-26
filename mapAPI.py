
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

<<<<<<< Updated upstream
    try: 
        response_raw = requests.get(f"https://nominatim.openstreetmap.org/search", params=params, headers=headers, timeout=10)
        response_raw.raise_for_status()
        response=response_raw.json()
=======
    try:
        response_raw = requests.get(
            "https://nominatim.openstreetmap.org/search", 
            params=params, 
            headers=headers,
            timeout=10 
        )
        
        response_raw.raise_for_status() 
        
        response = response_raw.json()
>>>>>>> Stashed changes

        if not response:
            return None

<<<<<<< Updated upstream
        lon = float(response[0]["lon"])
        lat = float(response[0]["lat"])
            
        # ATENÇÃO, ISSO É (Y,X) PQ MAPS USA (lat, lon), MAS PODE PRECISAR INVERTER 
        return (lat,lon)
    
    except Exception as e:
        print(f"ERRO NA API: {e}\n")
=======
        lat = float(response[0]["lat"])
        lon = float(response[0]["lon"])
        return (lat, lon)

    except Exception as e:
        print(f"Erro na API: {e}")
>>>>>>> Stashed changes
        return None



def testando():

    (X, Y) = getCoordinates("Torre Eiffel")

    print(f"Coordenada ({X},{Y})")
    print(f"coordenada pra pesquisar no MAPS: ({Y},{X})")
    
    
    
