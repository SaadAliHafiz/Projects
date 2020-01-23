class Vertex:
    def __init__(self,value):
        self.value=value
        self.dist=float("inf")
        self.pred=value
        self.visited=False

class PriorityQueue:
    def __init__(self):
        self.lst=[]

    def IsEmpty(self):
        if self.lst==[]:
            return True
        return False

    def Enqueue(self,v):
        self.lst.append(v)

    def ExtractMin(self):
        minloc=self.__FindMin()
        y=self.lst[minloc]
        self.lst.pop(minloc)
        return y

    def __FindMin(self):
        minloc=self.lst[0]
        loc=0
        for i in range(len(self.lst)):
            if self.lst[i].dist<minloc.dist:
                minloc=self.lst[i]
                loc=i
        return loc
class DGraph:
    def __init__(self,vertex):
        self.vertex=vertex
        self.adjMat=[[0 for i in range(vertex)]for j in range(vertex)]

    def AddDirectedEdges(self,src,dest,weight):
        self.adjMat[src][dest]=weight

    def GetDirectedNeighbours(self,source):
        neg=[]
        for i in range(self.vertex):
            if self.adjMat[source][i]>0:
                neg.append(i)
        return neg
    def DijkstraShortestPath(self,source):
        cost=[]
        #q=PriorityQueue()
        for i in range(self.vertex):
            cost.append(Vertex(i))
        for i in range(self.vertex):
            cost[i].dist=float("inf")
        cost[source].dist=0
        q = PriorityQueue()
        for i in range(self.vertex):
            q.Enqueue(cost[i])
        #q = PriorityQueue()
        while not q.IsEmpty():
            z=q.ExtractMin()
            self.visited=True
            neighbours=self.GetDirectedNeighbours(z.value)
            for i in neighbours:
                if cost[i].visited==False and cost[i].dist>z.dist+self.adjMat[z.value][i]:
                    cost[i].dist=z.dist+self.adjMat[z.value][i]
                    cost[i].pred=z.value
        for j in cost:
            print(j.value,j.dist,j.pred)

d=DGraph(4)
d.AddDirectedEdges(0,1,5)
d.AddDirectedEdges(0,2,20)
d.AddDirectedEdges(0,3,4)
d.AddDirectedEdges(0,1,8)
d.DijkstraShortestPath(0)
