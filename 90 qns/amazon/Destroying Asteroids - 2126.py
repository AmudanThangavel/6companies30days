class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        max_mass = 0
        total = 0
        length = len(asteroids)
        for i in range(length):
            if asteroids[i] > max_mass:
                max_mass = asteroids[i]
            total += asteroids[i]
        remain_mass = total - max_mass
        if mass + remain_mass < max_mass:
            return False

        asteroids.sort()
        s = mass
        for i in range(length):
            if s >= asteroids[i]:
                s += asteroids[i]
            else:
                return False
        return True
