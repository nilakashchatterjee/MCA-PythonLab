# Q4. Define a class Rectangle. The class should contain sides: length and breadth of the rectangle
# as
# the data members. It should support the following methods:
# (a) Constructor to initialize the data members: length and breadth
# (b) setLength for updating the length of the rectangle.
# (c) Setbreadth for updating breadth of the rectangle.
# (d) getBreadth for retrieving the breadth of the rectangle.
# (e) Area to find the area of the rectangle.
# (f) Perimeter for finding the perimeter of the rectangle

class rectangle:
    # defining the constructor
    def __init__(self):
        self.length = 1
        self.breadth = 1
    # setting functions
    def setLength(self,length):
        self.length = length
    def setBreadth(self,breadth):
        self.breadth = breadth
    # getting functions
    def getLength(self):
        print("The length of the rectangle is:",self.length)
    def getBreadth(self):
        print("The breadth of the rectangle is:",self.breadth)
    # area function
   def area(self):
        ar = self.length * self.breadth
        print("The area of the reactangle is:",ar)
    # perimeter function
    def perimeter(self):
        peri = 2 * (self.length + self.breadth)
        print("The perimeter of the reactangle is:",peri)

a = rectangle() #instance of class
a.setLength(8)
a.setBreadth(4)
a.getBreadth()
a.getLength()
a.area() 
a.perimeter()