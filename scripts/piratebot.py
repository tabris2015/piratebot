from gpiozero import Motor

class PirateRobot(object):
    # pins for control
    #               (FW, BW)
    left_pins =     (27, 22)
    right_pins =    (23, 24)
    
    def __init__(self, lpins, rpins):
        # pines
        self.left_pins = lpins
        self.right_pins = rpins
        # init hardware and pins
        self.left_motor = Motor(self.left_pins[0], self.left_pins[1])
        self.right_motor = Motor(self.right_pins[0], self.right_pins[1])
    
    def left(self, vel):
        if vel > 0:
            self.left_motor.forward(vel)
        else:
            self.left_motor.backward(vel)
    
    def right(self, vel):
        if vel > 0:
            self.right_motor.forward(vel)
        else:
            self.right_motor.backward(vel)
    
    def drive(self, linear, angular):
        # differential drive 
        left_vel = (linear + angular) / 2
        right_vel = (linear - angular) / 2

        self.left(left_vel)
        self.right(right_vel)