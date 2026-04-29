import random
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

def update_rectangle(center=(-23.0,-46.0), diagonal=1):
    half = diagonal/2
    lat, lon = center
    bounds = [[lat+half, lon+half],[lat-half, lon-half]]
    return [dl.Rectangle(bounds=bounds)]

def update_circle(center=(-23.0,-46.0), radius = 1):
     return [
        dl.Circle(
            center=center,
            radius=radius * 1000
        )
    ]
    

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
        half_diag = search_range/2
        bars_found = tree.range_search_rectangule(tree.root, lat-half_diag, lat+half_diag, lon-half_diag, lon+half_diag, 0)
        markers = update_markers(bars_found) 
        rectangle = update_rectangle(center=center_val, diagonal=search_range)
        table_data = [
        {"name": b.name, "address": b.address, "latitude": b.latitude, "longitude": b.longitude} 
        for b in bars_found
    ]
        return [markers + rectangle, table_data]
    elif shape == "circulo":
        #caso seja círculo usamos a função de busca correspondente 
        bars_found = tree.range_search_circle(tree.root, search_range, lat, lon)
        markers = update_markers(bars_found) 
        #atualizando o círculo 
        circle = update_circle(center=center_val, radius = search_range)
        table_data = [
        {"name": b.name, "address": b.address, "latitude": b.latitude, "longitude": b.longitude} 
        for b in bars_found
    ]
        return [markers + circle, table_data]
    else:
        return no_update

    

    
    