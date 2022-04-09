import math
import time
from random import randrange
from typing import List


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    @property
    def get_coords(self):
        return self.x, self.y


def calc_vector_coordinates(point_b: Point, point_a: Point):
    return point_b.x - point_a.x, point_b.y - point_a.y


def generate_point(count: int) -> List[Point]:
    points: List[Point] = []
    for i in range(count):
        points.append(Point(randrange(0, 5), randrange(0, 5)))
    return points


def is_quare(points):
    eps = 1e-10
    min_area = 0
    max_area = 0
    coords_min_area = ()
    coords_max_area = ()

    for a in range(len(points)):
        for b in range(len(points)):
            if b != a:
                for c in range(len(points)):
                    if c != a and c != b:
                        vector_a = calc_vector_coordinates(points[b], points[a])
                        vector_b = calc_vector_coordinates(points[c], points[b])
                        if vector_a[0] == vector_b[1] and abs(vector_a[1]) == vector_b[0]:
                            for d in range(len(points)):
                                vector_c = calc_vector_coordinates(points[d], points[c])
                                if abs(vector_a[0]) == vector_c[0] and abs(vector_a[1]) == vector_c[1]:
                                    area = points[a].x * points[b].y - points[a].y * points[b].x + points[b].x * points[c].y - points[b].y * points[c].x + points[c].x * points[d].y - points[c].y * points[d].x + points[d].x * points[a].y - points[d].y * points[a].x

                                    if area > max_area:
                                        max_area = area
                                        coords_max_area = (a, b, c, d)

                                    if area > eps and (min_area - area > eps or min_area < eps):
                                        min_area = area
                                        coords_min_area = (a, b, c, d)

    return min_area, coords_min_area, max_area, coords_max_area


def main():
    start_time = time.time()
    points = generate_point(count=100)
    # points = (Point(3, 8), Point(1, 4), Point(5, 2), Point(2, -3), Point(5, -1), Point(7, 6), Point(3, 2), Point(0, 0),
    #           Point(3, 7), Point(3, 1), Point(0, 8), Point(3, 8))
    is_quare(points)
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()
