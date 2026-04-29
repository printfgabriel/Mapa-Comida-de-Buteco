from bar import Bar
import csv
from D2Tree import D2_tree

def load_bars_from_csv():

    with open('data/butecos_com_coords.csv', mode='r', encoding='utf-8', newline='') as csv_file:
        
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        
        bars = []
        for row in csv_reader:
            latitude, longitude = row['latitude'], row['longitude']
            
            if latitude and longitude:
                new_bar = Bar(name=row['name'], address=row['address'], latitude=float(latitude), longitude=float(longitude))
                bars.append(new_bar)
            else:
                print(f"Bar {row['name']} com problemas, foi ignorado!")
        
    return bars




bars = load_bars_from_csv()
print("Fim da criação do CSV\n\n")

tree = D2_tree(bars)