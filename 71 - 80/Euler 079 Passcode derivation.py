"""
A common security method used for online banking is to ask the user for three
random characters from a passcode. For example, if the passcode was 531278,
they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be:
317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the
file so as to determine the shortest possible secret passcode of unknown length.
"""

#read information from 'keylog.txt' ans store in 'graph'
#graph[x] = a list of all numbers appearing before x
graph = {}
file = open("p079_keylog.txt","r")
for line in file:
    a,b,c = line[0],line[1],line[2]
    graph[a] = graph.get(a,[]) + [b,c]
    graph[b] = graph.get(b,[]) + [c]
file.close()


#given an acyclic graph, returns a permutation of graph's vertices such that
#if vertex u comes before vertex v, then vertex v is not directed to vertex u
#in this case it will present an ordering of the digits that follows all the
#above restrictions (like 5 is before 3, 7 is before 5, ...)
def topological(graph):
    order = []          #final answer
    visited = {}        #visited[i] if vertex 'i' is visited
    Vert = set(graph)   #set of Vertices

    def depthFirstSearch(node):
        visited[node] = False
        for child in graph.get(node,()):
            child_state = visited.get(child, None)

            #When reaching a cycle
            if child_state == False:
                raise ValueError("cycle")
            #Node was already visited
            if child_state == True:
                continue
            #Node has not been visited
            if child_state == None:
                Vert.discard(child)
                depthFirstSearch(child)

        order.append(node)
        visited[node] = 1

    while Vert:
        depthFirstSearch( Vert.pop() )
    return order[::-1]    

ans = topological(graph)
print("".join(ans))
