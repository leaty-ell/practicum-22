import math
from typing import Optional


class GeometricObject:
    """A class representing a geometric object."""
    
    def __init__(self, x: float = 0.0, y: float = 0.0,
                 color: str = 'black', filled: bool = False) -> None:
        self.__x = float(x)
        self.__y = float(y)
        self.__color = color
        self.__filled = filled
    
    def get_x(self) -> float:
        """Get X-coordinate."""
        return self.__x
    
    def get_y(self) -> float:
        """Get Y-coordinate."""
        return self.__y
    
    def set_coordinate(self, x: float, y: float) -> None:
        """Set X and Y coordinates."""
        self.__x = float(x)
        self.__y = float(y)
    
    def get_color(self) -> str:
        """Get color."""
        return self.__color
    
    def set_color(self, color: str) -> None:
        """Set color."""
        self.__color = color
    
    def is_filled(self) -> bool:
        """Check if the object is filled."""
        return self.__filled
    
    def set_filled(self, filled: bool) -> None:
        """Set filled status."""
        self.__filled = filled
    
    def __str__(self) -> str:
        """Return string representation of the geometric object."""
        filled_str = "filled" if self.__filled else "no filled"
        return f"({self.__x}, {self.__y}) {self.__color} {filled_str}"
    
    def __repr__(self) -> str:
        """Return detailed string representation."""
        return self.__str__()


class Circle(GeometricObject):
    """A class representing a circle."""
    
    def __init__(self, x: float = 0.0, y: float = 0.0, radius: float = 0.0,
                 color: str = 'black', filled: bool = False) -> None:
        super().__init__(x, y, color, filled)
        self.__radius = float(radius) if radius > 0 else 0.0
    
    @property
    def radius(self) -> float:
        """Get radius."""
        return self.__radius
    
    @radius.setter
    def radius(self, value: float) -> None:
        """Set radius (only positive values)."""
        self.__radius = float(value) if value > 0 else 0.0
    
    def get_area(self) -> float:
        """Calculate area of the circle."""
        return math.pi * self.__radius ** 2
    
    def get_perimeter(self) -> float:
        """Calculate perimeter (circumference) of the circle."""
        return 2 * math.pi * self.__radius
    
    def get_diameter(self) -> float:
        """Calculate diameter of the circle."""
        return 2 * self.__radius
    
    def __str__(self) -> str:
        """Return string representation of the circle."""
        return f"radius: {self.__radius}\n{super().__str__()}"
    
    def __repr__(self) -> str:
        """Return detailed string representation."""
        return f"radius: {self.__radius} {super().__str__()}"


class Rectangle(GeometricObject):
    """A class representing a rectangle."""
    
    def __init__(self, x: float = 0.0, y: float = 0.0, width: float = 0.0,
                 height: float = 0.0, color: str = 'black', filled: bool = False) -> None:
        super().__init__(x, y, color, filled)
        self.__width = float(width) if width > 0 else 0.0
        self.__height = float(height) if height > 0 else 0.0
    
    def get_width(self) -> float:
        """Get width."""
        return self.__width
    
    def set_width(self, width: float) -> None:
        """Set width (only positive values)."""
        self.__width = float(width) if width > 0 else 0.0
    
    def get_height(self) -> float:
        """Get height."""
        return self.__height
    
    def set_height(self, height: float) -> None:
        """Set height (only positive values)."""
        self.__height = float(height) if height > 0 else 0.0
    
    def get_area(self) -> float:
        """Calculate area of the rectangle."""
        return self.__width * self.__height
    
    def get_perimeter(self) -> float:
        """Calculate perimeter of the rectangle."""
        return 2 * (self.__width + self.__height)
    
    def __str__(self) -> str:
        """Return string representation of the rectangle."""
        return f"width: {self.__width}\nheight: {self.__height}\n{super().__str__()}"
    
    def __repr__(self) -> str:
        """Return detailed string representation."""
        return f"width: {self.__width} height: {self.__height} {super().__str__()}"


def main() -> None:
    """
    The main function demonstrating the classes.
    """
    point = GeometricObject()
    print(point)
    print()
    
    point.set_coordinate(-4, 9)
    print(point.get_x())
    print(point.get_y())
    point.set_color('red')
    print(point.get_color())
    point.set_filled(True)
    print(point.is_filled())
    print()
    print(point)
    print()
    
    point_2 = GeometricObject(8, -4, 'blue', True)
    print(point_2)
    print()
    circle = Circle()
    print(circle)
    print()
    
    circle.radius = -34
    print(circle.radius)
    circle.radius = 12
    print(circle.radius)
    print()
    
    circle_2 = Circle(3, -100, 20, 'green', True)
    print(circle_2)
    print()
    
    circle_2.set_color('grey')
    print(circle_2.get_color())
    print()
    
    print(circle_2.get_area())
    print(circle_2.get_perimeter())
    print(circle_2.get_diameter())
    print()
    
    circle_3 = Circle(90, -84, -223, 'pink')
    print(circle_3)
    print()
    

    rectangle = Rectangle()
    print(rectangle)
    print()
    rectangle.set_coordinate(11, 29)
    rectangle.set_color('yellow')
    rectangle.set_width(-10)
    rectangle.set_height(20)
    print(rectangle)
    print()
    rectangle.set_width(100)
    print(rectangle.get_width())
    print(rectangle.get_height())
    print()
    
    print(rectangle.get_area())
    print(rectangle.get_perimeter())
    print()
    
    rectangle_2 = Rectangle(10, 20, 30, -40, 'brown', True)
    print(rectangle_2)
    print()
    
    figures = []
    figures.append(point)
    figures.append(circle_2)
    figures.append(rectangle)
    print(figures)


if __name__ == "__main__":
    main()
