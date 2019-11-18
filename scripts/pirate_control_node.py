#!/usr/bin/env python
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

    def __init__(self, folder):    
        print("Inicializando hardware...")
        self.robot = PirateRobot()
        print('creando subs y pubs...')
        self.joy_sub = rospy.Subscriber(self.joy_topic, Joy, self.joyCallback, queue_size=1)
        self.twist_sub = rospy.Publisher(self.twist_topic, Twist, self.twistCallback, queue_size=1)
        

    def twistCallback(self, msg):
        #control manual de velocidad con el joystick
        self.linear = msg.linear.x
        self.angular = msg.angular.z

def main(args):
    rospy.init_node('autopilot', anonymous=True)
    stamper = AutoPilot(None)

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("shutting down")
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
