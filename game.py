print("Welcome to Python Game!")


player = {'player1': { 'name': 'Rai', 'full_hp': 25, 'current_hp': 25, 'full_mana': 20, 'current_mana': 20, 'physical_damage': 2, 'magical_damage': 2, 'armor': .5, 'spell_resist': .5, 'class': ''}}

for i in player.items():
	print(i)