# def my_function(num):
#     """this is my function"""
#     num  = 3
# my_function(1)

class Cat:
    breed = "american short hair"
    """Cat class"""
    def __init__(self, color, age, name="Kitty"):
        """Constructor method for Cat class"""
        self._color = color
        self._age = age
        self._name = name
        self._toys = []
        # self.breed = "feisty kitty ninja"
        print(self.speak())

    def get_color(self):
        """return the cats color"""
        return self._color

    def get_age(self):
        """returns the cats age"""
        return self._age

    def set_age(self, new_age):
        """sets a new cat age, 1-38 yrs range"""
        if new_age > 38:
            print("Thats too old for a cat's age!")
        elif new_age <= 0:
            print("Cats must have an age greater than 0")
        else:
            self._age = new_age

    def get_name(self):
        """returns the cats name"""
        return self._name

    def set_name(self, new_name):
        """sets a new cat name, between 2 and 20 character"""
        if len(new_name) > 20: 
            print("Thats too long of a name for a cat")
        elif len(new_name) <= 2:
            print("Cats need at least 2 characters for a name")
        else:
            self._name = new_name

    def speak(self):
        return f"{self.get_name()} says 'Meow!'"


    def feed_me(self, times=3):
        [ print("Meeooowwwww?!??") for _ in range(times)]


    def __repr__(self):
        return f"< {self._name} is a {self._color} Cat >"

    def __str__(self):
        return f"< {self._name} is a {self._color} Cat >"


# help(Cat)
blue = Cat("black", 8, "Blue")
blue._age = 99
print(blue._age)
print(blue.get_age())
blue.set_age(39)
print(blue.get_age())
blue.set_age(-2)
# print(blue.get_age())
# blue.set_age(9)
# print(blue.get_age())
# blue.set_age()
patch = Cat("tuxedo", 8, "Patch")
# print(patch._name)
# help(Cat)
# patch.set_name("Mr Fancypants Sparkles McGee")
# print(patch.get_name())
# patch.set_name("P")
# print(patch.get_name())
# patch.set_name("Mr Patch")
# print(patch.get_name())
# print(patch.speak())
# patch.feed_me()
# print(blue.breed)
# print(patch.breed)
# print(Cat.breed)
Cat.breed = "american long hair"
# print(blue.breed)
# print(patch.breed)
# print(Cat.breed)
# print(blue._name)
# blue.breed = "feisty kitty ninja"
# print(blue.breed)
# print(patch.breed)
# print(Cat.breed)
# class Widget:
#     price = "$5"
#     def __init__(self, color):
#         # instance variables
#         self.color = color
#         # self.price = "5$"


# calendar = Widget("blue")
# post_its = Widget("green")
# calculate = Widget('red')
# # calendar.price(6)
# # post_its.price(6)
# # calculate.price(6)
# Widget.price = "$6"
# print([blue, patch])
# # print([1, 2, 3, 4])
# print(blue)

cat = {
    "name": "Blue",
    "age": 8,
    "color": "black"
}

cat_2 = {
    "name": "Patch",
    "age": 8,
    "color": "tuxedo"
}

cat_2["age"] += 203

# Widget.price = "$6"

# calendar = Widget()
# post_it = Widget()

# calendar.price = "$6"
# post_it.price = "$6"
print(blue)