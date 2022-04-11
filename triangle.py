import time
from random import randrange
from typing import List


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


def area_triangle(vector_a: tuple[float, float], vector_b: tuple[float, float]):
    return abs(vector_a[0] * vector_b[1] - vector_a[1] * vector_b[0]) / 2


def triangle(points: List[Point]) -> tuple[int, tuple[int, int, int], int, tuple[int, int, int]]:
    eps = 1e-10
    min_area = 0
    max_area = 0
    index_points_min_area = ()
    index_points_max_area = ()

    for a in range(len(points)):
        for b in range(a, len(points)):
            vector_a = vector_coordinates(points[a], points[b])
            for c in range(b, len(points)):
                vector_b = vector_coordinates(points[b], points[c])
                area = area_triangle(vector_a, vector_b)

                if area > max_area:
                    max_area = area
                    index_points_max_area = (a, b, c)

                if area > eps and (min_area - area > eps or min_area < eps):
                    min_area = area
                    index_points_min_area = (a, b, c)

    return min_area, index_points_min_area, max_area, index_points_max_area


def main():
    points = generate_point(count=100, of=-100, to=100)

    start_time = time.time()
    min_area, index_points_min_area, max_area, index_points_max_area = triangle(points)
    print("--- %s seconds ---" % (time.time() - start_time))

    for i in range(len(index_points_min_area)):
        print(points[index_points_min_area[i]].x)
        print(points[index_points_min_area[i]].y)

    coords_x_max = [points[index_points_max_area[i]].x for i in range(len(index_points_max_area))]
    coords_y_max = [points[index_points_max_area[i]].y for i in range(len(index_points_max_area))]
    coords_x_max.append(points[index_points_max_area[0]].x)
    coords_y_max.append(points[index_points_max_area[0]].y)

    print(f"Площадь наименьшего треугольника равна: {min_area}")
    print(f"Его координаты:"
          f" {points[index_points_min_area[0]].x, points[index_points_min_area[0]].y},"
          f" {points[index_points_min_area[1]].x, points[index_points_min_area[1]].y},"
          f" {points[index_points_min_area[2]].x, points[index_points_min_area[2]].y}")

    print(f"Площадь наибольшего треугольника равна: {max_area}")
    print(f"Его координаты:"
          f" {points[index_points_max_area[0]].x, points[index_points_max_area[0]].y},"
          f" {points[index_points_max_area[1]].x, points[index_points_max_area[1]].y},"
          f" {points[index_points_max_area[2]].x, points[index_points_max_area[2]].y}")


if __name__ == '__main__':
    main()
