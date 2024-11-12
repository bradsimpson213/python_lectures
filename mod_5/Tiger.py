from Cat import Cat


class Tiger(Cat):
    def __init__(self, color, age, name, teeth):    
        super().__init__(color, age, name)
        self._teeth = teeth


    def speak(self):
        if self._name == "Tony":
            return f"{self._name} says 'They're GREAT!!!'"
        else:
            return f"{self._name} says 'RAWR!!!'"

    def __repr__(self):
        return f"< {self._name} is a {self._color} Tiger >"

    def __str__(self):
        return f"< {self._name} is a {self._color} Tiger >"

    def __len__(self):
        return self._age



tony = Tiger("orange", 72, "Tony", 30)
tigger = Tiger('orange', 90, "Tigger", 4)
print(tony)
print(tigger)

# print(len("abcdef"))
# print(len([1, 2, 3, 4]))
# print(len(4))
print(len(tigger))
print(tony.get_age())