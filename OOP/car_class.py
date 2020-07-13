class Car:

    def __init__(self, make, acceleration):
        self.make = make
        self.speed = 10
        self.acceleration = acceleration
        self.brake = 3
        self.max_speed = 200

    def accelerate(self):
        self.speed += self.acceleration
        if self.speed > 200:
            self.speed = 200
        return self.speed

    def decelerate(self):
        self.speed -= self.brake
        if self.speed < 0:
            self.speed = 0
        return self.speed



new_car = Car("Ford", 10)

print(new_car.decelerate())
print(new_car.decelerate())
print(new_car.decelerate())
print(new_car.decelerate())
print(new_car.decelerate())



