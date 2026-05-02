import math
from dash import callback, Output, Input, no_update, dash_table
import dash_leaflet as dl
from mapAPI import getCoordinates
from tree_instance import tree
from bar import Bar

def update_markers(bars:list[Bar]):
    markers = []
    for bar in bars:
        lat = bar.latitude
        lon = bar.longitude
        markers.append(
            dl.Marker(
                position=[lat, lon],
                # children=dl.Tooltip(f"Marker {i+1}"),
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

def update_rectangle(center, delta_lat, delta_long):
    lat, lon = center
    bounds = [[lat+delta_lat, lon+delta_long],[lat-delta_lat, lon-delta_long]]
    return [dl.Rectangle(bounds=bounds)]


def update_circle(center, radius = 1):
     return [
        dl.Circle(
            center=center,
            radius=radius * 1000
        )
    ]
    
# Fórmula de Haversine
def calculate_distance(lat_center, long_center, lat_bar, long_bar):
    R = 6371.0  # Raio médio da Terra 

    phi1, phi2 = math.radians(lat_center), math.radians(lat_bar)
    dphi = math.radians(lat_bar - lat_center)
    dlambda = math.radians(long_bar - long_center)

    a = math.sin(dphi / 2)**2 + \
        math.cos(phi1) * math.cos(phi2) * \
        math.sin(dlambda / 2)**2
        
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c

@callback(
    [Output("map-layer", "children"),
    Output("bar-table", "data")],
    Input("input-address", "value"),
    Input("input-range", "value"),
    Input("input-shape", "value")
)

def update_map(center_adr, search_range, shape):
    if not search_range or not center_adr:
        return no_update

    center_val = getCoordinates(center_adr)
    
    if center_val is None:
        return no_update

    lat, lon = center_val

    
    #caso formato seja retangulo usamos a função de busca adequada
    if shape == "retangulo": 
        # Transformando de KM para Latitude/Longitude
        delta_lat = search_range / (2*111.32 )
        delta_long = search_range / (2 *(111.32 * math.cos(math.radians(search_range))))
        
        bars_found = tree.range_search_rectangule(tree.root, lat-delta_lat, lat+delta_lat, lon-delta_long, lon+delta_long, 0)

        # Ordenando os bares pela distância
        bars_found.sort(key=lambda bar: calculate_distance(
            lat, lon, bar.latitude, bar.longitude
        ))

        markers = update_markers(bars_found) 
        rectangle = update_rectangle(center_val, delta_lat, delta_long)
        table_data = [
        {"name": b.name, "address": b.address, "distance": calculate_distance(lat, lon, b.latitude, b.longitude)} 
        for b in bars_found
    ]
        return [markers + rectangle, table_data]
    
    #caso seja círculo usamos a função de busca correspondente 
    elif shape == "circulo":
        bars_found = tree.range_search_circle(tree.root, search_range, lat, lon)

        # Ordenando os bares pela distância
        bars_found.sort(key=lambda bar: calculate_distance(
            lat, lon, bar.latitude, bar.longitude
        ))

        markers = update_markers(bars_found) 
        #atualizando o círculo 
        circle = update_circle(center=center_val, radius = search_range)
        table_data = [
        {"name": b.name, "address": b.address, "distance": calculate_distance(lat, lon, b.latitude, b.longitude)} 
        for b in bars_found
    ]
        return [markers + circle, table_data]
    else:
        return no_update

    

    
    