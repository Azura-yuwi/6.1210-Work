import sys
sys.setrecursionlimit(1500)

def dfs(Adj, s, parent = None, order = None): #given by template
    if parent is None:
        parent = [None for v in Adj]
        order = []
        parent[s] = s
    for v in Adj[s]:
        if parent[v] is None:
            parent[v] = s
            dfs(Adj, v, parent, order)
    order.append(s)
    return parent, order

def full_dfs(Adj): #given by template
    parent = [None for v in Adj]
    order = []
    for v in range(len(Adj)):
        if parent[v] is None:
            parent[v] = v
            dfs(Adj, v, parent, order)
    return parent, order

def find_meeting_point(Adj):
    '''
    inputs:
        Adj - an adjacency list such as [[1,2], [2], []]
    return a meeting point or None if no meeting points exist
    '''

    # reverse the edges
    revAdj = [[] for v in Adj]
    for v in range(len(Adj)):
        for s in Adj[v]:
            revAdj[s].append(v)

    p, ord = full_dfs(revAdj)
    last = ord[len(ord)-1]

    np, nord = dfs(revAdj, last)
    work = True

    for v in range(len(Adj)):
        if np[v] is None:
            work = False

    if work:
        return last

    return None

#adj = [[1,2],[2],[]]
#print(find_meeting_point(adj))# should return 2

#adj = [[1,2],[2],[1]]
#print(find_meeting_point(adj))# should return 2 or 1

#adj = [[1,2],[2],[1],[]]
#print(find_meeting_point(adj)) # should return None