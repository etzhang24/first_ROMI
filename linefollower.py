from drivetrain import Drivetrain



class Linefollower:
    def __init__(self, drivetrain):
        self.drivetrain = drivetrain


    def run(self):
        #print(f"left:{self.drivetrain.left_sensor.get()}")
        #print(f"right:{self.drivetrain.right_sensor.get()}")
        if self.drivetrain.left_sensor.get():
            self.drivetrain.move(-0.5,0.1)
            print("1")
        if self.drivetrain.right_sensor.get():
            self.drivetrain.move(0.5, 0.1)
            print("2")
        else:
            self.drivetrain.move(0,0.3)



