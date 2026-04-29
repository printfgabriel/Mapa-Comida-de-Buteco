
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

    try:
        response_raw = requests.get(
            "https://nominatim.openstreetmap.org/search", 
            params=params, 
            headers=headers,
            timeout=10 
        )
        
        response_raw.raise_for_status() 
        
        response = response_raw.json()

        if not response:
            return None

        lat = float(response[0]["lat"])
        lon = float(response[0]["lon"])
        return (lat, lon)

    except Exception as e:
        print(f"Erro na API: {e}")
        return None


    
    
