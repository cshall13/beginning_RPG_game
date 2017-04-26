
class Monster(object):
	def __init__(self, name, health = 10):
		self.name = name
		self.health = health
		self.power = 10
		
	def take_damage(self, damage):
		self.health -= damage
	
	def is_alive(self):
		return self.health > 0

class Goblin(Monster):
	def __init__(self):
		super(Goblin, self).__init__("Goblin", 16)  # <--- 16 is health,passed down from monster parameter
		self.power = 2
		self.xp_value = 5

class Hobgoblin(Goblin):
	def __init__(self):
		super(Hobgoblin, self).__init__("Hobgoblin")
		self.power = 3
		# self.name = "Hobgoblin"