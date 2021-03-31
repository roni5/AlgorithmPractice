def asteroidCollision(self, asteroids: List[int]) -> List[int]:

    stack =[]

    if not asteroids:
        return stack

    for asteroid in asteroids:
        if len(stack) == 0 or asteroid > 0:
            stack.append(asteroid)
        else:
            top = stack[-1]
            while True:
                if top < 0:
                    stack.append(asteroid)
                    break
                elif top == abs(asteroid):
                    stack.pop()
                    break
                elif top > abs(asteroid):
                    break
                else:
                    stack.pop()
                    if len(stack) == 0:
                        stack.append(asteroid)
                        break
    
    return stack
