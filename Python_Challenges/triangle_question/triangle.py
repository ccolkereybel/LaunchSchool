"""

Write a program to determine whether a triangle is equilateral, isosceles, or scalene.

An equilateral triangle has all three sides the same length.

An isosceles triangle has exactly two sides of the same length.

A scalene triangle has all sides of different lengths.

Note: For a shape to be a triangle at all, all sides must be of length > 0,
and the sum of the lengths of any two
sides must be greater than the length of the third side.

-check all 3 side lengths greater than 0
-check that sum of any two sides >= third side
-if all 3 sides =, triangle is equilateral
-if two sides =, trianlge is isosceles
-if no sides =, triangle is scalene

creating the class:
    -must accept 3 arguments for the sides
    -save these values in init
    -raise exception if side length <= 0
    -raise exception if not a real triangle
    -return type of triangle using triangle.kind

"""

# class Triangle:
#     def __init__(self, side1, side2, side3):
#         if side1 <= 0 or side2 <= 0 or side3 <= 0:
#             raise ValueError
#         elif side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
#             raise ValueError
#         else:
#             self.side1 = side1
#             self.side2 = side2
#             self.side3 = side3
#             self._kind = None

#     @property
#     def kind(self):
#         if self.side1 == self.side2 == self.side3:
#             self._kind = "equilateral"
#         elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
#             self._kind = 'isosceles'
#         else:
#             self._kind = 'scalene'
#         return self._kind

class Triangle:
    def __init__(self, side1, side2, side3):
        self.sides = [side1, side2, side3]
        if not self._is_valid():
            raise ValueError('Invalid triangle lengths')
        
    def _is_valid(self):
        return(
            all(side > 0 for side in self.sides)
            and self.sides[0] + self.sides[1] > self.sides[2]
            and self.sides[1] + self.sides[2] > self.sides[0]
            and self.sides[0] + self.sides[2] > self.sides[1] 
        )
    
    @property
    def kind(self):
        if len(set(self.sides)) == 1:
            return 'equilateral'
        if len(set(self.sides)) == 2:
            return 'isosceles'
        else:
            return 'scalene'
    