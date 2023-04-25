import random
FIGHTER = {"health": 5, "attack": 3, "dodge": 1}
THIEF = {"health": 2, "attack": 3, "dodge": 4}
MAGE = {"health": 1, "attack": 5, "dodge": 4}
TYPES = {"fighter": FIGHTER, "thief": THIEF, "mage": MAGE}

class Character():

    _health = 0
    _attack = 0
    _dodge = 0

    def __init__(self, char_type):
        self._char_type = char_type
        self._assign_attributes()

    def __str__(self):
        return self._char_type

    def _assign_attributes(self):
        types_dict = TYPES[self._char_type]
        self._health = types_dict['health']
        self._attack = types_dict['attack']
        self._dodge = types_dict['dodge']
    def attack(self):
        return self._attack

    def take_damage(self, damage):
        if self._dodge_success():
            return "Missed"
        self._health -= damage
        return f"{self._char_type} took {damage} damage"
    def _dodge_success(self):
        dodge_chance = self._dodge * 5
        dodge_roll = random.randint(1, 100)
        if dodge_roll <= dodge_chance:
            return True
        else:
            return False
    def _is_dead(self):
        if self._health < 1:
            return True
        else:
            return False

