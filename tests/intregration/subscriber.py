#!/usr/bin/env python
# license removed for brevity
import rospy

from control_msgs.msg import JointControllerState

import os





def main():
	counter = 0
	rospy.init_node('image_listener')

	#topics for each link
	link1_topic = '/manipulator/joint1_position_controller/state'
	link2_topic = '/manipulator/joint2_position_controller/state'
	link3_topic = '/manipulator/joint3_position_controller/state'
	link4_topic = '/manipulator/joint4_position_controller/state'
	link5_topic = '/manipulator/joint5_position_controller/state'
	link6_topic = '/manipulator/joint6_position_controller/state'
	
	rospy.Subscriber(link1_topic,JointControllerState,check_position1)
	rospy.Subscriber(link2_topic,JointControllerState,check_position2)
	rospy.Subscriber(link3_topic,JointControllerState,check_position3)
	rospy.Subscriber(link4_topic,JointControllerState,check_position4)
	rospy.Subscriber(link5_topic,JointControllerState,check_position5)
	rospy.Subscriber(link6_topic,JointControllerState,check_position6)
	rospy.spin()




def check_position1(msg):
	if abs(msg.set_point-msg.process_value) < 0.01:
		print('joint 1 passed test')


def check_position2(msg):
	if abs(msg.set_point-msg.process_value) < 0.01:
		print('joint 2 passed test')

def check_position3(msg):
	if abs(msg.set_point - msg.process_value) < 0.01:
		print('joint 3 passed test')
def check_position4(msg):
	if abs(msg.set_point-msg.process_value) < 0.01:
		print('joint 4 passed test')

def check_position5(msg):
	if abs(msg.set_point-msg.process_value) < 0.01:
		print('joint 5 passed test')
def check_position6(msg):
	if abs(msg.set_point-msg.process_value) < 0.01:
		print('joint 6 passed test')

if __name__ == '__main__':
	main()




