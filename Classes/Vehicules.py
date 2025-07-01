import time

class Vehicle:
    def wayToTurn(self):
        pass

    def turn(self, left):
        self.wayToTurn(self, left, True)
        time.sleep(0.25)
        self.wayToTurn(self, left, False)

class TrackedVehicle:
    def control_track(self, left, stop):
        pass

    def wayToTurn(self, left):
        self.control_track(self, left, True)


class WheeledVehicle:
    def turn_front_wheels(self, left, on):
        pass

    def turn(self, left):
        self.turn_front_wheels(left, True)
