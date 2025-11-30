import logging
import sys

from src.cli import Cli
from src.data_importer import CaseImporter

def main() -> None:
    logging.basicConfig()

    importer = CaseImporter()
    cli = Cli(importer)
    cli.do_import(sys.argv[1])
    cli.cmdloop()


if __name__ == "__main__":
    main()
