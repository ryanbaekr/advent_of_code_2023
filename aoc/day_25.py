"""Processing for Day 25"""

def snowverload(diagram: str) -> int:
    """Take the diagram and return the appropriate value"""

    graph: dict[str, list[str]] = {}

    for connection in diagram.splitlines():
        input_node, output_nodes_str = connection.split(": ")
        output_nodes = output_nodes_str.split(" ")
        try:
            graph[input_node].extend(output_nodes)
        except KeyError:
            graph[input_node] = output_nodes
        for output_node in output_nodes:
            try:
                graph[output_node].append(input_node)
            except:
                graph[output_node] = [input_node]

    temp = _brandes(graph)

    bounding_nodes: list[str] = []

    for key, val in temp.items():
        if val > 300000:
            bounding_nodes.append(key)

    visited = [key]
    queue = [key]

    while queue:
        next_queue = []

        for v in queue:
            for w in graph[v]:
                if w in bounding_nodes:
                    if w not in visited:
                        visited.append(w)
                    continue
                if w not in visited:
                    visited.append(w)
                    next_queue.append(w)

        queue = next_queue

    return len(visited) * (len(graph.keys()) - len(visited))


def _brandes(graph: dict[str, list[str]]) -> dict[str, float]:
    betweenness = {key: 0.0 for key in graph}

    for s in graph:
        stack = []
        pred: dict[str, list[str]] = {key: [] for key in graph}
        dist = {key: -1 for key in graph}
        dist[s] = 0
        sigma = {key: 0 for key in graph}
        sigma[s] = 1
        queue = [s]

        while queue:
            v = queue[0]
            queue = queue[1:]
            stack.append(v)
            for w in graph[v]:
                if dist[w] < 0:
                    queue.append(w)
                    dist[w] = dist[v] + 1
                if dist[w] == dist[v] + 1:
                    sigma[w] += sigma[v]
                    pred[w].append(v)

        delta = {key: 0.0 for key in graph}
        while stack:
            w = stack.pop()
            for v in pred[w]:
                delta[v] += (sigma[v] / sigma[w]) * (1 + delta[w])
            if w != s:
                betweenness[w] += delta[w]

    return betweenness
