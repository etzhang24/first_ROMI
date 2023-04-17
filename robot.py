import wpilib
import os
from wpilib import TimedRobot,Joystick,Spark,DigitalInput
from linefollower import Linefollower
from drivetrain import Drivetrain

class MyRobot(TimedRobot):

    def robotInit(self):
        self.controller = Joystick(0)
        self.drivetrain=Drivetrain()
        self.linefollower = Linefollower(self.drivetrain)
    def robotPeriodic(self):
        pass
    def autonomousInit(self):
        pass

    def teleopPeriodic(self):
        forward=self.controller.getRawAxis(0)
        rotate=self.controller.getRawAxis(1)
        self.drivetrain.move(forward,-rotate)

    def autonomousPeriodic(self):
        self.linefollower.run()

if __name__ == "__main__":
    os.environ["HALSIMWS_HOST"] = "10.0.0.2"
    os.environ["HALSIMWS_PORT"] = "3300"
    wpilib.run(MyRobot)