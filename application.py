import numpy as np
def chebyshev_distance(p1, p2):
    """Docstring..."""
    return max(abs(x - y) for x, y in zip(p1, p2))

def chebyshev_distance1(p1, p2):
    return max([abs(x - y) for x, y in zip(p1, p2)])


def chebyshev_distance2(p1, p2):
    return np.max(np.abs(np.array(p1) - np.array(p2)))


if __name__ == "__main__":
    point1 = (1, 2, 3)
    point2 = (4, 5, 6)
    distance = chebyshev_distance(point1, point2)
    print("Chebyshev Distance:", distance)
    distance1 = chebyshev_distance1(point1, point2)
    print("Chebyshev Distance1:", distance1)
    distance2 = chebyshev_distance2(point1, point2)
    print("Chebyshev Distance2:", distance2)
