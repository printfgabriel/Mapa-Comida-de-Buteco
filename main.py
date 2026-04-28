import dash
from dash import html, dcc
import dash_leaflet as dl
import csv
from bar import Bar
from mapAPI import getCoordinates
import time
from D2Tree import D2_tree
app = dash.Dash(__name__)
icon = dict(html="<div><span> 10 </span></div>", className="marker-cluster marker-cluster-small", iconSize=[40, 40])

app.layout = html.Div([
    html.Div([html.H1("Mapa Comida de Buteco")], className="header"),
    html.Div([
        html.Div([
            dl.Map(
                [
                    dl.TileLayer(),
                    dl.LayerGroup(id="map-layer"),
                    dl.DivMarker(
                        position=[-19.9167, -43.9345],
                        iconOptions=icon
                    )
                ],
                center=[-19.9167, -43.9345],
                zoom=12,
                style={
                    "height": "90vh"
                }
            )], className="map-area"),
        html.Div([
            html.Div([

                dcc.Input(
                    id="input-address",
                    type="text",
                    placeholder="Digite o endereço",
                    className="text-input"
                ),

                dcc.Input(
                    id="input-diagonal",
                    type="number",
                    placeholder="Digite a diagonal do retângulo",
                    className="text-input"
                ),

                html.H2("Resultados"),

                html.Div(id="table-container", className="table-container")

            ], className="right-panel")
        ])
    ], className="content")

    
    ], className="main-container")

# ESSE IMPORT  TEM Q FICAR AQUI MESMO, DPS DA CRIAÇÃO DO APP
import callbacks 


#Lê arquivo csv e retorna conteúdo
#pensei agora vamo deixar os comentários em português mesmo? 
def load_bars_from_csv(file_path):

    with open('data/butecos_com_coords.csv', mode='w', encoding='utf-8', newline='') as csv_file:
        
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        
        bars = []
        for row in csv_reader:
            latitude, longitude = row['latitude'], row['longitude']
            
            if latitude and longitude:
                new_bar = Bar(name=row['name'], address=row['address'], latitude=latitude, longitude=longitude)
                bars.append(new_bar)
            else:
                print(f"Bar {row['name']} com problemas, foi ignorado!")
        
    return bars
    


def main():
    print("Hello from mapa-comida-de-buteco!")
    bars = load_bars_from_csv('data/butecos_bh.csv')
    print("Fim da criação do CSV\n\n")
    
    tree = D2_tree(bars)

    # tree.print_tree()
    # tree.validate_tree()

if __name__ == "__main__":
    #app.run(debug=True)
    main()


    

# app.layout  = html.Div([
#     dl.Map(center=[-23, -46], zoom=8, style={'width': '100%', 'height': '500px'}, children=[
#         dl.TileLayer(),
#         dl.LayerGroup(id="marker-layer")
#     ]),
#     dcc.Input(id="input-center", value="", type="text", debounce=True),
#     dcc.Input(id="input-diagonal", value="", type="number"),
# ])

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