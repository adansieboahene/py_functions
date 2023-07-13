def is_triangle(a, b, c):
    if a > b + c or b > a + c or c > a + b:
        return False
    else:
        return True

def main():
    a = int(input("Enter the length of one sticl: "))
    b = int(input("Enter the length of another stick: "))
    c = int(input("Enter the length of the third stick: "))

    if is_triangle(a, b, c):
        print("These sticks can form a triangle.")
    else:
        print("These sticks cannot form a triangle.")
