def has_proper_sides(sides):
    return sides[0] > 0 and sides[1] > 0 and sides[2] > 0

def has_proper_sides_lengh(sides):
    print(sides[0] + sides[1] >= sides[2])
    return sides[0] + sides[1] >= sides[2] and sides[0] + sides[2] >= sides[1] and sides[1] + sides[2] >= sides[0]

def is_a_triangle(sides):
    return has_proper_sides(sides) and has_proper_sides_lengh(sides)

def equilateral(sides):
    if(not is_a_triangle(sides)):
        return False
    return sides[0] == sides[1] == sides[2]


def isosceles(sides):
    if(not is_a_triangle(sides)):
        return False
    return sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]


def scalene(sides):
    if(not is_a_triangle(sides)):
        return False
    return sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]
