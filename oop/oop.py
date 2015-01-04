class Animal:
	def __init__(self, name, color, age, gender):
		self.name=name
		self.color=color
		self.age=age
		self.gender=gender
	def print_all(self):
		print(self.name)
		print(self.color)
		print(self.age)
		print(self.gender)


Dinosaur=Animal(name="internet_explorer", color="light blue", age=10000000000003, gender="female")


cat=Animal(name="Fluffy", color="green", age=20, gender="not_defined")

Dinosaur.print_all()
print("#############")
cat.print_all()
