class Shape:
    def area(self):
        return 0

class Triangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
    
    def area(self):
        return 0.5 * self.width * self.height
    
    def __str__(self):
        return f"Triangle with width {self.width} and height {self.height} has an area of {self.area()}."

triangle = Triangle(10, 5)
print(triangle)