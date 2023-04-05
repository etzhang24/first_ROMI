
from drivetrain import Drivetrain
from wpilib import DigitalInput

class Linefollower:
    def __init__(self, drivetrain, forward, rotate):
        self.left_sensor = DigitalInput(9)
        self.right_sensor = DigitalInput(8)



    def run(self):
        print(f"left: {self.left_sensor.get()}")
        print(f"right: {self.right_sensor.get()}")

