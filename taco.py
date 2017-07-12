meat = input("What meat would you like for your taco?: ")
topping = input("What topping would you like to be added to your taco?: ")

class Taco():
    def __init__(self,meat,topping):
        self.meat = meat
        self.topping = topping
    def yourOrder(self):
        print("Your taco consists of " + self.meat + " with " + self.topping)

myTaco = Taco(meat,topping)

print(myTaco.meat)
print(myTaco.topping)
myTaco.yourOrder()