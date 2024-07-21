import math
pi = math.pi
# print(round(pi))
# print(abs(pi))

slicing = "from that to that"
# print(slicing[0:5])

website1 = "http://www.python.org"
website2 = "http://www.google.org"

me = slice(11,-4)
print(website1[me])
# li = [website1, website2]
# print(type(li))
# print()

age = int(input("Enter your age: "))
if age >= 18:
    print("You are a adult.")
elif age < 18:
    print("You are a child.")
else:
    print("You are a t.")

temp = int(input("Enter a temp: "))
if temp >= 0 and temp <= 10:
    print("temp is between 0 and 10")
elif temp >= 10 and temp <= 20:
    print("temp is not between 10 and 20")
elif temp >= 20 and temp <= 30:
    print("temp is bet than 20 and 30")
else:
    print("temp is gret than 30")
