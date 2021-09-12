def classify_triangle(a, b, c):
    if(a == b == c):
        print("This is an equilateral triangle.");

    elif(a == b or a == c or b == c):
        print("This is an isosceles triangle.");

    else:
        print("This is an scalene triangle.");

    if(a**2 + b**2 == c**2):
        print("This is also a right triangle.");

def main():
    #print();
    a = int(input("Enter the length of your first side:"));
    b = int(input("Enter the length of your second side:"));
    c = int(input("Enter the length of your third side:"));
    classify_triangle(a, b, c);

main();