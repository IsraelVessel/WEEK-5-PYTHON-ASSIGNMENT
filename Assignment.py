# Activity 1: Class, Constructor, Inheritance Example

class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def get_summary(self):
        return f"{self.title} by {self.author}, published in {self.year}. Genre: {self.genre}."


class ComicBook(Book):
    def __init__(self, title, author, year, illustrator, series):
        super().__init__(title, author, year, genre="Comic")
        self.illustrator = illustrator
        self.series = series

    def get_summary(self):
        # Polymorphism: overrides base method
        return (f"'{self.title}' ({self.series} Series), written by {self.author}, "
                f"illustrated by {self.illustrator}, published in {self.year}.")


# Example usage for Activity 1
book1 = Book("Sapiens: A Brief History of Humankind", "Yuval Noah Harari", 2011, "Non-fiction")
comic1 = ComicBook("The Amazing Spider-Man", "Stan Lee", 1963, "Steve Ditko", "Marvel")

print(book1.get_summary())
print(comic1.get_summary())


# Activity 2: Polymorphism Challenge 🎭

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("The vehicle moves.")


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type  # e.g., Petrol, Electric

    def move(self):
        print(f"{self.brand} {self.model} is driving on the road. 🚗")


class Plane(Vehicle):
    def __init__(self, brand, model, max_altitude):
        super().__init__(brand, model)
        self.max_altitude = max_altitude  # in feet

    def move(self):
        print(f"{self.brand} {self.model} is flying at an altitude up to {self.max_altitude} feet. ✈️")


class Boat(Vehicle):
    def __init__(self, brand, model, boat_type):
        super().__init__(brand, model)
        self.boat_type = boat_type  # e.g., yacht, sailboat

    def move(self):
        print(f"{self.brand} {self.model}, a {self.boat_type}, is sailing on water. 🚤")


# Example usage for Activity 2
my_car = Car("Tesla", "Model S", "Electric")
my_plane = Plane("Boeing", "747", 35000)
my_boat = Boat("Beneteau", "Oceanis 45", "sailboat")

my_car.move()    # Tesla Model S is driving on the road. 🚗
my_plane.move()  # Boeing 747 is flying at an altitude up to 35000 feet. ✈️
my_boat.move()   # Beneteau Oceanis 45, a sailboat, is sailing on water. 🚤
