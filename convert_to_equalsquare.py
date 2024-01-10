def equal_square(a, b):
    if b!=0 :
        return equal_square(b, a % b)
    return a

def convert_to_equalsquare(width, height):
    
    # Calculate the side length of the largest square that fits in the rectangle
    side_length = equal_square(width,height)
    
    # Calculate the number of squares along the width and height
    squares_width = width // side_length
    squares_height = height // side_length
    
    # Calculate total number of squares
    total_squares = squares_width * squares_height
    
    return total_squares

# Given dimensions of the rectangle
rectangle_width = int(input("enter length - "))
rectangle_height = int(input("enter height - "))

# Calculate the number of squares that can be formed
num_squares = convert_to_equalsquare(rectangle_width, rectangle_height)

print(f"The number of squares that can be formed from a {rectangle_width}x{rectangle_height} rectangle is: {num_squares}")
