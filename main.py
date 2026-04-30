import dash
from dash import html, dcc, dash_table
import dash_leaflet as dl
from tree_instance import tree
import json


app = dash.Dash(__name__)



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
                        options={
                            "style": {
                                "color": "blue", 
                                "weight": 1, 
                                "fillOpacity": 0.01
                                }
                            }, 
                        hoverStyle={"fillOpacity": 0.3, "color": "blue"} 
                    ),
                    dl.LayerGroup(id="map-layer"),
                    
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
                    placeholder="Digite a diagonal ou raio",
                    className="text-input"
                ),

                html.H2("Resultados"),

                dash_table.DataTable(
                    id="bar-table",
                    columns=[
                        {"name": "Nome", "id": "name"},
                        {"name": "Distância", "id": "distance"},
                        {"name": "Endereço", "id": "address"},
                    ],
                    data=[], 
                    page_size=20,
                    style_table={'overflowX': 'auto'}
                )

            ], className="right-panel")
        ])
    ], className="content")

    
    ], className="main-container")


import callbacks 

def main():
    print("Hello")
    print(f"Árvore carregada com {len(tree.bars)} bares.")


if __name__ == "__main__":
    main()
    app.run(debug=True)


