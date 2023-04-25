#PEP257

class Rocket():

    def __init__(self):
        # Each rocket has (x, y) position
        self.x = 0
        self.y = 0

    def move_up(self):
        # Increment the y-position of the rocket
        self.y +=1

my_rockets=[]
for x in range(0,5):
    new_rocket = Rocket()
    my_rockets.append(new_rocket)

my_rockets[0].move_up()

for rocket in my_rockets:
    print("Rocket altitude:", rocket.y)


