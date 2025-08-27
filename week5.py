# Assignment 1: Design Your Own Class! 🏗️

# -------- Disability Center --------
class DisabilityCenter:
    # start with name, place, and services
    def __init__(self, name, location, services):
        self.name = name
        self.location = location
        self.services = services

    # show info
    def show_info(self):
        print(f"{self.name} is in {self.location}")
        print("We offer:")
        for s in self.services:
            print("-", s)

    # give a service
    def provide_service(self, service):
        if service in self.services:
            print(f"Now providing: {service}")
        else:
            print(f"{service} not available")


# make Africa Ability Trust
aat = DisabilityCenter(
    "Africa Ability Trust",
    "Kibera, Nairobi",
    ["Therapy", "Training", "Counselling"]
)

# test it
aat.show_info()
aat.provide_service("Therapy")
aat.provide_service("Counselling")

print("\n--- Polymorphism Example ---")


#Activity 2: Polymorphism Challenge! 🎭

# -------- Polymorphism with Vehicles --------
class Vehicle:
    def move(self):
        print("This vehicle moves")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# test them
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()
