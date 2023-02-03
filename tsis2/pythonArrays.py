cars = ["Ford", "Volvo", "BMW"]

x = cars[0]
print(x)

cars[0] = "Toyota"
print(cars[0])

x = len(cars)

for i in cars:
  print(i)

cars.append("Honda")
print(cars)

cars.pop(0)

cars.remove("Volvo")
print(cars)