"""
Напишите класс Character обладающий 3 характеристиками: атака, здоровье, уклоенине
FIGHTER = {"health": 5, "attack": 3, "dodge": 1}
THIEF = {"health": 2, "attack": 3, "dodge": 4}
MAGE = {"health": 1, "attack": 5, "dodge": 4}
TYPES = {"fighter": FIGHTER, "thief": THIEF, "mage": MAGE}

Класс имеет следующие методы:
Распределение атрибутов как описано выше: character_1 = Character("fighter")
Атака
Получение урона в случае если увернуться не удалось.
Уклонение: каждое очко уклонения умножается на 5. Результат уклонения зависит от рандомно генерируемого числа
от 0 до 100. Если это число меньше или равно навыка уклонения, то герой уклоняется от атаки.
Смерть: если здоровье меньше 1.

Напишите функцию которая заставит сразиться разных героев друг с другом 100 раз. Выведите счет.
"""
from Character.Character import Character
import random

"""character_1 = Character("fighter")
character_2 = Character("thief")
character_3 = Character("mage")
"""
"""def battle(character_1,character_2):
    character_1_wins = 0
    character_2_wins = 0
    character_3_wins = 0
    while True:
        if character_1._is_dead == False and character_2._is_dead ==False:
        character_1.take_damage(character_2.attack)"""


def character_fight(type1, type2):
    character_1 = Character(type1)
    character_2 = Character(type2)
    coin_toss = random.randint(0, 1)
    if coin_toss == 0:
        first, second = [character_1, character_2]
    else:
        first, second = [character_2, character_1]

    while True:
        if attack_character(first, second):
            return str(first)
        if attack_character(second, first):
            return str(second)

def attack_character(first, second):
    damage = first.attack()
    second.take_damage(damage)
    if second._is_dead():
        return True
    return False

def main():
    char_1 = "thief"
    char_2 = "fighter"
    char_1_win = 0
    char_2_win = 0
    for _ in range(100):
        winner = character_fight(char_1, char_2)
        if winner==char_1:
            char_1_win += 1
        else:
            char_2_win += 1
    print("Results: ")
    print(f"{char_1}: {char_1_win}")
    print(f"{char_2}: {char_2_win}")

if __name__ == "__main__":
    main()