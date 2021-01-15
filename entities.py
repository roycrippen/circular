from collections import OrderedDict
from typing import Dict, Set, List


class Entities:
    """Class of java object entity dependencies"""

    def __init__(self, file_path: str, packages=None):
        if packages is None:
            packages = []
        self.deps: Dict[str, Set[str]] = {}
        self.circular_deps: List[str] = []
        self.read_dep_file(file_path, packages)

    def read_dep_file(self, file_name: str, packages=None):
        excludes = ['java.', 'javax.', 'sun.', 'jdk.', 'com.sun']
        if packages is None:
            packages = []
        with open(file_name) as fp:
            for line in fp:
                if line[0] != " ":
                    continue

                line = line.lstrip()
                if any(line.startswith(exclude) for exclude in excludes):
                    continue

                if len(packages) > 0:
                    for package in packages:
                        if line.lstrip().startswith(package):
                            self.__parse_line(line, excludes)
                else:
                    self.__parse_line(line, excludes)

    def find_circular_deps(self, level: int = 1):
        if level < 1 or level > 5:
            print('Error level must be between 1 and 5')
            return

        xss = []
        for target_k in self.deps.keys():
            xss += self.__update_circular_deps(target_k, level)

        xss = [xs for xs in xss if not any(xs.count(x) > 1 for x in xs)]
        xss = [sorted(xs) for xs in xss if len(xs) > 1]
        xss = [xs + [xs[0]] for xs in xss]
        xss = [" -> ".join(xs) for xs in xss]
        self.circular_deps = list(OrderedDict.fromkeys(xss))
        pass

    def __update_circular_deps(self, target_k: str, level: int) -> List[List[str]]:
        def go(candidate_list, k, lev):
            if k not in self.deps:
                return []

            result_lists = []
            for dep in self.deps[k]:
                if dep in self.deps and target_k in self.deps[dep]:
                    result_lists.append(candidate_list + [dep])
                    continue
                if lev - 1 > 0:
                    result_lists += go(candidate_list + [dep], dep, lev - 1)
            return result_lists

        return go([target_k], target_k, level)

    def __parse_line(self, line: str, excludes: List[str]):
        xs = " ".join(line.split()).split(' ')
        if len(xs) < 3:
            print(f'Error parsing line: {line}')
            return
        k = xs[0]
        v = xs[2]

        if any(v.startswith(exclude) for exclude in excludes):
            return

        if k in self.deps:
            self.deps.get(k).add(v)
        else:
            self.deps[k] = {v}

    def print_deps(self):
        import pprint
        pp = pprint.PrettyPrinter(indent=4, width=300)
        print('Dependencies')
        pp.pprint(self.deps)
        print('\n')

    def print_circular_deps(self):
        import pprint
        pp = pprint.PrettyPrinter(indent=4, width=300)
        print('Circular Dependencies')
        pp.pprint(self.circular_deps)
        print('\n')
