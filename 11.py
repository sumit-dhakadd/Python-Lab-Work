
import turtle

class Pattern:
    def __init__(self):
        self.s = turtle.Screen()
        self.s.bgcolor("black")
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.c = ["red", "yellow", "cyan", "green", "magenta"]

    def spiral(self):
        for i in range(100):
            self.t.color(self.c[i % 5])
            self.t.forward(i * 3)
            self.t.right(91)

    def polygon(self):
        n = int(self.s.numinput("Polygon", "Enter sides:", 6))
        for i in range(n):
            self.t.forward(100)
            self.t.right(360 / n)

    def fractal(self, l, d):
        if d == 0:
            self.t.forward(l)
        else:
            for a in [0, 60, -120, 60]:
                self.fractal(l / 3, d - 1)
                self.t.left(a)

    def koch(self):
        self.t.penup()
        self.t.goto(-200, 100)
        self.t.pendown()
        self.fractal(400, 4)

    def flower(self):
        for i in range(36):
            self.t.color(self.c[i % 5])
            self.t.circle(100)
            self.t.left(10)

    def run(self):
        funcs = [self.spiral, self.polygon, self.koch, self.flower]
        def menu():
            self.t.clear()
            ch = self.s.textinput("Menu", "1.Spiral  2.Polygon\n3.Koch  4.Flower")
            if ch in ["1", "2", "3", "4"]:
                funcs[int(ch)-1]()
            else:
                print("Invalid choice!")
            self.s.ontimer(menu, 100)
        menu()
        self.s.mainloop()

Pattern().run()
