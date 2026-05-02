from bar import Bar
import math

# Calcula a distância em km entre dois pontos
def calculates_distance(latitude1, longitude1, latitude2, longitude2):
    #raio da terra em km
    earth_radius = 6371 
    
    #converte graus em radianos
    latitude1 = math.radians(latitude1)
    latitude2 = math.radians(latitude2)
    longitude1 = math.radians(longitude1)
    longitude2 = math.radians(longitude2)
    
    difference_latitudes = latitude2 - latitude1
    difference_longitudes = longitude2 - longitude1
    
    #usando formula de Haversine para calcular distância entre dois pontos com base em latitude e longitude
    sqr_expression = (
        math.sin(difference_latitudes / 2) ** 2 
        + math.cos(latitude1) * math.cos(latitude2) * math.sin(difference_longitudes / 2) ** 2
    )
    
    distance = 2 * earth_radius * math.asin(math.sqrt(sqr_expression))
    return distance
    
class Tree_node:
    def __init__(self, value= None, bar:Bar = None, left_node = None, right_node= None):
        self.value = value
        self.bar = bar
        self.left_son = left_node
        self.right_son = right_node

class D2_tree:
    def __init__(self, bars: list[Bar]):
        self.root = self.build_tree(0, bars)
        self.bars = bars
        
        
    def build_tree(self, depth, bars, bars_by_other_axis=None):
        #caso a lista esteja vazia
        if not bars:
            return None
        
        #determina qual eixo vamos calcular a mediana
        #profundidades pares -> mediana da latitude, profundidades ímpares-> mediana da longitude
        axis = depth % 2
        
        #ordenamos por latitude e longitude apenas na primeira chamada
        if bars_by_other_axis is None:
            bars = sorted(bars, key=lambda b: b.latitude)
            bars_by_other_axis = sorted(bars, key=lambda b: b.longitude)
    
        ordered_bars = bars
        other_ordered_bars = bars_by_other_axis
    

        #caso tenhamos chegado a um nó folha guardamos um objeto
        if(len(ordered_bars) == 1):
            node = Tree_node(bar =ordered_bars[0])
        else:
        #caso não seja um nó folha guardamos e mediana e calculamos recursivamente as subárvores a esquerda e direita
        
            middle = len(ordered_bars) // 2
            
            if(axis == 0):
               node = Tree_node(ordered_bars[middle].latitude)
            else:
               node = Tree_node(ordered_bars[middle].longitude)     
               
            #divide os bares em duas metades de acordo com mediana
            left_ordered_bars = ordered_bars[0:middle]
            right_ordered_bars = ordered_bars[middle:]
        
            
            #divide os bares no outro eixo também
            left_other_axis_ordered_bars = []
            right_other_axis_ordered_bars = []
            
            left_ids = set(id(bar) for bar in left_ordered_bars)
            
            for bar in other_ordered_bars:
                if id(bar) in left_ids:
                    left_other_axis_ordered_bars.append(bar)
                else:
                    right_other_axis_ordered_bars.append(bar)
                
            node.left_son = self.build_tree(depth + 1, left_other_axis_ordered_bars, left_ordered_bars)
            
            node.right_son = self.build_tree(depth + 1, right_other_axis_ordered_bars, right_ordered_bars)
            
        return node 
    

    def range_search_rectangule(self, node: Tree_node, lat_min, lat_max, long_min, long_max, depth):
        if not node:
            return []
        
        result_bars = []

        if not node.left_son and not node.right_son:
            if node.bar:
                bar = node.bar
                if long_min <= bar.longitude <= long_max and  lat_min <= bar.latitude <= lat_max:
                    return[bar]
                return []

        c = node.value
        axis = depth % 2 
        # par é latitude
        # impar é longitudo

        if axis==0: # latitude
            if lat_min <= c and node.left_son:
                result_bars.extend(self.range_search_rectangule(node.left_son, lat_min, lat_max, long_min, long_max, depth+1))
            if lat_max >= c and node.right_son:
                result_bars.extend(self.range_search_rectangule(node.right_son, lat_min, lat_max, long_min, long_max, depth+1))

        else:  #longitude
            if long_min <= c and node.left_son:
                result_bars.extend(self.range_search_rectangule(node.left_son, lat_min, lat_max, long_min, long_max, depth+1))
            if long_max >= c and node.right_son:
                result_bars.extend(self.range_search_rectangule(node.right_son, lat_min, lat_max, long_min, long_max, depth+1))

        return result_bars
    

    def range_search_circle(self, node: Tree_node, radius, center_latitude, center_longitude, depth = 0):
        if not node: 
            return []
        
        axis = depth % 2
        results = [] 
        
        #raio em km convertido para graus
        delta_latitude = radius / 111
        latitude_radians = math.radians(center_latitude)
        delta_longitude = radius / (111 * math.cos(latitude_radians))
        
        #caso sejá nó folha verificamos se o bar está dentro do círculo 
        if node.bar is not None:
            #considerando tolerância de 50 metros 
            tolerance = 0.05
            if calculates_distance(center_latitude, center_longitude, node.bar.latitude, node.bar.longitude) <= radius + tolerance:
                results.append(node.bar)
            return results 
                
        #chamamos a função recursivamente considerando latitude caso profundidade seja par
        if(axis == 0):
            if center_latitude - delta_latitude <= node.value:
                results += self.range_search_circle(node.left_son, radius, center_latitude, center_longitude, depth+1)
            if center_latitude + delta_latitude >= node.value:
                results += self.range_search_circle(node.right_son, radius, center_latitude, center_longitude, depth+1)
        else: 
            #considerando longitude caso profundidade seja ímpar 
            if center_longitude - delta_longitude <= node.value:
                results += self.range_search_circle(node.left_son, radius, center_latitude, center_longitude, depth+1)
            if center_longitude + delta_longitude >= node.value:
                results += self.range_search_circle(node.right_son, radius, center_latitude, center_longitude, depth+1)
                
        return results  
    
