# ESSE ARQUIVO NÃO ESTÁ SENDDO UTILIZADO NO MOMENTO
# SUA UTILIDADE É MOSTRAR ARQUIVOS QUE FORAM TRANSFORMADOS AO LONGO DO CÓDIGO
# VISTO QUE USAMOS ESSES ARQUIVOS NO APLICATIVO CRIADO


# TEM Q DAR pip install geopandas
import geopandas as gpd
import requests
import zipfile
import io

url = "https://geoservicos.pbh.gov.br/geoserver/wfs?service=WFS&version=1.0.0&request=GetFeature&typeName=ide_bhgeo:BAIRRO_OFICIAL&srsName=EPSG:31983&outputFormat=SHAPE-ZIP"
headers = {
    'User-Agent': 'Mozilla/5.0'
}

response = requests.get(url, headers=headers)

if response.content[:2] != b'PK':
    print(response.text)
else:
    z = zipfile.ZipFile(io.BytesIO(response.content))
    z.extractall('./data')
    
    gdf = gpd.read_file('./data/BAIRRO_OFICIAL.shp')
    gdf = gdf.to_crs(epsg=4326)
    gdf.to_file('./data/bairros_bh.geojson', driver='GeoJSON')
    
    print("Convertido!")