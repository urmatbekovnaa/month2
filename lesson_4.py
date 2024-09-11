from random import randint, choice


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        hero = choice(heroes)
        self.__defence = hero.ability

    def attack(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                if type(hero) == Berserk and self.defence != hero.ability:
                    blocked = choice([5, 10])
                    hero.blocked_damage = blocked
                    hero.health -= (self.damage - blocked)
                else:
                    hero.health -= self.damage

    def __str__(self):
        return 'BOSS ' + super().__str__() + f' defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def apply_super_power(self, boss, heroes):
        pass

    def attack(self, boss):
        boss.health -= self.damage


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'CRITICAL_DAMAGE')

    def apply_super_power(self, boss, heroes):
        coefficient = randint(2, 5)
        boss.health -= self.damage * coefficient
        print(f'Warrior {self.name} hit critically {self.damage * coefficient}')


class Magic(Hero):
    def __init__(self, name, health, damage,):
        super().__init__(name, health, damage, 'BOOST')
        self.boost_damege =5

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero != self:
                hero.damage += self.boost_damege
                print(f'Magic {self.name} boosted {hero.name} by {self.boost_damege}. New damage: {hero.damage}')
class Hacker(Hero):
    def __init__(self, name, health, damage, stolen_health):
        super().__init__(name, health, damage, 'LARCENY')
        self.__stolen_health = stolen_health

    # TODO
    def apply_super_power(self, boss, heroes):
        stolen_health = randint(10, 30)
        boss.health -= stolen_health
        self.health += stolen_health
        print(f'Hacker {self.name} stole {stolen_health} health from {boss.name}')



class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'BLOCK_AND_REVERT')
        self.__blocked_damage = 0

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value

    def apply_super_power(self, boss, heroes):
        boss.health -= self.__blocked_damage
        print(f'Berserk {self.name} reverted {self.__blocked_damage} damage.')


class Bomber(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'EXPLODE')
        self.explosion_damage = 100  # Дополнительный урон от взрыва

    def explode(self, boss):
        print(f'Bomber {self.name} взрывается, нанося боссу {self.explosion_damage} урона!')
        boss.health -= self.explosion_damage  # Наносим урон боссу


class Witcher(Hero):
    def __init__(self, name,  health, damage):
        super().__init__( name,  health, damage, 'REVIVAL')
        self.__revival = 0

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health <= 0 and hero != self:
                hero.health = self.health
                self.health = 0
                print(f'Witcher {self.name} revived {hero.name} by sacrificing himself.')


class Spitfire(Hero):
    def __init__(self, name, health, damage,):
        super().__init__(name, health, damage, 'AGGRESSION')
        self.__aggression_damage = 0

    def apply_super_power(self, boss, heroes):
        if any(hero.health <= 0 for hero in heroes if hero != self):
            self.__aggression_damage = min(self.__aggression_damage + 80, 80)
            boss.health -= self.__aggression_damage
            print(f'Spitfire {self.name} showed aggression and dealt {self.__aggression_damage} extra damage!')



class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, 'HEAL')
        self.__heal_points = heal_points


    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and hero != self:
                hero.health += self.__heal_points


round_number = 0


def is_game_over(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
        return True
    return False


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.attack(heroes)
    for hero in heroes:
        if hero.health > 0 and boss.health > 0 and hero.ability != boss.defence:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes)
    show_statistics(boss, heroes)


def show_statistics(boss, heroes):
    print(f'---------- ROUND {round_number} ----------')
    print(boss)
    for hero in heroes:
        print(hero)


def start_game():
    boss = Boss(name='Elena', health=1500, damage=50)

    warrior_1 = Warrior(name='Ahiles', health=280, damage=10)
    warrior_2 = Warrior(name='Helios', health=290, damage=15)
    magic = Magic(name='Potter', health=260, damage=10)
    berserk = Berserk(name='Guts', health=240, damage=5)
    doc = Medic(name='Merlin', health=200, damage=5, heal_points=15)
    assistant = Medic(name='Marin', health=300, damage=5, heal_points=5)
    witcher = Witcher(name='Gon', health=270, damage=0)
    hacker = Hacker(name='Rubi', health=210, damage=5, stolen_health=0)
    spitfire = Spitfire(name='Pedro', health=280, damage=10)
    bomber = Bomber(name='Megan', health=220, damage=5)

    heroes_list = [warrior_1, doc, warrior_2, magic, berserk, assistant, witcher, hacker, spitfire, bomber]

    show_statistics(boss, heroes_list)
    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)

start_game()


