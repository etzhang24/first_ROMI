import wpilib
import os
from wpilib import TimedRobot,Joystick,Spark,DigitalInput
from wpilib.drive import DifferentialDrive
from linefollower import Linefollower


class MyRobot(TimedRobot):

    def robotInit(self):
        self.controller = Joystick(0)
        self.left_motor=Spark(0)
        self.right_motor = Spark(1)
        self.drivetrain=DifferentialDrive(self.left_motor,self.right_motor)
        self.Linefollower = Linefollower(self.drivetrain)
    def robotPeriodic(self):
        pass
    def autonomousInit(self):
        self.left_sensor = DigitalInput(9)
        self.right_sensor = DigitalInput(8)

    def teleopPeriodic(self):
        forward=self.controller.getRawAxis(0)
        rotate=self.controller.getRawAxis(1)
        self.drivetrain.arcadeDrive(forward,-rotate)

    def autonomousPeriodic(self):
        self.Linefollower.run()

if __name__ == "__main__":
    os.environ["HALSIMWS_HOST"] = "10.0.0.2"
    os.environ["HALSIMWS_PORT"] = "3300"
    wpilib.run(MyRobot)