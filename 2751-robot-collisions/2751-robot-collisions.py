class Solution:
    def survivedRobotsHealths(self, positions: list[int], healths: list[int], directions: str) -> list[int]:
        n = len(positions)
        
        robots = []
        for i in range(n):
            robots.append((positions[i], healths[i], directions[i], i))
        robots.sort()
        
        stack = []  
        health = [r[1] for r in robots]
        
        for i in range(n):
            pos, h, d, idx = robots[i]
            
            if d == 'R':
                stack.append(i)
            else:  
                while stack and health[i] > 0:
                    j = stack[-1]
                    
                    if health[j] < health[i]:
                        stack.pop()
                        health[i] -= 1
                        health[j] = 0
                    elif health[j] > health[i]:
                        health[j] -= 1
                        health[i] = 0
                    else:
                        stack.pop()
                        health[j] = 0
                        health[i] = 0
                        break
        result = []
        for i in range(n):
            if health[i] > 0:
                result.append((robots[i][3], health[i]))

        result.sort()
        
        return [h for _, h in result]