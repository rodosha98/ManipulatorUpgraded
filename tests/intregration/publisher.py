#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64
import math
import random


def talker():



	pub1 = rospy.Publisher('/manipulator/joint1_position_controller/command', Float64, queue_size=10)
	pub2 = rospy.Publisher('/manipulator/joint2_position_controller/command', Float64, queue_size=10)
	pub3 = rospy.Publisher('/manipulator/joint3_position_controller/command', Float64, queue_size=10)
	pub4 = rospy.Publisher('/manipulator/joint4_position_controller/command', Float64, queue_size=10)
	pub5 = rospy.Publisher('/manipulator/joint5_position_controller/command', Float64, queue_size=10)
	pub6 = rospy.Publisher('/manipulator/joint6_position_controller/command', Float64, queue_size=10)

	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(50)


	while not rospy.is_shutdown():


		pos1 = 0.0
		pos2 = 0.0
		pos3 = 0.0
		pos4 = 0.0
		pos5 = 0.0
		pos6 = 0.0




		pub1.publish(pos1)
		pub2.publish(pos2)
		pub3.publish(pos3)
		pub4.publish(pos4)
		pub5.publish(pos5)
		pub6.publish(pos6)



		rate.sleep()



def main():
	talker()

if __name__ == '__main__':
	main()



