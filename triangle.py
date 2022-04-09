from random import uniform
from typing import List


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


def generate_point(count: int) -> List[Point]:
    points: List[Point] = []
    for i in range(count):
        points.append(Point(uniform(0, 5), uniform(0, 5)))
    return points


def calc_vector_coordinates(point_b: Point, point_a: Point):
    return point_b.x - point_a.x, point_b.y - point_a.y


def calculating_area_triangle(points: List[Point]) -> tuple[int, tuple[int, int, int], int, tuple[int, int, int]]:
    eps = 1e-10
    min_area = 0
    max_area = 0
    coords_min_area = ()
    coords_max_area = ()

    for a in range(len(points)):
        for b in range(len(points)):
            vector_a = calc_vector_coordinates(points[b], points[a])
            for c in range(len(points)):
                vector_b = calc_vector_coordinates(points[c], points[b])
                area = abs(vector_a[0] * vector_b[1] - vector_a[1] * vector_b[0]) / 2

                if area > max_area:
                    max_area = area
                    coords_max_area = (a, b, c)

                if area > eps and (min_area - area > eps or min_area < eps):
                    min_area = area
                    coords_min_area = (a, b, c)

    return min_area, coords_min_area, max_area, coords_max_area


def main():
    points = generate_point(count=10)
    min_area, coords_min_area, max_area, coords_max_area = calculating_area_triangle(points)
    for i in range(len(coords_min_area)):
        print(points[coords_min_area[i]].x)
        print(points[coords_min_area[i]].y)
    coords_x_max = [points[coords_max_area[i]].x for i in range(len(coords_max_area))]
    coords_y_max = [points[coords_max_area[i]].y for i in range(len(coords_max_area))]
    coords_x_max.append(points[coords_max_area[0]].x)
    coords_y_max.append(points[coords_max_area[0]].y)

    print(f"Площадь наименьшего треугольника равна: {min_area}")
    print(f"Его координаты:"
          f" {points[coords_min_area[0]].x, points[coords_min_area[0]].y},"
          f" {points[coords_min_area[1]].x, points[coords_min_area[1]].y},"
          f" {points[coords_min_area[2]].x, points[coords_min_area[2]].y}")

    print(f"Площадь наибольшего треугольника равна: {max_area}")
    print(f"Его координаты:"
          f" {points[coords_max_area[0]].x, points[coords_max_area[0]].y},"
          f" {points[coords_max_area[1]].x, points[coords_max_area[1]].y},"
          f" {points[coords_max_area[2]].x, points[coords_max_area[2]].y}")


if __name__ == '__main__':
    main()
