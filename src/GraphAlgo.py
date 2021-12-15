import json
import sys
from GraphAlgoInterface import GraphAlgoInterface
from typing import List
from src.Node import Node
from src import GraphInterface
from src.Edge import Edge


class GraphAlgo(GraphAlgoInterface):

    def getGraph(self, g):
        pass

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open("A0.json", 'r') as f:
                edgesArr = []
                data = json.load(f)
                src = data["src"]
                weight = data["w"]
                dst = data["dest"]

                arrE = data["Edges"]
                for line in arrE:
                    el = Edge(line["src"], line["w"], line["dest"])
                    edgesArr.append(el)
                    return True

        except IOError as error:
            print('No file : %s' %(file_name))
            return False
        try:
            nodesArr = []
            data = json.load(f)
            pos = data["pos"]
            id = data["id"]
            arrN = data["Nodes"]
            for line in arrN:

                el = Node(line["pos"], line["id"])
                nodesArr.append(el)
                return True
        except IOError as error:
            print('No file : %s' %(file_name))
            return False

    def save_to_json(self, file_name: str) -> bool:
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def plot_graph(self) -> None:
        pass




#
# data = json.load(open("A0.json"))
# print(type(data['Edges']))
# print(data)