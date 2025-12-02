from typing import Generator
import networkx as nx
import matplotlib.pyplot as plt

from src.models import Case


class FileGraph:
    def __init__(self, edge_len: int = 1, graph_cls = nx.Graph) -> None:
        self.cases: list[Case] = []
        self._graph: nx.Graph[str] = graph_cls()
        self.edge_len = edge_len

    def add_case(self, case: Case) -> None:
        self.cases.append(case)
        self._graph.add_nodes_from([case.guilty_initials, case.victim_initials])
        self._graph.add_edge(case.guilty_initials, case.victim_initials , length=self.edge_len)

    def add_cases(self, cases: list[Case]) -> None:
        for case in cases:
            self.add_case(case)
    
    @property
    def components(self) -> Generator[set[str]]:
        return nx.connected_components(self._graph)

    @property
    def components_count(self) -> int:
        return len(self.components)

    def draw(self, *args, **kwargs) -> None:
        nx.draw(self._graph, *args, with_labels=True, **kwargs)
