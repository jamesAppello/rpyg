import random as r
from .special import Special
# from .inventory import Item
# import pprint
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Player: #Person / User (like a Darkeden like game (o.s's get me lol))
    def __init__(self, name, hp, mp, atk, df, spec_atk, items):
        self.n = name
        self.max_hp = hp #setting both acts as fort of a health meter like a game online/etc
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.atk_lo = atk -10
        self.atk_hi = atk + 10
        self.df = df
        self.spec_atk = spec_atk
        self.items = items
        self.actions = ["Attack", "Special", "Items"]
    # generate|inflict damage 
    def init_attack(self):
        return r.randrange(self.atk_lo, self.atk_hi)

    # take damage
    def _damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        return self.hp
    
    def heal(self, damage):
        self.hp += damage
        if self.hp > self.max_hp:
            self.hp = self.max_hp 
    
    def get_hp(self):
        return self.hp
    def get_max_hp(self):
        return self.max_hp

    def get_mp(self):
        return self.mp
    def get_max_mp(self):
        return self.max_mp
    
    def mp_reducer(self, cost):
        self.mp -= cost
    

    # choose action
    def slct_action(self):
        i = 1
        print("\n" + bcolors.BOLD + self.n + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "      ACTIONS" + bcolors.ENDC)
        for item in self.actions:
            print("         " + str(i) + ":" + item)
            i += 1
    
    # choose special/Spell/Magic/ETC...
    def slct_atk(self):
        i = 1
        print("\n"+ bcolors.OKBLUE + bcolors.BOLD + "      SPECIALS" + bcolors.ENDC)
        for skill in self.spec_atk:
            print("         " + str(i) + ".", skill.n, "(cost:", str(skill.c) + ")")
            i += 1

    def slct_item(self):
        i = 1
        print("\n" + bcolors.OKGREEN + bcolors.BOLD + "      ITEMS:" + bcolors.ENDC)
        for item in self.items:
            print("         " + str(i) + ". " + item['item'].n, "-", item['item'].d, f" (x{item['quantity']})")
            i += 1

    # SELECT_A_TARGET
    def choose_target(self, enemies):
        i = 1
        print("\n"+bcolors.FAIL+bcolors.BOLD+ "    TARGET: "+bcolors.ENDC)
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print("        "+str(i)+".", enemy.n)
                i +=1
        choice = int(input("    Choose Target: ")) -1
        return choice

    # ENEMY STATS
    def get_enemy_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.max_hp) * 100 / 2
        # 50 instead of 25
        while bar_ticks > 0:
            hp_bar += "\xa4"
            bar_ticks -= 1
        while len(hp_bar) < 50:
            hp_bar += " "
        hp_string = str(self.hp) + "/" + str(self.max_hp)
        current_hp = ""
        if len(hp_string) < 9:
            decreased = 9 - len(hp_string)
            while decreased > 0:
                current_hp += " "
                decreased -= 1
            current_hp += hp_string
        else:
            current_hp = hp_string

        print("                        __________________________________________________ ")
        print(bcolors.BOLD + bcolors.HEADER + self.n +"     "+ 
        current_hp +bcolors.ENDC+" |" +bcolors.FAIL+ hp_bar +bcolors.ENDC+ "|")

    # PLAYER STATS
    def get_player_stats(self):
        bar_hp = ""
        bar_ticks = (self.hp / self.max_hp) * 100 / 4
        bar_mp = ""
        bar_mp_ticks = (self.mp / self.max_mp) * 100 / 10
        # Health Points
        while bar_ticks > 0: 
            bar_hp += "\xa4"
            bar_ticks -= 1
        while len(bar_hp) < 25:
            bar_hp += " "
        # Magic Points
        while bar_mp_ticks > 0:
            bar_mp += "\xa4"
            bar_mp_ticks -= 1
        while len(bar_mp) < 10:
            bar_mp += " "
        
        hp_string = str(self.hp) + "/" + str(self.max_hp)
        current_hp = ""
        if len(hp_string) < 9:
            decreased = 9 - len(hp_string)
            while decreased > 0:
                current_hp += " "
                decreased -= 1
            current_hp += hp_string
        else:
            current_hp = hp_string

        mp_string = str(self.mp) + "/" + str(self.max_mp)
        current_mp = ""
        if len(mp_string) < 7:
            decreased = 7 - len(mp_string)
            while decreased > 0:
                current_mp += " "
                decreased -= 1
            current_mp += mp_string
        else:
            current_mp = mp_string

        print("                           _________________________              ___________ ")
        print(bcolors.BOLD + self.n +"     "+ 
        bcolors.BOLD+ current_hp +" |" +bcolors.OKGREEN+ bar_hp +bcolors.ENDC+ "|    "+
        current_mp + " |"+bcolors.OKBLUE+ bar_mp +bcolors.ENDC +"|")

    def choose_enemy_skill(self):
        skill_choice = r.randrange(0, len(self.spec_atk))
        skill = self.spec_atk[skill_choice]
        skill_dmg = skill._damage()
        pct = (self.hp / self.max_hp) * 100
        if self.mp < skill.c or skill.t == "white" and pct > 50:
            return self.choose_enemy_skill()
        else:
            return skill, skill_dmg