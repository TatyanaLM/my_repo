import random

NumsList = ['Джокер', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', "Дама", "Король", "Туз"]
MastList = ["пик", "крестей", "бубей", "червей"]

class Card():
    #NumsList = ['Джокер', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', "Дама", "Король", "Туз"]
    #MastList = ["пик", "крестей", "бубей", "червей"]

    def __init__(self, num, mast="none"):
        self.num = num
        self.mast = mast

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

    def get(self, index):
        if index < len(self.deck):
            if len(self.deck) > 0:
                result = self.deck[index]
                self.deck.remove(self.deck[index])
            else:
                result = "Карты кончились"
        else:
            return "Такого индекса нет в колоде"
        return result
    #def shuffle(self,):
    #def get(self, ):

deck = DeckofCards()
deck.shuffle()
#random_cart = deck.get(3)
#print(random_cart)

for c in range(54):
    print(c)
    random_cart = deck.get(0)
    print(random_cart.mast, random_cart.num)
    print(len(deck.deck))
    print("\n")


#print(deck.deck)
#print(deck.get())
#print(random_cart.mast, random_cart.num)