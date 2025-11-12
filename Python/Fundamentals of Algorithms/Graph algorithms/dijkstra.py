import heapq

def dijkstra(graph, start = 0):
    n_nodes = len(graph)
    
    dists = {dist: float('inf') for dist in range(n_nodes)}
    prevs = {prev: None for prev in range(n_nodes)}
    is_visited = {visit: False for visit in range(n_nodes)}
    
    dists[0] = 0

    curr_queue = [[dists[start], start]]

    while curr_queue:
        curr_dist, curr_node = heapq.heappop(curr_queue)

        if is_visited[curr_node] == False:
            is_visited[curr_node] = True

            for neighbour in range(n_nodes):
                edge_cost = graph[curr_node][neighbour]

                if edge_cost > 0:
                    new_dist = curr_dist + edge_cost

                    if new_dist < dists[neighbour]:
                        dists[neighbour] = new_dist
                        
                        prevs[neighbour] = curr_node

                        heapq.heappush(curr_queue, [new_dist,neighbour])
    return dists, prevs
                        
def display_shortest_paths(costs, previous_nodes, nodes, start_node_index): 
    # Iterate over all the nodes with their indices using enumerate for simultaneous access. 
    for index, node in enumerate(nodes): 
        # Check if the current node is not the start node. 
        if index != start_node_index: 
            # Set the current node index to start tracing back the path. 
            current_index = index 
            # Initialise the path with the current node. 
            path = node 
            # Trace back through the previous nodes until we reach the start node. 
            while previous_nodes[current_index] is not None: 
                # Prepend the previous node to the path. 
                # Previous node is fetched from 'previous_nodes' list using current index. 
                path = nodes[previous_nodes[current_index]] + path 
                # Update the current index to the index of the previous node. 
                current_index = previous_nodes[current_index] 
 
            # After the full path has been traced back, print the path with the total cost. 
            # The total cost is fetched from 'costs' list using the index of the current node. 
            print("Path for", node, "with cost", costs[index], ":",path) 

nodes = ["0","1","2","3","4"]
        
graph = [
    # To: 0  1  2  3  4  <-- Destination Node
    [ 0,  7,  5, 12,  0],  # From Node 0 (added A[0][2]=5 for symmetry with A[2][0]=5)
    [ 7,  0,  4,  0,  9],  # From Node 1 (added A[1][0]=7, A[1][4]=9)
    [ 5,  4,  0,  8,  0],  # From Node 2 (A[2][0]=5, A[2][1]=4)
    [12,  0,  8,  0,  6],  # From Node 3 (A[3][0]=12, A[3][2]=8)
    [ 0,  9,  0,  6,  0]   # From Node 4 (A[4][1]=9, A[4][3]=6)
]


costs, prevs = dijkstra(graph)

display_shortest_paths(costs, prevs, nodes, 0)