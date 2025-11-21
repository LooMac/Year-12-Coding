class Graph():
    def __init__(self):
        self.__graph = {}

    def add_edge(self, u, v):
        #Add edge between two provided verticies
        if u not in self.__graph:
            #If there is no list in dict for u init one
            self.__graph[u] = []
        if v not in self.__graph:
            #Do the same for v
            self.__graph[v] = []
        
        self.__graph[u].append(v)

        self.__graph[v].append(u)

    def display(self):
        #Display each vertex adjascent to other verticies by
        #iterating through each list for each vertex in the dict
        for vertex in self.__graph:
            print(f"{vertex}: {','.join(map(str, self.__graph[vertex]))}")