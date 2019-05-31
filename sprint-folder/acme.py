'''Product class'''
from random import randint


class Product:
    '''Describes a product

    Parameters
    -----------------------------
    name : str
        name of product
    price : int
        price of product
    weight : int
        weight of product
    flammability : float
        products tendency toward burning
    identifier : integer
        unique product number
    '''
    def __init__(self, name, price=10, weight=20,
                 flammability=0.5, identifier=randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        '''Tells you how stealable this product is'''
        score = self.price/self.weight
        if score < .5:
            return 'Not so stealable...'
        elif score >= .5 and score < 1.0:
            return 'Kinda stealable'
        else:
            return 'Very stealable!'

    def explode(self):
        '''Tells you how likely this product will explode'''
        score = self.flammability*self.weight
        if score < 10:
            return '...fizzle.'
        elif score >= 10 and score < 50:
            return '...boom!'
        else:
            return '...BABOOM!!'


class BoxingGlove(Product):
    '''This covers your hand and you hit people with it'''
    def __init__(self, name, price=10, weight=10,
                 flammability=0.5, identifier=randint(1000000, 9999999)):
        super().__init__(name=name, price=price,
                         flammability=flammability, identifier=identifier)
        self.weight = weight

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return 'That tickles!'
        elif self.weight >= 5 and self.weight < 15:
            return 'Hey that hurt!'
        else:
            return 'OUCH!'  # add wilhelm scream
