"""network = {
    1: [2, 3],
    2: [1, 4],
    3: [1],
    4: [2]
}

network = {
    1: [2],
    2: [1],
    3: [4],
    4: [3]
}"""

network = {
    1: [2, 3],
    2: [1, 3],
    3: [1, 2, 4],
    4: [3]
}

def get_reachable_nodes(graph, start_node):
    ans = [start_node]
    checked_nodes = []
    #For a brute force solution, I need to check each node to see what options they have, I need to be carefull as I could get into a node I have already checked before
    temp_nodes = graph[start_node]
    temp_nodes2 = []
    #I need to add to ans those options that doesn't exist there yet, then I need to register the nodes I just checked to the checked_nodes
    ans = list(set(ans) | set(temp_nodes))
    checked_nodes.append(start_node)
    #now that I have some answer and some new nodes, I need to check each new node, but be carefull to not check again one that I have already or this will never end.
    
    while len(temp_nodes) > 0:
        for n in temp_nodes:
            temp_nodes2 = list(set(temp_nodes2) | set(graph[n]))
            ans = list(set(ans) | set(temp_nodes2))
            checked_nodes.append(n)

        #print(temp_nodes2)
        temp_nodes = [item for item in temp_nodes2 if item not in checked_nodes]

    #print(checked_nodes)
    ans.sort()
    return ans

print(get_reachable_nodes(network, 1))