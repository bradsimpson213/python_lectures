

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
            return ("Thats too old for a cat's age!")
        elif new_age <= 0:
            return ("Cats must have an age greater than 0")
        else:
            self._age = new_age

    def get_name(self):
        """returns the cats name"""
        return self._name

    def set_name(self, new_name):
        """sets a new cat name, between 2 and 20 character"""
        if len(new_name) > 20: 
            return ("Thats too long of a name for a cat")
        elif len(new_name) <= 2:
            return ("Cats need at least 2 characters for a name")
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





