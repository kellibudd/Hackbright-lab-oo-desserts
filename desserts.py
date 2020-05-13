"""Dessert classes."""


class Cupcake:
    """A cupcake."""
    
    cache = {}

    def __repr__(self):
        """Human-readable printout for debugging."""
        
        return f'<Cupcake name="{self.name}" qty={self.qty}>'

    def __init__(self, name, flavor, price):
        """Creating class instance"""

        self.name = name
        self.flavor = flavor
        self.price = price
        self.qty = 0
        cls.cache[self.name] = cls.cache.get(self.name, f'<Cupcake name="{self.name}" qty={self.qty}>')

    @classmethod
    def get(cls, name):

        if name in cls.cache:
          return name, cls.cache[name]
        else:
          print("Sorry, that cupcake doesn't exist")

    def add_stock(self, amount):
        
        self.qty = self.qty + amount

    def sell(self, amount):

        if self.qty == 0:
          print('Sorry, these cupcakes are sold out')

        elif amount > self.qty:
          self.qty = 0

        else:
          self.qty = self.qty - amount

    @staticmethod
    def scale_recipe(ingredients, amount):

        for ingredient in ingredients:
          print(ingredient)
          print(ingredient[0])
          print(ingredient[1])
          ingredient = (ingredient[0], ingredient[1] * amount)
          ingredients.append(ingredient)
          print(ingredients)

        return ingredients


if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
