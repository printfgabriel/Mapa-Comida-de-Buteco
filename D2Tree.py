from bar import Bar
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
        
        
    def build_tree(self, depth, bars):
        #caso a lista esteja vazia
        if not bars:
            return None
        
        #determina qual eixo vamos calcular a mediana
        #profundidades pares -> mediana da latitude, profundidades ímpares-> mediana da longitude
        axis = depth % 2
        
        ordered_bars = []
        if(axis == 0):
            ordered_bars = sorted(bars, key = lambda b: b.latitude)
        else:
            ordered_bars = sorted(bars, key = lambda b: b.longitude)
        
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
            
            node.left_son = self.build_tree(depth+1, ordered_bars[0:middle])
            node.right_son = self.build_tree(depth+1, ordered_bars[middle:])
            
        return node 
    

    def range_search(self, node: Tree_node, lat_min, lat_max, long_min, long_max, depth):
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
                result_bars.extend(self.range_search(node.left_son, lat_min, lat_max, long_min, long_max, depth+1))
            if lat_max >= c and node.right_son:
                result_bars.extend(self.range_search(node.right_son, lat_min, lat_max, long_min, long_max, depth+1))

        else:  #longitude
            if long_min <= c and node.left_son:
                result_bars.extend(self.range_search(node.left_son, lat_min, lat_max, long_min, long_max, depth+1))
            if long_max >= c and node.right_son:
                result_bars.extend(self.range_search(node.right_son, lat_min, lat_max, long_min, long_max, depth+1))

        return result_bars
    
    
    
    
    
    
        
    # def bar_label(self, bar):
    #     nome = getattr(bar, "name", getattr(bar, "nome", "sem_nome"))
    #     lat = getattr(bar, "latitude", "?")
    #     lon = getattr(bar, "longitude", "?")
    #     return f"{nome} (lat={lat}, lon={lon})"


    # def print_tree(self):
    #     if self.root is None:
    #         print("Árvore vazia")
    #         return

    #     self._print_node(self.root, depth=0, side="ROOT")


    # def _print_node(self, node, depth, side):
    #     indent = "    " * depth

    #     if node is None:
    #         print(f"{indent}{side}: None")
    #         return

    #     eixo = "latitude" if depth % 2 == 0 else "longitude"

    #     if node.bar is not None:
    #         print(f"{indent}{side}: FOLHA -> {self.bar_label(node.bar)}")
    #     else:
    #         print(f"{indent}{side}: NÓ INTERNO | eixo={eixo} | mediana={node.value}")
    #         self._print_node(node.left_son, depth + 1, "L")
    #         self._print_node(node.right_son, depth + 1, "R")


    # def validate_tree(self):
    #     folhas = []
    #     erros = []

    #     def walk(node, depth):
    #         if node is None:
    #             return

    #         eh_folha = node.left_son is None and node.right_son is None

    #         if eh_folha:
    #             if node.bar is None:
    #                 erros.append(f"Erro: folha no nível {depth} não guarda Bar.")
    #             else:
    #                 folhas.append(node.bar)
    #         else:
    #             if node.bar is not None:
    #                 erros.append(f"Erro: nó interno no nível {depth} guarda Bar.")
    #             if node.value is None:
    #                 erros.append(f"Erro: nó interno no nível {depth} não tem mediana.")

    #             walk(node.left_son, depth + 1)
    #             walk(node.right_son, depth + 1)

    #     walk(self.root, 0)

    #     print("\nVALIDAÇÃO")
    #     print(f"Total de bares originais: {len(self.bars)}")
    #     print(f"Total de folhas com Bar: {len(folhas)}")

    #     ids_originais = set(id(bar) for bar in self.bars)
    #     ids_folhas = set(id(bar) for bar in folhas)

    #     if ids_originais != ids_folhas:
    #         erros.append("Erro: nem todos os bares originais aparecem nas folhas, ou há bares extras.")

    #     if erros:
    #         print("Resultado: ERRO")
    #         for erro in erros:
    #             print("-", erro)
    #     else:
    #         print("Resultado: OK — nós internos guardam medianas e folhas guardam objetos Bar.")      