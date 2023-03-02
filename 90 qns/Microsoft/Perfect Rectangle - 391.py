class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        if not rectangles:
            return False
        if len(rectangles) == 1:
            return True
        x1 = y1 = float('inf')
        x2 = y2 = float('-inf')
        area = 0
        points = set()
        for x, y, xx, yy in rectangles:
            x1 = min(x1, x)
            y1 = min(y1, y)
            x2 = max(x2, xx)
            y2 = max(y2, yy)
            area += (xx - x) * (yy - y)
            p1 = (x, y)
            p2 = (xx, y)
            p3 = (xx, yy)
            p4 = (x, yy)
            for p in (p1, p2, p3, p4):
                if p in points:
                    points.remove(p)
                else:
                    points.add(p)
        return area == (x2 - x1) * (y2 - y1) and points == {(x1, y1), (x1, y2), (x2, y1), (x2, y2)}
