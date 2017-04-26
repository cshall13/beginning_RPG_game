class Hero(object):
	def __init__(self, name = "Incognito"):
		self.name = name
		self.health = 10
		self.max_health = self.health
		self.power = 5
		self.xp = 0
		self.level = 1

	def check_level(self):
		if self.xp > 3:
			self.level = 2
			self.level_up()

	def level_up(self):
		print "Thou hast leveled up %s! Thy hp is  now %d and thy power is now %d" % (self.name, self.max_health, self.power)
		self.health = self.max_health
		self.power += 2

	def cheer_hero(self):
		print "Fight hard, %s!" % self.name

	# this class method returns a boolean. True, if the hero is alive false if the hero is dead 
	def is_alive(self):
		return self.health > 0 #same as if statement below
		# if self.health > 0:
		# 	return True
		# else: 
		# 	return False

	def attack(self, who_to_attack):
		who_to_attack.health -= self.power
	
	def increase_health(self, amount):
		self.health += amount
		if self.health > self.max_health:
			self.health = self.max_health