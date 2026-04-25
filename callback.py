import dash
from dash import html, dcc, Output, Input
import dash_leaflet as dl
import random
from mapAPI import getCoordinates

app = dash.Dash(__name__)

# Essa função aq gera market aleatório, só pra testar.
# Em breve vai ser a lista q retorna da busca na árvore
def update_markers(n=5):
    markers = []
    for i in range(n):
        lat = -23 + random.uniform(-0.5, 0.5)  # Random latitude
        lon = -46 + random.uniform(-0.5, 0.5)  # Random longitude
        color = random.choice(["red", "blue", "green", "orange", "purple"])
        markers.append(
            dl.Marker(
                position=[lat, lon],
                children=dl.Tooltip(f"Marker {i+1}"),
                icon={
                    "iconUrl": f"https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-{color}.png",
                    "iconSize": [25, 41],
                    "iconAnchor": [12, 41],
                    "popupAnchor": [1, -34],
                    "shadowUrl": "https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png",
                    "shadowSize": [41, 41]
                }
            )
        )
    return markers
    # TROCAR PELA LÓGICA

def update_rectangle(center=(-23.0,-46.0), diagonal=1):
    half = diagonal/2
    (lat,lon) = center

    bounds = [[lat+half, lon+half],[lat-half, lon-half]]

    return [dl.Rectangle(bounds=bounds)]


# app.layout = html.Div([
#     dl.Map(center=[-23, -46], zoom=8, style={'width': '100%', 'height': '500px'}, children=[
#         dl.TileLayer(),
#         dl.LayerGroup(id="marker-layer")
#     ]),
#     dcc.Input(id="input-center", value="", type="text", debounce=True),
#     dcc.Input(id="input-diagonal", value="", type="number"),
# ])



@app.callback(
    Output("marker-layer", "children"),
    Input("input-address", "value"),
    Input("input-diagonal", "value"),
)

def update_map(center_adr, diag_val):
    if not diag_val or not center_adr:
        return dash.no_update
    print(0)

    # center_val = getCoordinates(center_adr)

    # if center_val is None:
    #     print("Error: corrdinates = None\n")
    #     return dash.no_update

    # print(center_val)

    markers =  update_markers(5) 
    print(1)

    # sem o centro pq to resolvendo ainda center=center_val,
    rectangle = update_rectangle(diagonal=diag_val)
    # print(center_val)

    return markers + rectangle
    

if __name__ == "__main__":
    app.run(debug=True)
 











