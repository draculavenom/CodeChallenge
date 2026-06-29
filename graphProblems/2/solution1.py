print("This is not working, but I wanted to keed the idea so far")
delivery_map = {
    1: [(2, 10), (3, 5)],
    2: [(1, 10), (4, 2)],
    3: [(1, 5),  (4, 1)],
    4: [(2, 2),  (3, 1)]
}


def find_fastest_route(graph, start_hub, destination_hub):
    ans = -1
    optim_route = []
    possible_roads = graph[start_hub]
    checked_routes = [start_hub]
    i = 0
    
    while len(possible_roads) > 0:

        keys = get_keys_from_tuple_list(possible_roads)
        print(keys)
        for r in checked_routes:
            if r in keys:
                possible_roads = delete_tuples_from_list(r, possible_roads)
                #I need to remove the tuples with that key

        for r in possible_roads:
            if r[0] == destination_hub:
                if optim_route == []:
                    optim_route = [r]
                if sum_time(optim_route) > r[1]:
                    optim_route = [r]
                
            possible_roads = possible_roads + graph[r[0]]
            checked_routes.append(r[0])
        print(possible_roads)
        i = i + 1
        if i == 3:
            break
    
    if any(item[0] == destination_hub for item in possible_roads):
        ans = sum_time(optim_route)
    
    return ans

def sum_time(routes):
    sum = 0
    for r in routes:
        sum += r[1]
    return sum

def get_keys_from_tuple_list(l):
    ans = []
    for t in l:
        ans.append(t[0])
    return list(set(ans))

def delete_tuples_from_list(k, l):
    ans = []
    for l1 in l:
        if l1[0] != k:
            ans.append(l1)
    return ans

print(find_fastest_route(delivery_map, 1, 2))