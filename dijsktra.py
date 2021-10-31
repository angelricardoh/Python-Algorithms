import heapq
def dijkstra(graph,node):
    distances={node:float('inf') for node in graph}
    distances[node]=0
    came_from={node:None for node in graph}
    queue=[(0,node)]
    
    while queue:
        current_distance,current_node=heapq.heappop(queue)
        # relaxation
        for next_node,weight in graph[current_node].items():
            distance_temp=current_distance+weight
            if distance_temp<distances[next_node]:
                distances[next_node]=distance_temp
                came_from[next_node]=current_node
                heapq.heappush(queue,(distance_temp,next_node))
    return distances,came_from

graph={
    'A':{'B':2,'C':3},
    'B':{'D':3,'E':1},
    'C':{'F':2},
    'D':{},
    'E':{'F':1},
    'F':{}
}
graph['A']# return {'B':2,'C':3}, which are the subnode of A
graph['A']['B']# return 2, which is the distance of A and B

print(dijkstra(graph,'A'))
# return {'A': 0, 'B': 2, 'C': 3, 'D': 5, 'E': 3, 'F': 4},
# {'A': None, 'B': 'A', 'C': 'A', 'D': 'B', 'E': 'B', 'F': 'E'}
# the result means for example, 'A' to 'A' is 0, 'A' to 'B' is 2
# the shortest path: for example, 'A' to 'F', we start from 'F'
# and trace back. 'F' comes from 'E', 'E' from 'B', 'B' from 'A'