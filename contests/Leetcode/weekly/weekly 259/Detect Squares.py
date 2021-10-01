class DetectSquares:

    def __init__(self):
        self.store={}

    def add(self, point: List[int]) -> None:
        point=tuple(point)
        if point not in self.store:
            self.store[point]=0
        self.store[point]+=1

    def count(self, point: List[int]) -> int:
        ans=0
        x,y = point[0]-1,point[1]-1
        while x>=0 and y>=0:
            if (x,y) in self.store and (x,point[1]) in self.store and (point[0],y) in self.store:
                ans += self.store[(x,y)] * self.store[(x,point[1])] * self.store[(point[0],y)]
            x-=1
            y-=1
        x,y = point[0]-1,point[1]+1
        while x>=0 and y<=1000:
            if (x,y) in self.store and (x,point[1]) in self.store and (point[0],y) in self.store:
                ans += self.store[(x,y)] * self.store[(x,point[1])] * self.store[(point[0],y)]
            x-=1
            y+=1
        x,y = point[0]+1,point[1]-1
        while x<=1000 and y>=0:
            if (x,y) in self.store and (x,point[1]) in self.store and (point[0],y) in self.store:
                ans += self.store[(x,y)] * self.store[(x,point[1])] * self.store[(point[0],y)]
            x+=1
            y-=1
        x,y = point[0]+1,point[1]+1
        while x<=1000 and y<=1000:
            if (x,y) in self.store and (x,point[1]) in self.store and (point[0],y) in self.store:
                ans += self.store[(x,y)] * self.store[(x,point[1])] * self.store[(point[0],y)]
            x+=1
            y+=1
        return ans

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
