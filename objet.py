numberList = [1.2, 3.5, 4.3, 2.8]
phoneNumberDictionary = {"alice": "01234 567890", "bob": "01324 765098"}
mixedList = [5, 4, 3, 2, 1, "boom"]


class Person:
    """Personne."""

    def __init__(self, name):
        """Donne un nom."""
        self.name = name

    def walk(self):
        """Marche."""
        print(f"{self.name} marche.")


volunteers = [Person("Alice"), Person("Bob"), Person("Carol")]
for volunteer in volunteers:
    volunteer.walk()

# Ici, nous reprenons nos outils !
toolbox = {
    "screwdriver": Screwdriver(50),
    "hammer": Hammer(),
    "nails": [Nail(), Nail(), Nail()],
}
