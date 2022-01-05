class Fancy:

    def __init__(self):
        self.seq = []
        

    def append(self, val: int) -> None:
        self.seq.append(val)
        

    def addAll(self, inc: int) -> None:
        temp = [x + inc for x in self.seq]
        self.seq = temp
        

    def multAll(self, m: int) -> None:
        temp = [x * m for x in self.seq]
        self.seq = temp

    def getIndex(self, idx: int) -> int:
        if self.seq[idx]:
            return self.seq[idx]
        else:
            return -1
        


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)