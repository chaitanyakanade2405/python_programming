#Class simply defines of creating a blueprint/template for creating objects
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")

#Object is an instance of a class
point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()