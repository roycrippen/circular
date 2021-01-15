import sys

from entities import Entities

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Application requires <file> argument and optional <package list> arguments.')
        exit(-1)

    args = sys.argv[1:]
    file_name = args[0]
    packages = args[1:]

    print(f'    Target file: {file_name}')
    print(f'Target packages: {packages}\n')
    if len(packages) == 0:
        packages = None
    entities = Entities(file_name, packages=packages)
    entities.print_deps()
    entities.find_circular_deps(level=5)
    entities.print_circular_deps()
