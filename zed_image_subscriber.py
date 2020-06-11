#!/usr/bin/env python
# coding=utf-8
import rospy
from sensor_msgs.msg import Image


def callback(image_data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %d.", image_data.height)


def listener():
    rospy.init_node("zed_image_subscriber", anonymous=True)
    rospy.Subscriber("/zed/zed_node/left/image_rect_color", Image, callback)
    rospy.loginfo("starting zed_image_subscriber node success.")
    rospy.spin()


if __name__ == '__main__':
    listener()
