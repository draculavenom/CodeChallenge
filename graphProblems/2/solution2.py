delivery_map = {
    1: [(2, 10), (3, 5)],
    2: [(1, 10), (4, 2)],
    3: [(1, 5),  (4, 1)],
    4: [(2, 2),  (3, 1)]
}


def find_fastest_route(graph, start_hub, destination_hub):
    ans = -1
    optim_route = []
    adjacent_roads = graph[start_hub]
    possible_routes = create_possible_routes(start_hub, adjacent_roads)
    

    #I need to generate all the possible routes, then check with is the best one.
    for p in possible_routes:
        print(possible_routes)
        print(p)
        adjacent_roads = graph[p[0][2]]
        new_routes = create_possible_routes(p[0][2], adjacent_roads)
        possible_routes.remove(p)
        for nr in new_routes:
            possible_routes.append([p, nr])
        
    
    
    print(possible_routes)


    optim_route = target_search(possible_routes, destination_hub)
    print("optim routes are: ")
    print(optim_route)
    if len(optim_route) > 0:
        ans = sum_time(optim_route)
    
    return ans

#the purpose is to return a list of tuples with the following structure:
#start point, cost, target point
#then I will create a new item in the list of that node has another posibility, but if one node already exist, I should continue from that point instead
def create_possible_routes(h, roads):
    possible_routes = []
    for r in roads:
        #if len(possible_routes) == 0:
            possible_routes.append([(h, r[1], r[0])])
    return possible_routes

#this function will search if the target exist inside the adjacent nodes of a given hub
def target_search(pr, t):
    ans = []
    for r in pr:
        for p in r:
            if p[2] == t:
                ans.append(p)
    return ans

def sum_time(routes):
    sum = 0
    for r in routes:
        sum += r[1]
    return sum

print(find_fastest_route(delivery_map, 1, 2))