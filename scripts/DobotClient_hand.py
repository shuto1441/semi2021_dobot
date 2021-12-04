#!/usr/bin/env python
import rospy
# import sys
# LIBPATH = "../../dobot/src"
# sys.path.append(LIBPATH)
import DobotClient as dc
from semi2021_dobot.msg import dobot

class Subscribe_publishers():
    def __init__(self):
        # Subscriberを作成
        self.subscriber = rospy.Subscriber('dobot_status', dobot, self.callback)
        # messageの型を作成
        self.message = dobot()

    def callback(self, message):
        isJoint = False
        position_x = message.x
        position_y = message.y
        position_z = message.z
        gesture = message.gesture
        if(gesture == 'up'):
            dc.set_jog_cmd(isJoint, 5)
        if(gesture == 'down'):
            dc.set_jog_cmd(isJoint, 6)
        if(gesture == 'left'):
            dc.set_jog_cmd(isJoint, 3)
        if(gesture == 'right'):
            dc.set_jog_cmd(isJoint, 4)
        #dc.set_ptp_cmd(1, position_x, position_y, position_z, 30)

def main():
    # nodeの立ち上げ
    rospy.init_node('Node_name')

    sub = Subscribe_publishers()

    rospy.spin()

if __name__ == '__main__':
   main()