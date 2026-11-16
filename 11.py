
import turtle

class PatternGenerator:
    def __init__(self):
        self.s = turtle.Screen()
        self.s.title("Turtle Pattern Generator")
        self.s.bgcolor("black")
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.colors = ["red", "yellow", "cyan", "green", "magenta"]

    def spiral(self):
        for i in range(100):
            self.t.color(self.colors[i % 5])
            self.t.forward(i * 3)
            self.t.right(91)

    def polygon(self):
        n = int(self.s.numinput("Polygon", "Enter sides:", 6))
        for i in range(n):
            self.t.color(self.colors[i % 5])
            self.t.forward(100)
            self.t.right(360 / n)

    def fractal(self, size, depth):
        if depth == 0:
            self.t.forward(size)
        else:
            for angle in [0, 60, -120, 60]:
                self.fractal(size / 3, depth - 1)
                self.t.left(angle)

    def koch(self):
        self.t.penup()
        self.t.goto(-200, 100)
        self.t.pendown()
        self.t.color("cyan")
        self.fractal(400, 4)

    def flower(self):
        for i in range(36):
            self.t.color(self.colors[i % 5])
            self.t.circle(100)
            self.t.left(10)

    def run(self):
        options = {
            "1": self.spiral,
            "2": self.polygon,
            "3": self.koch,
            "4": self.flower
        }

        def menu():
            self.t.clear()
            ch = self.s.textinput(
                "Pattern Generator",
                "1.Spiral\n2.Polygon\n3.Koch Fractal\n4.Flower"
            )
            if ch in options:
                options[ch]()
            else:
                print("Invalid choice!")
            self.s.ontimer(menu, 100)

        menu()
        self.s.mainloop()


PatternGenerator().run()
