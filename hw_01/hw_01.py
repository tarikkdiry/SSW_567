#Classifies triangle based on side lengths
triangle = ""
side_list = []

def classify_triangle(a, b, c):

    side_list = [a, b, c]
    side_count = []
    count = 0
    a = side_list[0]
    b = side_list[1]
    c = side_list[2]

    for x in range(len(side_list)):
        for y in range(len(side_list)):
            if (side_list[x] == side_list[y]):
                count += 1
        side_count.append(count)
        count = 0

    if ((a**2) + (b**2) == (c**2)):
        triangle = "right"
    elif (a <= 0 or b <= 0 or c <= 0):
        triangle = "NotATriangle"
    else:
        if (max(side_count) == 1):
            triangle = "scalene"
        elif (max(side_count) == 2):
            triangle = "isosceles"
        else:
            triangle = "equilateral"
          
    return triangle


print("The triangle is a " + classify_triangle(-1,4,5) + " triangle.")
