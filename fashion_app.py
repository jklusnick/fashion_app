import random
import string

shoes = [
	'Adidas',
	'Chucks', 
	'white Vans', 
	'black Vans', 
	'khaki Vans', 
	'Nike slides'
	]
socks = [
	'black',
	'white'
	]

pants = [
	'gray',
	'black',
	'green',
	'khaki',
	'jeans'
	]

shorts = [
	'cargo',
	'short',
	'jean'
	]

shirts = [
	'long sleeve',
	'short sleeve'
	]

jacket = [
	'Billabong hoodie',
	'khaki jacket',
	'black raincoat',
	]

if __name__ == "__main__":
	cold = raw_input("Is it cold today Jake? ")
	if cold == "y":
		print "Okay Jake, wear your " + random.choice(shoes) + " with " + random.choice(socks) + \
		" socks, " + random.choice(pants) + " pants, your favorite " + random.choice(shirts) + " shirt, and your " + random.choice(jacket) + "."
	if cold == "n":
		hot = raw_input("Is it hot? ")
		if hot == "y":
			print "Okay Jake, wear your " + random.choice(shoes) + " with " + random.choice(socks) + \
			" socks, " + random.choice(shorts) + " shorts, and a tank top."
		if hot == "n":
			print "Okay Jake, wear your " + random.choice(shoes) + " with " + random.choice(socks) + \
			" socks, " + random.choice(pants) + " pants, and your favorite " + random.choice(shirts) + " shirt."