class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.x = 0
        self.y = 0
        self.dir = 0  
        self.dirs = ["East", "North", "West", "South"]
        self.perimeter = 2 * (width + height) - 4
        self.started = False 

    def step(self, num: int) -> None:
        if self.perimeter == 0:
            return
        
        self.started = True
        num %= self.perimeter
    
        if num == 0:
            num = self.perimeter
        
        while num > 0:
            if self.dir == 0:  
                steps = min(num, self.w - 1 - self.x)
                self.x += steps
            elif self.dir == 1: 
                steps = min(num, self.h - 1 - self.y)
                self.y += steps
            elif self.dir == 2: 
                steps = min(num, self.x)
                self.x -= steps
            else:  
                steps = min(num, self.y)
                self.y -= steps
            
            num -= steps

            if num > 0:
                self.dir = (self.dir + 1) % 4

    def getPos(self) -> list:
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.dirs[self.dir]