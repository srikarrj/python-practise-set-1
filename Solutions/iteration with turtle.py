import turtle

# Set up the graphics window
wn = turtle.Screen()
wn.setup(500, 500)

# Create a turtle named alex
alex = turtle.Turtle()
alex.speed(500)  # Set the drawing speed to a moderate pace
alex.width(200)  # Set the pen width

# Function to draw a ring pattern
def draw_ring_pattern(t, radius, num_rings, spacing, color):
    t.color(color)
    for _ in range(num_rings):
        t.circle(radius)
        t.penup()
        t.right(90)
        t.forward(spacing)
        t.left(90)
        t.pendown()
        radius += spacing

# Step 1: Draw the first set of rings in red
alex.penup()
alex.goto(0, 0)
alex.pendown()
draw_ring_pattern(alex, 20, 5, 20, "red")

# Step 2: Move to the second position and draw the green rings
alex.penup()
alex.goto(-50, -50)
alex.pendown()
draw_ring_pattern(alex, 20, 5, 20, "green")

# Step 3: Move to the third position and draw the blue rings
alex.penup()
alex.goto(50, -50)
alex.pendown()
draw_ring_pattern(alex, 20, 5, 20, "blue")

# Hide the turtle and display the window
alex.hideturtle()
wn.mainloop()
