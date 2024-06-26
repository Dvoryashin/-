from collections import deque
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []
      
search_queue = deque()

search_queue += graph['you']

searched = []
 
while search_queue:
    person = search_queue.popleft()
    if person not in searched:
        if person[-1] == 'm':
            print(person + 'is a mango seller')
        else:
            search_queue += graph[person]
            searched.append(person)