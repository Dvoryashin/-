infinity = float('inf')

#пути
graph = {}

graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5

graph['a'] = {}
graph['a']['fin'] = 1

graph['fin'] = {}

#цены
costs = {}

costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

#родители
parents = {}

parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

processed = []

def cheapest_node(costs, processed):
    lowest_cost = float('inf')
    cheapest_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            cheapest_node = node

    return cheapest_node

node = cheapest_node(costs, processed)
while node is not None:
    processed.append(node)
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = costs[node] + neighbors[n]
        if new_cost < costs[n]:
            costs[n] = new_cost
            parents[n] = node
    node = cheapest_node(costs, processed)

print(costs)
