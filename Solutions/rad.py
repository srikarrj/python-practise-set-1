import turtle # allows us to use the turtles library

# Create a graphics window
wn = turtle.Screen()
wn.setup(400, 400) # Set window dimensions

# Set the dimensions
circle_rad = 60 # Radius of the circle
rectangle_width = 4 * circle_rad # Width of the rectangle (4 times the radius)
rectangle_height = circle_rad / 2 # Height of the rectangle (1/2 of the radius)

# Create a turtle named alex
alex = turtle.Turtle()
alex.shape("turtle") # Set shape to turtle
alex.color('blue') # Set color to red

# Draw the circle
alex.circle(circle_rad)

# Position alex to start drawing the rectangle
alex.penup() # Lift the pen to avoid drawing lines
alex.goto(-rectangle_width / 2, -circle_rad) # Move to starting position
alex.pendown() # Lower the pen to start drawing

# Draw the rectangle
alex.forward(rectangle_width) # Draw the bottom side
alex.right(90) # Turn right 90 degrees
alex.forward(rectangle_height) # Draw the right side
alex.right(90) # Turn right 90 degrees
alex.forward(rectangle_width) # Draw the top side
alex.right(90) # Turn right 90 degrees
alex.forward(rectangle_height) # Draw the left side

# Close the window when clicked
wn.exitonclick()
