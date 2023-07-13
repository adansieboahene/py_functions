PI = 3.14159

def area_of_circle(radius):
  area = PI * radius ** 2
  return area

radius = float(input("Enter the radius of your circle: "))

area = area_of_circle(radius)

print("The area of the circle is: ", area)