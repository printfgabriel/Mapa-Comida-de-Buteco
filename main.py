import dash
from dash import html, dcc
import dash_leaflet as dl

app = dash.Dash(__name__)

app.layout = html.Div([
    dl.Map(center=[-23, -46], zoom=8, style={'width': '100%', 'height': '500px'}, children=[
        dl.TileLayer(),
        dl.LayerGroup(id="marker-layer")
    ]),
    dcc.Input(id="input-center", value="", type="text", debounce=True),
    dcc.Input(id="input-diagonal", value="", type="number"),
])


# ESSE IMPORT  TEM Q FICAR AQUI MESMO, DPS DA CRIAÇÃO DO APP
import callbacks 


if __name__ == "__main__":
    app.run(debug=True)