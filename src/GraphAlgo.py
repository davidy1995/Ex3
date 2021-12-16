import json
import sys
from GraphAlgoInterface import GraphAlgoInterface
from typing import List
from src.Node import Node
from src import GraphInterface
from src.Edge import Edge
from src.Location import Location



class GraphAlgo(GraphAlgoInterface):

    def __init__(self,src,weight,dest,id,location):
        self.src = src
        self.weight = weight
        self.dest =dest
        self.id=id
        self.location=location


    def getGraph(self, g):
        pass

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open("A0.json", 'r') as f:
                edgesArr = []
                nodesArr = []
                data = json.load(f)
                self.src = data["src"]
                self.weight = data["w"]
                self.dest = data["dest"]
                self.pos = data["pos"]
                self.id = data["id"]
                arrN = data["Nodes"]
                arrE = data["Edges"]
                for line in arrE:
                    ed = Edge(line["src"], line["w"], line["dest"])
                    edgesArr.append(ed)
                for line1 in arrN:
                    no = Node(line1["id"],line1["pos"])
                    nodesArr.append(no)

        except ValueError as e:
            return False
        return True

    def save_to_json(self, file_name: str) -> bool:
        try:
            with open("info_.json", "a") as data:
                edgesArr = {Edge: {'src': self.src, 'w': self.weight,'dest' : self.dest}}
                nodesArr = {Node:{'pos' : self.location, 'id' : self.id}}
                data.write(json.dumps(edgesArr,nodesArr))
                data.close()

        except ValueError as e:
            return False
        return True

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def plot_graph(self) -> None:
        pass




