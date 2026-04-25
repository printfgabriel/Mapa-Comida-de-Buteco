import dash
from dash import html, dcc
import dash_leaflet as dl

app = dash.Dash(__name__)
icon = dict(html="<div><span> 10 </span></div>", className="marker-cluster marker-cluster-small", iconSize=[40, 40])

app.layout = html.Div([
    html.Div([html.H1("Mapa Comida de Buteco")], className="header"),
    html.Div([
        html.Div([
            dl.Map(
                [
                    dl.TileLayer(),
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
                    type="text",
                    placeholder="Digite a diagonal do retângulo",
                    className="text-input"
                ),

                html.H2("Resultados"),

                html.Div(id="table-container", className="table-container")

            ], className="right-panel")
        ])
    ], className="content")

    
    ], className="main-container")


dl.Map(
    [dl.TileLayer(), dl.DivMarker(position=[-19.9167, -43.9345], iconOptions=icon)],
    center=[-19.9167, -43.9345],
    zoom=11,
    style={"height": "50vh", "width": "80vh"},
   
)

# app.layout  = html.Div([
#     dl.Map(center=[-23, -46], zoom=8, style={'width': '100%', 'height': '500px'}, children=[
#         dl.TileLayer(),
#         dl.LayerGroup(id="marker-layer")
#     ]),
#     dcc.Input(id="input-center", value="", type="text", debounce=True),
#     dcc.Input(id="input-diagonal", value="", type="number"),
# ])


# ESSE IMPORT  TEM Q FICAR AQUI MESMO, DPS DA CRIAÇÃO DO APP
import callbacks 


if __name__ == "__main__":
    app.run(debug=True)
def main():
    print("Hello from mapa-comida-de-buteco!")


if __name__ == "__main__":
    main()
