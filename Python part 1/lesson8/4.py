class Rocket():

    def __init__(self):
        # Each rocket has (x, y) position
        self.x = 0
        self.y = 0

    def move_up(self):
        # Increment the y-position of the rocket
        self.y +=1

my_rocket = Rocket()
print("Rocket altitude:", my_rocket.y)

my_rocket.move_up()
print("Rocket altitude:", my_rocket.y)

my_rocket.move_up()
print("Rocket altitude:", my_rocket.y)