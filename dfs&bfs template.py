# dfs with recursion
def dfs(node, visited):
    if node in visited:
        return
    
    visited.add(node)

    for n in node.children:
        if n not in visited:
            dfs(n, visited)

# dfs with stack
def dfs(root):
    stack = [root]
    while stack:
        cur = stack.pop()
        process(cur)

        for c in cur.children:
            stack.push(c)
    
# bfs with queue
def bfs(root):
    queue = [root]

    while queue:
        cur = queue.pop(0)
        process(cur)

        for c in cur.children:
            queue.append(c)