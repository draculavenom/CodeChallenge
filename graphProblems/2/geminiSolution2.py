import heapq

delivery_map = {
    1: [(2, 10), (3, 5)],
    2: [(1, 10), (4, 2)],
    3: [(1, 5),  (4, 1)],
    4: [(2, 2),  (3, 1)]
}

complex_map = {
    1: [(2, 4), (4, 2)],
    2: [(1, 4), (3, 8), (5, 2)],
    3: [(2, 8), (6, 3)],
    4: [(1, 2), (5, 1), (7, 10)],
    5: [(2, 2), (4, 1), (6, 5), (8, 2)],
    6: [(3, 3), (5, 5), (9, 1)],
    7: [(4, 10), (8, 6)],
    8: [(5, 2), (7, 6), (9, 1)],
    9: [(6, 1), (8, 1)],
    10: [(11, 5)],
    11: [(10, 5)]
}

def find_fastest_route_with_path(graph, start_hub, destination_hub):
    shortest_times = {node: float('inf') for node in graph}
    shortest_times[start_hub] = 0
    
    # NEW: Master tracker for reconstruction map -> {child: parent}
    # This tells us exactly which node got us to the current node the fastest
    parents = {node: None for node in graph}

    priority_queue = [(0, start_hub)]

    while priority_queue:
        current_time, current_node = heapq.heappop(priority_queue)

        # When we hit the destination, we stop and build the path map backwards!
        if current_node == destination_hub:
            path = []
            trace_node = destination_hub
            
            # Trace backward from destination to start using our parents dictionary
            while trace_node is not None:
                path.append(trace_node)
                trace_node = parents[trace_node]
            
            # Since we traced it backward, reverse it to get start -> destination
            path.reverse()
            return current_time, path

        if current_time > shortest_times[current_node]:
            continue

        for neighbor, travel_time in graph[current_node]:
            time_to_neighbor = current_time + travel_time

            if time_to_neighbor < shortest_times[neighbor]:
                shortest_times[neighbor] = time_to_neighbor
                
                # NEW: Record that the fastest way to get to 'neighbor' right now
                # is coming directly from 'current_node'
                parents[neighbor] = current_node
                
                heapq.heappush(priority_queue, (time_to_neighbor, neighbor))

    return -1, []

#print(find_fastest_route_with_path(delivery_map, 1, 2))
print(find_fastest_route_with_path(complex_map, 4, 7))