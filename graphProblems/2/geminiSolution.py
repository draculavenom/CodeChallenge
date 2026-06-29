import heapq

delivery_map = {
    1: [(2, 10), (3, 5)],
    2: [(1, 10), (4, 2)],
    3: [(1, 5),  (4, 1)],
    4: [(2, 2),  (3, 1)]
}

def find_fastest_route(graph, start_hub, destination_hub):
    # Step 1: Track the best time found so far for EVERY node.
    # We initialize them to infinity because we haven't found a path yet.
    shortest_times = {node: float('inf') for node in graph}
    shortest_times[start_hub] = 0  # It takes 0 minutes to reach the start

    # Step 2: The Priority Queue (Min-Heap)
    # Stored as tuples: (accumulated_time, current_node)
    # Python's heapq always keeps the smallest accumulated_time at index 0.
    priority_queue = [(0, start_hub)]

    # Step 3: Traverse the graph greedily
    while priority_queue:
        # Always pop the option with the absolute lowest accumulated time
        current_time, current_node = heapq.heappop(priority_queue)

        # If we reached the destination, this is guaranteed to be the fastest route!
        if current_node == destination_hub:
            return current_time

        # If we already found a faster way to this node in the past, skip it
        if current_time > shortest_times[current_node]:
            continue

        # Step 4: Check neighbors
        for neighbor, travel_time in graph[current_node]:
            time_to_neighbor = current_time + travel_time

            # If this new path is faster than any path we've seen to this neighbor before:
            if time_to_neighbor < shortest_times[neighbor]:
                shortest_times[neighbor] = time_to_neighbor  # Update our tracker
                heapq.heappush(priority_queue, (time_to_neighbor, neighbor))

    # If the queue is empty and we never hit the destination, it's unreachable
    return -1

print(find_fastest_route(delivery_map, 1, 2))
#print(find_fastest_route(delivery_map, 1, 1))