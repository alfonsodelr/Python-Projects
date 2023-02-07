class Line:
    def __init__(self):
        self.start = self.Point(0,0)
        self.end = self.Point(1,1)

    def show_line(self):
        print("start: " , self.start.x, self.start.y, "\nend: ", self.end.y, self.end.y)

    def move_start(self, x, y):
        self.start.x = x
        self.start.y = y

    def move_end(self,x,y):
        self.end.x = x
        self.end.y = y

    def copy_line(self, other):
        self.start.x = other.start.x
        self.start.y = other.start.y
        self.end.x = other.end.x
        self.end.y = other.end.y

    class Point:
        def __init__(self):
            self.x = 0
            self.y = 0
        def __init__(self, x, y):
            self.x = x
            self.y = y
        def move_point(self, x, y):
            self.x = x
            self.y = y

class Upper:
    def __init__(self):
        self.test = Inner()

class Inner:
    def __init__(self):
        self.mine = 0

class Parent:
    def __init__(self):
        self.a = 0
        self.b = "empty"
        self.c = 0
    
class Child(Parent):
    def __init__(self, a,b,c,d):
        super().__init__(a,b,c)
        self.d = d


def main():
    line = Line()
    line.show_line()
    line.move_start(10,20)
    line.move_end(20,20)
    line.show_line()
    line2 = Line()
    line2.copy_line(line)
    line2.show_line()

main()