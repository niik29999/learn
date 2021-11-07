from random import choice

def square(x):
    return x * x


def greet(name, isEnemy):
    if not isinstance(isEnemy, bool):
        raise ValueError('isEnemy must be a boolean type')
    if isEnemy:
        return f'Hello {name}! I will kill you, bastard!'
    else:
        return f'Hello {name}! How are you?'


def eat_burgers(number):
    if number > 3:
        return f'Oh! I overate!'
    else:
        return f'Mmm! That was excellent!'


def can_fly(name):
    if name == 'Batman':
        return True
    else:
        return False


def get_arsenal():
    return choice(('knife', 'handgun', 'machine gun'))


class Shooter:
    def __init__(self, name, money = 1000, guns = []):
        self.name = name
        self.money = money
        self.guns = guns

    def get_cash(self, cash):
        self.money = self.money + cash
        if cash > 1000:
            return 'Let\'s go to the party!'
        else:
            return 'Let\'s go for more money!'

    def greet(self):
        if self.money > 100:
            return 'Hello! How are you?'
        else:
            return 'Hello! I need cash!'

    def buy_gun(self, new_gun, gun_cost):
        if self.money >= gun_cost:
            self.money -= gun_cost
            self.guns.append(new_gun)
            return 'Wow! Cool stuff!'
        else:
            return 'Sorry:( I have no money for this toy.'