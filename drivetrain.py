import wpilib
import os
from wpilib import TimedRobot,Joystick,Spark,DigitalInput
from wpilib.drive import DifferentialDrive

class Drivetrain:
        def __init__(self):
            self.left_motor = Spark(0)
            self.right_motor = Spark(1)
            self.drivetrain = DifferentialDrive(self.left_motor, self.right_motor)
            self.left_sensor = DigitalInput(9)
            self.right_sensor = DigitalInput(8)


        def move(self, forward, rotate):
            self.drivetrain.arcadeDrive(forward,rotate)

