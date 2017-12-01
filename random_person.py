import random

class Person:
	"""GBiT student"""
	def __init__(self, age, name, eye_color, fav_ice_cream):
		self.age = age
		self.name = name
		self.eye_color = eye_color
		self.fav_ice_cream = fav_ice_cream

	def print_person(self):
		print "This person's name is " + self.name + ", " + str(self.age) + " years old, has " + self.eye_color + " eye color, and " + self.fav_ice_cream + " is their favorite flavor of ice cream"
	
	def change_name(self,new_name):
		self.name = new_name

ages = [x for x in range(0, 100)]

names = [
	"Jacob",
	"Adithya",
	"Alejandro",
	"Gillian",
	"Joey",
	"Becky",
	"Benjamin"
]

eye_colors = [
	"blue",
	"green",
	"brown",
	"hazel"
]

fav_ice_creams = [
	"vanilla",
	"chocolate",
	"rocky road",
	"birthday cake",
	"mint chip"
]

name = names[random.randint(0, len(names)-1)]
eye_color = eye_colors[random.randint(0, len(eye_colors)-1)]
fav_ice_cream = fav_ice_creams[random.randint(0, len(fav_ice_creams)-1)]
age = ages[random.randint(0, len(ages)-1)]

las_vegas = Person(age, name, eye_color, fav_ice_cream)
las_vegas.print_person()