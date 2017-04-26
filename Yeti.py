class Yeti(object):
	def __init__(self):
		self.health = 12 
		self.power = 8
		self.xp_value = 15
		self.name = "Yeti"

	def take_damage(self, damage):
		self.health -= damage
	
	def is_alive(self):
		return self.health > 0