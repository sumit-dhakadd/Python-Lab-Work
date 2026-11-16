
import turtle

class PatternGenerator:

    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Interactive Turtle Fractal Renderer")
        self.screen.bgcolor("black")
        self.screen.setup(800, 700)

        self.t = turtle.Turtle()
        self.t.speed(0)
        self.palette = ["red", "yellow", "cyan", "green", "magenta"]

    def draw_spiral(self):
        self.t.clear()
        for n in range(100):
            self.t.pencolor(self.palette[n % 5])
            self.t.forward(n * 3)
            self.t.right(91)

    def draw_polygon(self):
        self.t.clear()
        sides = int(self.screen.numinput("Polygon", "Enter sides:", 6))
        for n in range(sides):
            self.t.pencolor(self.palette[n % 5])
            self.t.forward(100)
            self.t.right(360 / sides)

    def draw_fractal(self, size, depth):
        if depth <= 0:
            self.t.forward(size)
        else:
            size /= 3
            self.draw_fractal(size, depth - 1)
            self.t.left(60)
            self.draw_fractal(size, depth - 1)
            self.t.right(120)
            self.draw_fractal(size, depth - 1)
            self.t.left(60)
            self.draw_fractal(size, depth - 1)

    def draw_koch(self):
        self.t.clear()
        self.t.penup()
        self.t.goto(-200, 100)
        self.t.pendown()
        self.t.pencolor("cyan")
        self.draw_fractal(400, 4)

    def draw_flower(self):
        self.t.clear()
        for n in range(36):
            self.t.pencolor(self.palette[n % 5])
            self.t.circle(100)
            self.t.left(10)

    def run(self):
        options = {
            "1": self.draw_spiral,
            "2": self.draw_polygon,
            "3": self.draw_koch,
            "4": self.draw_flower
        }

        def select_pattern():
            choice = self.screen.textinput(
                "Turtle Generator",
                "1. Spiral\n2. Polygon\n3. Koch Fractal\n4. Flower\nEnter choice:"
            )

            if choice in options:
                options[choice]()
            else:
                print("Invalid choice!")

            self.screen.ontimer(select_pattern, 100)

        select_pattern()
        self.screen.mainloop()


app = PatternGenerator()
app.run()
