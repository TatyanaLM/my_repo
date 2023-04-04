import random

NumsList = ['Джокер', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', "Дама", "Король", "Туз"]
MastList = ["пик", "крестей", "бубей", "червей"]

class Card():
    #NumsList = ['Джокер', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', "Дама", "Король", "Туз"]
    #MastList = ["пик", "крестей", "бубей", "червей"]

    def __init__(self, num, mast="none"):
        self.num = num
        self.mast = mast
        #self._assign_attributes()

'''    def _assign_attributes(self, num, mast):
        if NumsList[num]:
            self.num = num
        num_dict = NumsList[self.num]
        mast_dict = NumsList[self.mast]
        self.num = num_dict[
        self.mast = mast_dict['attack']'''

class DeckofCards():

    def __init__(self):
        self.deck = []
        for current_num in NumsList:
            if current_num == "Джокер":
                pass
            else:
                for current_mast in MastList:
                    current_cart = Card(current_num, current_mast)
                    self.deck.append(current_cart)
        self.deck.append(Card("Джокер"))
        self.deck.append(Card("Джокер"))

    def shuffle(self):
        random.shuffle(self.deck)

    def get(self):
        result = self.deck[random.randint(0, 54)]
        return result
    #def shuffle(self,):


    #def get(self, ):

deck = DeckofCards()
deck.shuffle()
#for c in deck.deck:
    #print(c.mast, c.num)

random_cart = deck.get()
#print(deck.get())
print(random_cart.mast, random_cart.num)