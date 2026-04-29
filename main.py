import dash
from dash import html, dcc, dash_table
import dash_leaflet as dl
import csv
from mapAPI import getCoordinates
import time
from D2Tree import D2_tree
from tree_instance import tree
import json


app = dash.Dash(__name__)

icon = dict(html="<div><span> 10 </span></div>", className="marker-cluster marker-cluster-small", iconSize=[40, 40])

with open("data/bairros_bh.geojson", "r", encoding="utf-8") as f:
    geojson_data = json.load(f)

app.layout = html.Div([
    html.Div([html.H1("Mapa Comida de Buteco")], className="header"),
    html.Div([
        html.Div([
            dl.Map(
                [
                    dl.TileLayer(),
                    dl.GeoJSON(
                        data=geojson_data,
                        id="bairros-layer",
                        options={"style": {"color": "blue", "weight": 1, "fillOpacity": 0.1}}, # Estética
                        hoverStyle={"fillOpacity": 0.3, "color": "red"} # Efeito ao passar o mouse
                    ),
                    dl.LayerGroup(id="map-layer"),
                    dl.DivMarker(
                        position=[-19.9167, -43.9345],
                        iconOptions=icon
                    )
                ],
                center=[-19.928056, -43.941944],
                zoom=13.5,
                style={
                    "height": "90vh"
                }
            )], className="map-area"),
        html.Div([
            html.Div([
                dcc.RadioItems(
                id="input-shape",
                options=[
                    {"label": "Retângulo", "value": "retangulo"},
                    {"label": "Círculo", "value": "circulo"},
                ],
                value="retangulo",
                className="radio-input"
                ),
                dcc.Input(
                    id="input-address",
                    type="text",
                    placeholder="Digite o endereço",
                    className="text-input"
                ),

                dcc.Input(
                    id="input-range",
                    type="number",
                    placeholder="Digite a diagonal do retângulo",
                    className="text-input"
                ),

                html.H2("Resultados"),

                dash_table.DataTable(
                    id="bar-table",
                    columns=[
                        {"name": "Nome", "id": "name"},
                        {"name": "Endereço", "id": "address"},
                        {"name": "Latitude", "id": "latitude"},
                        {"name": "Longitude", "id":"longitude"}
                    ],
                    data=[], 
                    page_size=20,
                    style_table={'overflowX': 'auto'}
                )
                # html.Div(id="table-container", className="table-container")

            ], className="right-panel")
        ])
    ], className="content")

    
    ], className="main-container")

# ESSE IMPORT  TEM Q FICAR AQUI MESMO, DPS DA CRIAÇÃO DO APP
import callbacks 

def main():
    print("Hello")
    print(f"Árvore carregada com {len(tree.bars)} bares.")


if __name__ == "__main__":
    main()

    app.run(debug=True)


# def load_bars_from_csv(file_path):

#     with open(file_path, mode='r', encoding='utf-8') as csv_file, \
#          open('data/butecos_com_coords.csv', mode='w', encoding='utf-8', newline='') as out_file:
        
#         csv_reader = csv.DictReader(csv_file, delimiter=';')
#         writer = csv.writer(out_file, delimiter=';')
#         writer.writerow(['name', 'latitude', 'longitude'])
        
#         bars = []
#         for row in csv_reader:
#             time.sleep(1)
#             print(row['name'])
            
#             coordinate = getCoordinates(row['address'].replace(",", " "))
            
#             latitude, longitude = "", ""
            
#             if coordinate:
#                 latitude, longitude = coordinate
#                 new_bar = Bar(name=row['name'], address=row['address'], latitude=latitude, longitude=longitude)
#                 bars.append(new_bar)
#             else:
#                 print(f"Erro na API ao ler csv, bar: {row['name']}")

#             writer.writerow([row['name'], latitude, longitude])
        
#     return bars