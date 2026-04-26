import random
from dash import callback, Output, Input, no_update
import dash_leaflet as dl
from mapAPI import getCoordinates

def update_markers(n=5):
    markers = []
    for i in range(n):
        lat = -23 + random.uniform(-0.5, 0.5)
        lon = -46 + random.uniform(-0.5, 0.5)
        color = random.choice(["red", "blue", "green", "orange", "purple"])
        markers.append(
            dl.Marker(
                position=[lat, lon],
                children=dl.Tooltip(f"Marker {i+1}"),
                icon={
                    # "iconUrl": f"https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-{color}.png",
                    "iconUrl": "/static/marker_food.png",
                    "iconSize": [60, 60],
                    #0.6
                    "iconAnchor": [30, 41],
                    "shadowUrl": "https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png",
                    "shadowSize": [41, 41]
                }
            )
        )
    return markers

def update_rectangle(center=(-23.0,-46.0), diagonal=1):
    half = diagonal/2
    lat, lon = center
    bounds = [[lat+half, lon+half],[lat-half, lon-half]]
    return [dl.Rectangle(bounds=bounds)]

@callback(
<<<<<<< Updated upstream
    Output("marker-layer", "children"),
    Input("input-center", "value"),
=======
    Output("map-layer", "children"),
    Input("input-address", "value"),
>>>>>>> Stashed changes
    Input("input-diagonal", "value"),
)
def update_map(center_adr, diag_val):
    if not diag_val or not center_adr:
        return no_update

    center_val = getCoordinates(center_adr)
    
    if center_val is None:
        return no_update

    markers = update_markers(5) 
    rectangle = update_rectangle(center=center_val, diagonal=diag_val)

    return markers + rectangle