import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = list(color)
        self.filled = False
        self.__sides = []
        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = list(sides)

    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(r, g, b):
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                return True
            else:
                return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        if len(sides) == self.sides_count:
            for side in sides:
                if side <= 0:
                    return False
            return True
        else:
            return False

    def get_sides(self):
        list_sides = self.__sides
        return list_sides

    def __len__(self):
        perimetr = 0
        if len(self.__sides) > 0:
            for side in self.__sides:
                perimetr += side
        return perimetr

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) > 0:
            self.__radius = self.__len__()/(2*math.pi)

    def get_square(self):
        square = math.pi*(self.__radius**2)
        return square

    def get_radius(self):
        return self.__radius


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        square = 0
        sides_list = super().get_sides()
        if len(sides_list) == 3:
            perimetr_2 = super().__len__()/2
            geron = perimetr_2
            for side in sides_list:
                geron *= (perimetr_2-side)
            square = math.sqrt(geron)
        return square


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        self.__sides = []
        if len(sides) == 1:
            side_list = [sides[0]]*Cube.sides_count
            super().__init__(color, *tuple(side_list))
        else:
            super().__init__(color,  sides)

    def get_volume(self):
        volume = 1
        side_list = self.get_sides()
        if len(side_list) == 12:
            for i in range(3):
                volume *= side_list[i]
        return volume


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())
print(len(circle1))
print(cube1.get_volume())
