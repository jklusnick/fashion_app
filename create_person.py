class Person:
	"""GBiT student"""
	def __init__(self, age, name, eye_color, fav_ice_cream):
		self.age = age
		self.name = name
		self.eye_color = eye_color
		self.fav_ice_cream = fav_ice_cream

	def print_person(self):
		print "This person's name is " + self.name + ", " + str(self.age) + " years old, has " + self.eye_color + " eye color, and " + self.fav_ice_cream + " is his favorite flavor of ice cream"
	
	def change_name(self,new_name):
		self.name = new_name


jake = Person(17, "Jake", "brown", "chocolate chip cookie dough")
jake.print_person()
jake.change_name("Jacob")
jake.print_person()
