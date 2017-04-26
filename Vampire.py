from Monster import Monster

class Vampire(Monster):
	def __init__(self):
		super(Vampire, self).__init__("Vampire")
		self.health = 12
		self.power = 5
		# self.name = "Vampire"
		self.xp_value = 10
	
