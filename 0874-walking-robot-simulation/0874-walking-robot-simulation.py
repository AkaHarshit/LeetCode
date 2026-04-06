class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        obs = set((x, y) for x, y in obstacles)
        
        x, y = 0, 0
        d = 0  
        max_dist = 0
        
        for cmd in commands:
            if cmd == -1:  
                d = (d + 1) % 4
            elif cmd == -2:  
                d = (d - 1) % 4
            else:
                dx, dy = dirs[d]
                for _ in range(cmd):
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in obs:
                        break
                    
                    x, y = nx, ny
                    max_dist = max(max_dist, x*x + y*y)
        
        return max_dist