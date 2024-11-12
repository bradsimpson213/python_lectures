from Cat import Cat


def test_constructor():
    age = 5
    color = "black"
    name= "Kitty Cat"
    new_cat = Cat(color, age, name)
    assert new_cat._color == color
    assert new_cat._age == age
    assert new_cat._name == name


def test_name_default():
    age = 6
    color = "brown"
    new_cat = Cat(color, age)
    assert new_cat._color == color
    assert new_cat._age == age
    assert new_cat._name == "Kitty"


def test_color_getter():
    new_cat1 = Cat("orange", 4)
    new_cat2 = Cat("gray", 11)
    assert new_cat1.get_color() == new_cat1._color
    assert new_cat2.get_color() == new_cat2._color

def test_age_getter():
    new_cat1 = Cat("orange", 7)
    new_cat2 = Cat("red", 6)
    assert new_cat1.get_age() == new_cat1._age
    assert new_cat2.get_age() == new_cat2._age

def test_age_setter_correct():
    new_cat = Cat("white", 5)
    new_cat.set_age(14)
    assert new_cat._age == 14

def test_age_setter_too_high():
    new_cat = Cat("white", 5)
    result = new_cat.set_age(44)
    assert new_cat._age == 5
    assert result == "Thats too old for a cat's age!"

def test_age_setter_too_low():
    new_cat = Cat("white", 5)
    result = new_cat.set_age(-1)
    assert new_cat._age == 5
    assert result == "Cats must have an age greater than 0"


def test_speak_method():
    new_cat = Cat("tuxedo", 6)
    new_cat2 = Cat("black", 12, "Steve")
    cat_spoke = new_cat.speak()
    cat_spoke2 = new_cat2.speak()
    assert cat_spoke == "Kitty says 'Meow!'"
    assert cat_spoke2 == "Steve says 'Meow!'"


def test_name_getter():
    new_cat = Cat("gray", 12, "Kevin")
    assert new_cat.get_name() == new_cat._name


def test_name_setter():
    new_cat = Cat("purple", 6, "Tammy")
    new_cat.set_name("Karen")
    assert new_cat.get_name() == "Karen"

def test_name_setter_too_long():
    new_cat = Cat("pink", 12, "Harry")
    result = new_cat.set_name("Mr Harry I need a haircut now the kitty")
    assert result == "Thats too long of a name for a cat"
    assert new_cat.get_name() == "Harry"

def test_name_setter_too_short():
    new_cat = Cat("blue", 5, 'Tim')
    result = new_cat.set_name("T")
    assert result == "Cats need at least 2 characters for a name"
    assert new_cat.get_name() == 'Tim'