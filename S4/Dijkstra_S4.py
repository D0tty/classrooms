# -*- coding: utf-8 -*-
"""
March 2018
Graphs: Shortest Paths Dijkstra
@author: Nathalie
"""

from algopy import graph


inf = float('inf')

# cost of edge x -> y
# G.costs[(x, y)]
    

def chooseMin(dist, M):
    """
    M: boolean vector, represents a set of vertices
    returns the vertex in M that minimized the vector dist
    if no vertex such that dist[x] != inf, returns None
    """
    x = None
    mini = inf
    for i in range(len(dist)):
        if M[i] and dist[i] < mini:
            x = i
            mini = dist[i]
    return x
    
def Dijkstra(G, src):
    dist = [inf] * G.order
    dist[src] = 0
    p = [-1] * G.order    
    M = [True] * G.order
    x = src
    n = 1
    while x != None and n < G.order    :
        M[x] = False
        for y in G.adjlists[x]:
            if dist[x] + G.costs[(x, y)] < dist[y]:
                dist[y] = dist[x] + G.costs[(x, y)]
                p[y] = x
        
        x = chooseMin(dist, M)
        n += 1
        
    return (dist, p)
    


#----------------------------------------------------------------------------
    
"""
    instead of working with a set of all vertices: 
    here we have a list that contains "usefull" vertices
"""

def delMinInList(L, dist):
    '''
    returns and deletes the vertex in L (not empty) with minimum distance
    '''
    imin = 0
    for i in range(1, len(L)):
        if dist[L[i]] < dist[L[imin]]:
            imin = i
    x = L[imin]
    L[imin] = L[-1]
    L.pop()
    return x

def Dijkstra2(G, src, dst = None):
    dist = [inf] * G.order
    dist[src] = 0
    p = [-1] * G.order    
    L = [src]
    while L != []:
        x = delMinInList(L, dist)
        for y in G.adjlists[x]:
            if dist[x] + G.costs[(x, y)] < dist[y]:
                if dist[y] == inf:
                    L.append(y)
                dist[y] = dist[x] + G.costs[(x, y)]
                p[y] = x
        
    return (dist, p)
    
    
#------------------------------------------------------------------------------
# exercise 1.2: round trip
# Optimization: Dijkstra with a heap 
    
from algopy import heap_spe as heap
    
def Dijkstra_withoutM(G, src, dst, M):
    '''
    src != dst
    dst is reachable from src
    the shortest path between src and dst without vertices in M
    '''
    #FIXME
    pass

def there_and_back(G, src, dst):
    #FIXME
    pass
