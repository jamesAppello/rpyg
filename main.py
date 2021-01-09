from classes.game import Player
from classes.game import bcolors
from classes.special import Special
from classes.inventory import Item
import random as r
# 14 = 100%
# print(bcolors.HEADER+"\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"+bcolors.ENDC)
# print("NAME              HP                       MP")
# print("                  ______________           ___________________  ")
# print(bcolors.BOLD+ "VALUES:  460/460 |"+bcolors.OKGREEN+"\xe2\xe2\xe2\xe2\xe2\xe2\xe2\xe2\xe2\xe2\xe2\xe2\xe2\xe2     "+bcolors.ENDC+"    "+
# "65/65 |"+bcolors.OKBLUE+"\xe2\xe2\xe2\xe2\xe2\xe2\xe2\xe5\xe2\xe2\xe2\xe2\xe2\xe2     "+bcolors.HEADER+"    ")
# print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"+bcolors.ENDC)


# attacks/skills
fire = Special("F1r3", 25, 250, "black")
lightning = Special("L1ghtn1ng", 25, 301, "black")
judokick = Special("Jud0K1ck", 25, 175, "black")
frostbite = Special("Fr0stByte", 40, 313, "black")
meteor = Special("M3t30r", 26, 405, "black")
# healing
cure = Special("Cur3", 25, 120, "white")
cure_a1 = Special("Cur3_AE", 32, 194, "white")
cure_a2 = Special("Cur3_AE2", 50, 6000, 'white')

# Create Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hi_potion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
super_potion = Item("Super-Potion", "potion", "Heals 500 HP", 500)
elixr = Item("Elixr", "elixr", "Full HP/MP restore", 9999)
mega_elixr = Item("Mega-Elixr", "MegaElixr", "Fully restores party's HP/MP", 9999)
grenade = Item('Grenade', 'attack', "Deals 500 damage", 500)

# Set player prop:key-value pair
player_skills = [fire, lightning, judokick, frostbite, meteor, cure, cure_a1]
player_items = [
    {"item": potion, "quantity": 15},
    {"item": hi_potion, "quantity": 5},
    {"item": super_potion, "quantity": 5},
    {"item": elixr, "quantity": 5},
    {"item": mega_elixr, "quantity": 2},
    {"item": grenade, "quantity": 12},
]
enemy_skills = [fire, meteor, lightning, cure_a2]
# enemy_items = []

# Instantiate [Player]
p1 = Player("[Str1kR](1)", 1460, 232, 303, 34, player_skills, player_items)
p2 = Player("[V4lc0n](2)", 2700, 288, 311, 25, player_skills,  player_items)
p3 = Player("[RyptR](3)", 1635, 274, 268, 30, player_skills,  player_items)

# instantiate [Player] => [Enemy]
enemy1 = Player("<D1ngu$>", 772, 142, 482, 325, enemy_skills, [])
enemy2 = Player("<M4v3rK>", 6085, 650, 525, 25, enemy_skills, []) # CLI_UI looks better with the main enemy in middle
enemy3 = Player("<M1n10n>", 1772, 142, 482, 325, enemy_skills, [])
# PLAYERS_ARRAY
_PLAYERS = [p1, p2, p3]
_ENEMIES = [enemy1, enemy2, enemy3]

running = True
i = 0
print(bcolors.WARNING+"\n\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\xa4\n"+bcolors.ENDC)
# print(bcolors.FAIL + bcolors.BOLD + f"{enemy.n} ATTACKS!!!!" + bcolors.ENDC)

