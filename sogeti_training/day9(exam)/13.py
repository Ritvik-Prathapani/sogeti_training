class shape:
    def area(self):
        print(f"prints the area")

class square(shape):
    def area(self,length,breadth):
        print(f"the area of square is {length*breadth}")
    
class triangle(shape):
    def area(self,base,height):
        print(f"the area triangle is {0.5*base*height}")

a1=square()
a1.area(2,3)
t1=triangle()
t1.area(5,4)

