from random import randrange
from typing import List
import time


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    @property
    def get_coords(self):
        return self.x, self.y


def generate_point(count: int) -> List[Point]:
    points: List[Point] = []
    for i in range(count):
        points.append(Point(randrange(0, 100), randrange(0, 100)))
    return points


def calc_vector_coordinates(point_b: Point, point_a: Point):
    return point_b.x - point_a.x, point_b.y - point_a.y


def composition_vector(point_a: Point, point_b: Point):
    return point_a.x * point_b.y - point_a.y * point_b.x


def calculation_area(point_a: Point, point_b: Point, point_c: Point, point_d: Point):
    return sum((composition_vector(point_a, point_b),
                composition_vector(point_b, point_c),
                composition_vector(point_c, point_d),
                composition_vector(point_d, point_a)))


def calculating_area_square(points):
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
                                    area = calculation_area(points[a], points[b], points[c], points[d])

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
    min_area, coords_min_area, max_area, coords_max_area = calculating_area_square(points)

    print("--- %s seconds ---" % (time.time() - start_time))

    if min_area == 0 and max_area == 0:
        print("Квадрат не найден")
    else:
        print(f"Площадь наибольшего квадрата равна: {max_area}")
        print(f"Его координаты:"
              f" {points[coords_max_area[0]].x, points[coords_max_area[0]].y},"
              f" {points[coords_max_area[1]].x, points[coords_max_area[1]].y},"
              f" {points[coords_max_area[2]].x, points[coords_max_area[2]].y},"
              f" {points[coords_max_area[3]].x, points[coords_max_area[3]].y}")
        print(f"Площадь наименьшего квадрата равна: {min_area}")
        print(f"Его координаты:"
              f" {points[coords_min_area[0]].x, points[coords_min_area[0]].y},"
              f" {points[coords_min_area[1]].x, points[coords_min_area[1]].y},"
              f" {points[coords_min_area[2]].x, points[coords_min_area[2]].y},"
              f" {points[coords_min_area[3]].x, points[coords_min_area[3]].y}")


if __name__ == '__main__':
    main()
