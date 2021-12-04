#!/usr/bin/env python
import rospy
# import sys
# LIBPATH = "../../dobot/src"
# sys.path.append(LIBPATH)
import DobotClient as dc
from semi2021_dobot.msg import hand
from semi2021_dobot.msg import dobot

class Subscribe_publishers():
    def __init__(self):
        # Subscriberを作成
        self.subscriber_front = rospy.Subscriber('front_sensing/hand_status', hand, self.callback_front)
        # Subscriberを作成
        self.subscriber_side = rospy.Subscriber('under_sensing/hand_status', hand, self.callback_under)
        # Publisherを作成
        self.publisher_right = rospy.Publisher('dobot_right/dobot_status', dobot, queue_size=10)
        # Publisherを作成
        self.publisher_left = rospy.Publisher('dobot_left/dobot_status', dobot, queue_size=10)
        # messageの型を作成
        self.message_right = dobot()
        # messageの型を作成
        self.message_left = dobot()

    def callback_front(self, message):
        self.message_right.z = message.right_y
        self.message_left.z = message.left_y
        # callback時の処理
        self.make_msg_right(self.message_right)
        # callback時の処理
        self.make_msg_left(self.message_left)
        # publish
        self.send_msg()

    def callback_under(self, message):
        self.message_right.x = message.right_x
        self.message_right.y = message.right_y
        self.message_right.gesture = message.right_gesture
        self.message_left.x = message.left_x
        self.message_left.y = message.left_y
        self.message_left.gesture = message.left_gesture
        # callback時の処理
        self.make_msg_right(self.message_right)
        # callback時の処理
        self.make_msg_left(self.message_left)
        # publish
        self.send_msg()

    def make_msg_right(self, message):
        # 処理を書く
        self.message_right.x = message.x
        self.message_right.y = message.y
        self.message_right.z = message.z
        self.message_right.gesture = message.gesture

    def make_msg_left(self, message):
        # 処理を書く
        self.message_left.x = message.x
        self.message_left.y = message.y
        self.message_left.z = message.z
        self.message_left.gesture = message.gesture

    def send_msg(self):
        self.publisher_right.publish(self.message_right)
        self.publisher_left.publish(self.message_left)

def main():
    # nodeの立ち上げ
    rospy.init_node('Node_name')

    sub = Subscribe_publishers()

    rospy.spin()

if __name__ == '__main__':
   main()