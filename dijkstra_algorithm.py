import os
start =2
def min_vector(v,Q):
    # print "I'm in min_vector"
    # print "v: %r" % v
    # print "Q: %r" % Q
    m = -1
    for x in Q:
        # print "x: %d" % x
        if v[x] != -1:
            if m==-1:
                m = v[x]
                count = x
            elif v[x]<m:
                m=v[x]
                count = x
    # print "count: %d, min:%f"% (count,m)
    return count, m

def min_pair(a,b):
    m = -1
    # print "min_pair"
    # print "\ta: %f" % a
    # print "\tb: %f" % b

    if a==-1 and b==-1:
        m = -1
    elif a==-1:
        m = b
    elif b==-1:
        m = a
    else:
        m = a if a<b else b
    # print "\t %f" % m
    return m

def min_add(a,b):
    min = 0
    # print "min_add"
    # print "\ta: %f" % a
    # print "\tb: %f" % b
    if a==-1 or b==-1:
        min = -1
    else:
        min = a + b
    # print "\t %f" % min
    return min
# Example Graphs
# G = [
#     [0,4,2,2],
#     [4,0,1,3],
#     [2,1,0,-1],
#     [2,3,0,-1]
# ]
# G = [
#     [0,6,-1,6,5],
#     [-1,0,-1,3,-1],
#     [-1,-1,0,10,-1],
#     [6,-1,7,0,4],
#     [-1,-1,8,-1,0]
#      ]
# G = [
#     [0,3,4,-1,-1,-1,-1],
#     [3,0,-1,2,4,-1,-1],
#     [4,-1,0,2,-1,9,-1],
#     [-1,2,2,0,1,-1,-1],
#     [-1,4,-1,1,0,-1,5],
#     [-1,-1,9,-1,-1,0,8],
#     [-1,-1,-1,-1,5,8,0]
#     ]
G = [
    [0,2,-1,6,-1],
    [2,0,1,-1,-1],
    [-1,1,0,2,-1],
    [6,-1,2,0,8],
    [-1,-1,-1,8,0]
]
distance = 0
S=[]
paths =[]
Q=[]
for i in range(len(G[0])):
    Q.append(i)
v = [-1]*len(G[0])
v[start]=0

while len(Q)>0:
    os.system("clear")
    l, distance = min_vector(v,Q)
    S.append(l)
    v[l]="X"
    del Q[Q.index(l)]
    paths.append("{%d:%d= %5.2f}" % (start,l,distance))
    print "v: %r" % v
    print "distance: %f" % distance
    print "next node: %d" % l
    print "S: %r" % S
    print "Q: %r" % Q
    dv = G[l]
    print "dv(%d): %r" % (l,dv)
    print "offset: %r" % ([distance]*len(G[0]))
    dvPlusOffset = []
    for y in range(len(dv)):
        dvPlusOffset.append(min_add(dv[y],distance))
    print "dv+offset: %r" % dvPlusOffset
    print "current v: %r" %v
    for y in Q:
        # print "y: %d (element of Q)" % y
        v[y]=min_pair(min_add(dv[y],distance),v[y])
    print "next v: %r" % v
    raw_input()
for s in paths:
    print s
