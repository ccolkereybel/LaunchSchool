
from add_point import coordinates

def get_coordinates():
    return coordinates[:]


def reflect_point(coordinates):
    x, y = coordinates
    return (x, -y)

def calculate_reflected_slope():
    (x2, y2), (x1, y1) = [reflect_point(point) for point in get_coordinates()]
    return (y2 - y1) / (x2 - x1)