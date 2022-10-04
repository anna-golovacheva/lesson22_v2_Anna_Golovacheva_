# в задании представлен один класс который нужно разбить на 4
# Воин      - Warrior
# Лекарь    - Healer
# Дерево    - Tree
# Ловушка   - Trap

# Воин в состоянии защищаться от врагов, атаковать и передвигаться по полю
# Лекарь может защищаться, лечить воина и панически спасаться бегством
# Дерево может защищаться (попробуй разруби сходу) и гореть в огне
# Ловушка не может ничего кроме как атаковать того, кто на нее наступит
# Для решения этой задачи не используйте наследование

#РЕШЕНИЕ:


class Warrior:
    def defense(self):
        print('Воин поднимает щит.')

    def attack(self):
        print('Воин наносит удар.')

    def move(self):
        print('Воин сотрясает землю.')

class Healer:
    def healer_defense(self):
        print('Лекарь прячется за аптечкой.')

    def heal(self):
        print('Лекарь исцеляет воина.')

    def healer_move(self):
        print('Лекарь ползет.')


class Tree:
    def tree_defense(self):
        print('Дерево стойко держит удар.')

    def on_fire(self):
        print('Дерево нестойко горит.')

class Trap:
    def trap_attack(self):
        print("It's a trap!")


if __name__ == '__main__':
    unit = Warrior()
    healer = Healer()
    trap = Trap()