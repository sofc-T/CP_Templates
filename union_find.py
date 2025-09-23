nodes = []
parent = {i:i for i in range(len(nodes))}
def getParent(node):
    if node == parent[node]:
        return node
    
    # path reduction 
    # comment the line below to disable path reduction
    parent[node] = getParent(parent[node])
    return parent[node]

def union(node1, node2):
    parent[getParent(node1)] = parent[getParent(node2)]
