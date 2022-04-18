from random import randrange
from typing import List
import time


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


def generate_point(count: int, of: int, to: int) -> List[Point]:
    points: List[Point] = []
    for i in range(count):
        points.append(Point(randrange(of, to), randrange(of, to)))
    return points


def vector_coordinates(point_a: Point, point_b: Point):
    return point_b.x - point_a.x, point_b.y - point_a.y


def composition_vector(point_a: Point, point_b: Point):
    return point_a.x * point_b.y - point_a.y * point_b.x


def area_square(point_a: Point, point_b: Point, point_c: Point, point_d: Point):
    return sum((composition_vector(point_a, point_b),
                composition_vector(point_b, point_c),
                composition_vector(point_c, point_d),
                composition_vector(point_d, point_a))) / 2


def square(points):
    eps = 1e-10
    min_area = 0
    max_area = 0
    index_points_min_area = ()
    index_points_max_area = ()

    for a in range(len(points)):
        for b in range(a, len(points)):
            for c in range(b, len(points)):
                x_m = (points[a].x + points[c].x) / 2
                y_m = (points[a].y + points[c].y) / 2
                x_b = x_m + y_m - points[a].y
                y_b = y_m - x_m + points[a].x
                if points[b].x == x_b and points[b].y == y_b:
                    for d in range(c, len(points)):
                        x_d = x_m - y_m + points[a].y
                        y_d = y_m + x_m - points[a].x
                        if points[d].x == x_d and points[d].y == y_d:
                            area = area_square(points[a], points[b], points[c], points[d])

                            if area > max_area:
                                max_area = area
                                index_points_max_area = (a, b, c, d)

                            if area > eps and (min_area > area or min_area < eps):
                                min_area = area
                                index_points_min_area = (a, b, c, d)

    return min_area, index_points_min_area, max_area, index_points_max_area


def main():
    points = generate_point(count=100, of=-10, to=10)

    start_time = time.time()
    min_area, index_points_min_area, max_area, index_points_max_area = square(points)
    print("--- %s seconds ---" % (time.time() - start_time))

    if min_area == 0 and max_area == 0:
        print("Квадрат не найден")
    else:
        print(f"Площадь наибольшего квадрата равна: {max_area}")
        print(f"Его координаты:"
              f" {points[index_points_max_area[0]].x, points[index_points_max_area[0]].y},"
              f" {points[index_points_max_area[1]].x, points[index_points_max_area[1]].y},"
              f" {points[index_points_max_area[2]].x, points[index_points_max_area[2]].y},"
              f" {points[index_points_max_area[3]].x, points[index_points_max_area[3]].y}")
        print(f"Площадь наименьшего квадрата равна: {min_area}")
        print(f"Его координаты:"
              f" {points[index_points_min_area[0]].x, points[index_points_min_area[0]].y},"
              f" {points[index_points_min_area[1]].x, points[index_points_min_area[1]].y},"
              f" {points[index_points_min_area[2]].x, points[index_points_min_area[2]].y},"
              f" {points[index_points_min_area[3]].x, points[index_points_min_area[3]].y}")


if __name__ == '__main__':
    main()
