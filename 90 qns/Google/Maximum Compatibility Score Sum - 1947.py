class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        set_students = [set((i + 1) if v else -(i + 1)
                            for i, v in enumerate(row)) for row in students]
        set_mentors = [set((i + 1) if v else -(i + 1)
                           for i, v in enumerate(row)) for row in mentors]
        return max(sum(len(s & m) for s, m in zip(p, set_mentors))
                   for p in permutations(set_students))
