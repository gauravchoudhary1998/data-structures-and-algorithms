class MyCalendarTwo:

    def __init__(self):
        self.singles = []
        self.doubles = []

    def book(self, startTime: int, endTime: int) -> bool:
        
        for d in self.doubles:
            if max(d[0], startTime) < min(d[1],endTime):
                return False
        
        for s in self.singles: 
            if max(s[0],startTime) < min(s[1],endTime): 
                self.doubles.append([max(s[0],startTime), min(s[1],endTime)])

        self.singles.append([startTime,endTime])

        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)