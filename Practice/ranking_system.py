class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0
        self.posRanks = [-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8]
    
    def inc_progress(self, num):
        curr = self.posRanks.index(self.rank)
        ans = self.posRanks.index(num)
        print(curr, ans)
        if curr == ans and self.rank != 8:
            self.progress += 3
        elif curr - ans < 1 and self.rank != 8:
            gap = ans - curr
            d = 10 * gap * gap
            self.progress += d
        elif curr - ans < 0 or abs(curr - ans) == 1 and self.rank != 8:
            self.progress += 1

        while self.progress >= 100:
            self.progress -= 100
            curr+=1
        if curr <= 15: 
            self.rank = self.posRanks[curr]
        else:
            self.rank = 8
        if self.rank == 8:
            self.progress = 0

        

user = User()
user.inc_progress(6)
print(user.rank)
print(user.progress)