# GAME_START
while running:
    print(bcolors.WARNING+"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"+bcolors.ENDC)
    print(bcolors.BOLD + bcolors.HEADER + "NAME                     HP                                MP"+bcolors.ENDC)
    
    for player in _PLAYERS: # LOOP TO PRINT OUT STATS
        player.get_player_stats()
    print("\n")
    for enemy in _ENEMIES:
        enemy.get_enemy_stats()
    print(bcolors.WARNING+"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"+bcolors.ENDC)
    
    for player in _PLAYERS: # LOOP TO PRINT OUT ACTIONS >> GAME
        player.slct_action()
        choice = input("    Choose an action...\n")
        idx = int(choice) - 1

        if idx == 0:
            dmg = player.init_attack()
            enemy = player.choose_target(_ENEMIES)
            _ENEMIES[enemy]._damage(dmg)
            print(player.n+"attacked"+ _ENEMIES[enemy].n.replace(" ", "")+" for", dmg, "damage points!")
            
            if _ENEMIES[enemy].get_hp() == 0:
                print(bcolors.BOLD+bcolors.OKGREEN+ _ENEMIES[enemy].n.replace(" ", "") + " was defeated!")
                del _ENEMIES[enemy]
        
        elif idx == 1:
            player.slct_atk()
            skill_choice = int(input("      Choose a skill...\n")) - 1
            
            if skill_choice == -1:
                continue
            skill = player.spec_atk[skill_choice]
            skill_dmg = player.init_attack()
            current_mp = player.get_mp()
            
            if skill.c > current_mp:
                print(bcolors.FAIL + "\nInsufficient MP\n" + bcolors.ENDC)
                continue
            player.mp_reducer(skill.c)
            
            if skill.t == "white":
                player.heal(skill_dmg)
                print(bcolors.OKBLUE + "\n" + skill.n + " heals for", str(skill_dmg), "HP!" + bcolors.ENDC)
            
            elif skill.t == 'black':
                enemy = player.choose_target(_ENEMIES)
                _ENEMIES[enemy]._damage(skill_dmg)
                print(bcolors.OKBLUE + "\n" + skill.n + " inflicts", str(skill_dmg), "points of damage to "+ _ENEMIES[enemy].n.replace(" ", "") + bcolors.ENDC)
                
                if _ENEMIES[enemy].get_hp() == 0:
                    print(bcolors.BOLD+bcolors.OKGREEN+ _ENEMIES[enemy].n.replace(" ", "") + " was defeated!")
                    del _ENEMIES[enemy]

        elif idx == 2:
            player.slct_item()
            item_choice = int(input("       Choose an Item: ")) - 1
            
            if item_choice == -1:
                continue
            
            item = player.items[item_choice]['item']
            
            if player.items[item_choice]['quantity'] == 0:
                print(bcolors.FAIL + '\n' + item.n + " DEPLETED..." + bcolors.ENDC)
                continue
            
            player.items[item_choice]['quantity'] -= 1
            
            if item.t == 'potion':
                player.heal(item.p)
                print(bcolors.OKGREEN + '\n' + item.n + " heals for", str(item.p), "HP" + bcolors.ENDC)
            
            elif item.t == 'elixr':
                if item.t == 'MegaElixr':
                    for i in _PLAYERS:
                        i.hp = i.max_hp
                        i.mp = i.max_mp
                else:
                    player.hp = player.max_hp
                    player.mp = player.max_mp
                print(bcolors.OKGREEN + '\n' + item.n + " fully restores HP/MP" + bcolors.ENDC)
            
            elif item.t == 'attack':
                enemy = player.choose_target(_ENEMIES)
                _ENEMIES[enemy]._damage(item.p)
                print(bcolors.FAIL + '\n' + item.n + " deals", str(item.p), "HP damage points to "+ _ENEMIES[enemy].n + bcolors.ENDC)
                
                if _ENEMIES[enemy].get_hp() == 0:
                    print(bcolors.BOLD+bcolors.OKGREEN+ _ENEMIES[enemy].n.replace(" ", "") + " was defeated!"+bcolors.ENDC)
                    del _ENEMIES[enemy]
        elif idx == 603 or idx == 604:
            print(bcolors.OKGREEN + "PLAYER TEAM WINS!" + bcolors.ENDC)
            running = False
    # check if battle is still commencing
    defeated_players = 0
    defeated_enemies = 0
    for player in _PLAYERS:
        if player.get_hp() == 0:
            defeated_players += 1
    
    for enemy in _ENEMIES:
        if enemy.get_hp() == 0:
            defeated_enemies += 1
    
    # check if player won
    if defeated_enemies == 2:
        print(bcolors.OKGREEN + "PLAYER TEAM WINS!" + bcolors.ENDC)
        running = False
    
    # check if enemy won
    if defeated_players == 2:
        print(bcolors.FAIL + f"ENEMY TEAM WINS! YOU LOSE!" + bcolors.ENDC)
        running = False
    print("\n")
    # enemy attack code
    # need to randomly decide which player that the enemy attacks
    for enemy in _ENEMIES:    
        enemy_choice = r.randrange(0, 3)
        
        if enemy_choice == 0:
            # attack choice
            target = r.randrange(0, 3)
            enemy_dmg = enemy.init_attack()
            _PLAYERS[target]._damage(enemy_dmg)
            print(enemy.n.replace(" ","")+" attacks "+ _PLAYERS[target].n.replace(" ", "") +" for "+ str(enemy_dmg))
        
        elif enemy_choice == 1:
            skill, skill_dmg = enemy.choose_enemy_skill()
            enemy.mp_reducer(skill.c)
            
            if skill.t == "white":
                enemy.heal(skill_dmg)
                print(bcolors.OKBLUE + skill.n + " heals "+ enemy.n +" for", str(skill_dmg), "HP!" + bcolors.ENDC)
            
            elif skill.t == 'black':
                target = r.randrange(0, 3)
                _PLAYERS[target]._damage(skill_dmg)
                print(bcolors.OKBLUE + "\n"+ enemy.n.replace(" ", "") +"'s " + skill.n + " inflicts", str(skill_dmg), "points of damage to "+ _PLAYERS[target].n.replace(" ", "") + bcolors.ENDC)
                if _PLAYERS[target].get_hp() == 0:
                    print(bcolors.WARNING+ _PLAYERS[target].n.replace(" ", "") + " was defeated!"+bcolors.ENDC)
                    del _PLAYERS[target]

