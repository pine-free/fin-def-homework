import logging
import cmd
from typing import Callable

from .models import Case
from .data_importer import CaseImporter
from .file_graph import FileGraph

logger = logging.getLogger(__name__)


class Cli(cmd.Cmd):
    def __init__(self, importer: CaseImporter) -> None:
        super().__init__()
        self.cases: list[Case]= []
        self.importer = importer

        self._basic_graph = FileGraph()

    @property
    def get_show_method_map(self) -> dict[str, Callable[[], None]]:
        return {"basic": self._show_basic}

    def do_import(self, filepath: str) -> None:
        self.cases = self.importer.import_cases(filepath)
        self._basic_graph.add_cases(self.cases)

    def _show_basic(self) -> None:
        self._basic_graph.draw()

    def do_show(self, g_type: str) -> None:
        mmap = self.get_show_method_map
        if g_type in mmap:
            mmap[g_type]()
        else:
            logger.error("Error: wrong arg to show")
            logger.error(f"try one of: {','.join(mmap.keys())}")

    def do_q(self, arg: str) -> None:
        exit(0)
