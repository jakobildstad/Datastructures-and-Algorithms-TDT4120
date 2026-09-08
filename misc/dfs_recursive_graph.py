def dfs(root, visited):
    for neighbr in get_neighbors(root): # type: ignore
        if neighbr in visited:
            continue
        visited.add(neighbr)
        dfs(neighbr, visited)