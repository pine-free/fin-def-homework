from typing import Generator
import networkx as nx

from src.models import Case


class FileGraph:
    def __init__(self) -> None:
        self.cases: list[Case] = []
        self._graph: nx.Graph[str] = nx.Graph()

    def add_case(self, case: Case) -> None:
        self.cases.append(case)
        self._graph.add_nodes_from([case.guilty, case.victim])
        self._graph.add_edge(case.guilty, case.victim)

    def add_cases(self, cases: list[Case]) -> None:
        for case in cases:
            self.add_case(case)
    
    @property
    def components(self) -> Generator[set[str]]:
        return nx.connected_components(self._graph)

    @property
    def components_count(self) -> int:
        return len(self.components)

    def draw(self) -> None:
        nx.draw(self._graph, with_labels=True)
