def find_circular_dependencies(target, dependencies, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(target)
    path.append(target)

    for dep in dependencies.get(target, []):
        if dep in path:
            print(f"Circular dependency found:{' -> '.join(path+[dep])}")
        if dep not in visited:
            find_circular_dependencies(dep, dependencies, visited, path)

    path.pop()

def parse_makefile(makefile_path):
    dependencies = {}
    with open(makefile_path, 'r') as file:
        for line in file:
            if line.startswith('\t'):
                continue
            parts = line.strip().split(':')
            if len(parts) >= 2:
                target = parts[0].strip()
                deps = [dep.strip() for dep in parts[1].split()]
                dependencies[target] = deps
    return dependencies

def main():
    makefile_path = 'Makefile'
    dependencies = parse_makefile(makefile_path)
    for target in dependencies:
        find_circular_dependencies(target, dependencies)

if __name__ == "__main__":
    main()
    

