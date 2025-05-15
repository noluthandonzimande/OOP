# Base class
class Vehicle:
    def move(self):
        print("The vehicle is moving.")

# Subclasses with different move() implementations
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚢")

# Function demonstrating polymorphism
def vehicle_movement(vehicle):
    vehicle.move()

# Test with different vehicles
car = Car()
plane = Plane()
boat = Boat()

vehicle_movement(car)
vehicle_movement(plane)
vehicle_movement(boat)
