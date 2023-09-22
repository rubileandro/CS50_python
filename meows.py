class Cat:
    # Class variable
    MEOWS = 3

    # instance method
    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")


cat = Cat()
cat.meow()