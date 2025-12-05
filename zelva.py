import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Krásné ornamenty")
screen.setup(width=800, height=600)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Funkce pro kreslení ornamentů

def draw_spiral_flower(x, y, color1, color2):
    """Kreslí spirálový květ"""
    t.penup()
    t.goto(x, y)
    t.pendown()
    for i in range(36):
        t.color(color1 if i % 2 == 0 else color2)
        t.circle(100, 60)
        t.left(10)

def draw_star(x, y, size, color, points=5):
    """Kreslí hvězdu"""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    angle = 180 - (180 / points)
    for _ in range(points):
        t.forward(size)
        t.right(angle)
    t.end_fill()

def draw_mandala(x, y, radius, color):
    """Kreslí mandalu"""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    for i in range(36):
        t.circle(radius)
        t.left(10)

def draw_geometric_pattern(x, y, size):
    """Kreslí geometrický vzor"""
    t.penup()
    t.goto(x, y)
    t.pendown()
    colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple", "magenta"]
    for i in range(36):
        t.color(colors[i % len(colors)])
        t.forward(size)
        t.right(170)

def draw_hexagon_spiral(x, y):
    """Kreslí spirálu šestiúhelníků"""
    t.penup()
    t.goto(x, y)
    t.pendown()
    colors = ["#FF00FF", "#00FFFF", "#FFFF00", "#FF6600", "#00FF00", "#0066FF"]
    for i in range(60):
        t.color(colors[i % len(colors)])
        t.forward(i * 3)
        t.right(59)

def draw_rainbow_circles(x, y):
    """Kreslí duhové kruhy"""
    t.penup()
    t.goto(x, y)
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    radius = 10
    for i in range(15):
        t.color(colors[i % len(colors)])
        t.pendown()
        t.circle(radius)
        t.penup()
        radius += 5

# Kreslení ornamentů
print("🎨 Kreslím ornamenty...")

# Mandala v prostředku
t.width(2)
draw_mandala(0, -100, 50, "cyan")

# Spirálový květ
draw_spiral_flower(-200, 0, "magenta", "yellow")

# Hvězdy v rozích
draw_star(-300, 200, 60, "gold", 5)
draw_star(250, 200, 50, "lime", 7)
draw_star(-300, -250, 55, "red", 6)
draw_star(250, -250, 50, "purple", 8)

# Geometrický vzor
draw_geometric_pattern(150, 0, 100)

# Hexagonální spirála
draw_hexagon_spiral(-150, -50)

# Duhové kruhy
draw_rainbow_circles(200, -100)

print("✅ Ornamenty dokončeny!")
print("Klikněte na okno pro zavření...")

screen.exitonclick()