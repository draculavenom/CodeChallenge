server_network = {
    1: [(2, 100), (3, 50)],
    2: [(1, 100), (4, 80)],
    3: [(1, 50),  (4, 70)],
    4: [(2, 80),  (3, 70)]
}

def find_max_throughput_path(graph, source_server, target_server):
    ans = -1, []

    speeds = {}#definition of the speeds at 0, that way the newest speed will update it if it's higher, which will happens always the first time
    for g in graph:
        speeds[g] = 0
    
    queue = [(source_server, float('inf'))]
    speeds[source_server] = float('inf')
    parents = {}
    for n in graph:
        parents[n] = None

    while queue:
        node, speed = retrieve_fastest_element(queue)
        queue.remove((node, speed))

        if node == target_server:
            path = []
            trace_node = target_server
            
            while trace_node is not None:
                path.append(trace_node)
                trace_node = parents[trace_node]
            
            path.reverse()
            return speed, path
        
        if speed < speeds[node]:
            continue

        for server, server_speed in graph[node]:
            path_bottleneck = min(speed, server_speed)
            if path_bottleneck > speeds[server]:
                speeds[server] = path_bottleneck
                queue.append((server, path_bottleneck))
                parents[server] = node
        

    return ans

def retrieve_fastest_element(queue):
    ans = (0, 0)
    for q in queue:
        if ans[1] < q[1]:
            ans = q
    return ans

print(find_max_throughput_path(server_network, 3, 2))