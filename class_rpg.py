from Hero import Hero
from Monster import Goblin
from Monster import Hobgoblin
from Vampire import Vampire
from Yeti import Yeti
import random

# Ask the user for the hero's name
print ("What is your name, brave adventurer?")
hero_name = raw_input("> ")
the_hero = Hero(hero_name)
monster_types = ["hobgoblin", "vampire", "goblin", "yeti"]
monsters = []

print "How many monsters are you willing to fight?"
number_of_enemies = int(raw_input("> "))

for i in range(0, number_of_enemies):
	rand_num = random.randint(0,len(monster_types)-1)
	if(monster_types[rand_num] == "hobgoblin"):
		monsters.append(Hobgoblin())
	elif(monster_types[rand_num] == "vampire"):
		monsters.append(Vampire())
	elif(monster_types[rand_num] == "goblin"):
		monsters.append(Goblin())
	elif(monster_types[rand_num] == "yeti"):
		monsters.append(Yeti())

while len(monsters) > 0:

	for monster in monsters:
		print "Brave %s, you have encountered a %s!" % (the_hero.name, monster.name)
	# Run game as long as BOTH cahracters have health
		while monster.health > 0 and the_hero.is_alive():
	 		print "You have %d health and %d power." % (the_hero.health, the_hero.power)
	 		print "The %s has %d health and %d power." % (monster.name, monster.health, monster.power)
	 		print "What do you want to do?"
	 		print "1. fight %s" % (monster.name)
	 		print "2. do nothing"
	 		print "3. flee"
	 		print "4. Drink potion of life"
	 		print "> ",
	 		user_input = raw_input()
	 		
	 		if (user_input == "1"):
	 				# Hero is going to attack
	 			# the_goblin.health -= the_hero.power
	 			# the_hero.attack(the_goblin)			#All 3 of these attributes do the same thing 
	 			monster.take_damage(the_hero.power) 
	 			print "You have done %d damage to the %s" % (the_hero.power, monster.name)
	 			if monster.health <= 0:
	 				print "You have defeated the %s!" % (monster.name)	
	 				del monsters[monsters.index(monster)]
	 				the_hero.xp += monster.xp_value
	 				the_hero.check_level()	
	 		elif user_input == "2":
	 				# Hero is going to do nothing
	 			pass # <-- means do nothing, but acts as a space filler for indentation requirements		
			elif user_input == "3":
				print "Goodbye, coward"
				break
			elif user_input == "4":
				the_hero.health += 20
			else:
				print "Invalid input %s" % (user_input)
			if	 monster.health > 0:
					# hero has attacked (or not) AND goblin is still alive
				the_hero.health -= monster.power
				print "The %s hits you for %d damage" % (monster.name, monster.power)
				if the_hero.health <= 0:
					print "You have been killed by the %s! Some Hero...\nGoodbye %s." % (monster.name, the_hero.name)
					exit()
			if	 the_hero.health > 0 and the_hero.health < 5:
				print "You have gone into a rage. Your power has increased!"
				the_hero.cheer_hero()			
				the_hero.power += 5
print "You have saved us all %s! \nYou are a real Hero!" % the_hero.name



