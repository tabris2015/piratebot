#!/usr/bin/env python
import sys
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from piratebot import PirateRobot

class PirateControl:
    idx = 0
    twist_topic = '/cmd_vel'
    joy_topic = 'joy'
    
    linear = 0
    angular = 0

    def __init__(self):    
        print("Inicializando hardware...")
        self.robot = PirateRobot()
        print('creando subs y pubs...')
        self.twist_sub = rospy.Publisher(self.twist_topic, Twist, self.twistCallback, queue_size=1)
        
    def twistCallback(self, msg):
        #control manual de velocidad con el joystick
        linear = msg.linear.x
        angular = msg.angular.z
        self.robot.drive(linear, angular)

def main(args):
    rospy.init_node('pirate_control', anonymous=True)
    pirate = PirateControl()

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("shutting down")

if __name__ == '__main__':
    main(sys.argv)
