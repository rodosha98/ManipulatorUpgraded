#!/usr/bin/env python
# license removed for brevity
import rospy
import rostest
import unittest

from std_msgs.msg import Float64
from sensor_msgs.msg import JointState
from control_msgs.msg import JointControllerState
import math
import random
import numpy as np


class intTest(unittest.TestCase):
	
	def move_joint(self, pub, jvq):
		for i in range (7):
			pub.publish(jvq[i])
	
	def inizializer(self, j_num, string):
		name =  '/manipulator/joint' + str(j_num) + '_position_controller/' + str(string)
		return name

	def checkpos(self, msg):
		rospy.loginfo("Ya tut vse oki")
		self.assertAlmostEqual(msg.set_point, msg.process_value, delta = 0.01, msg = "joint failed test")
			


	def pusher(self):

		#desired position
		q1 = 1
		q2 = 0
		q3 = 0
		q4 = 0
		q5 = 0
		q6 = 0
		q_des = [q1, q2, q3, q4, q5, q6]

		#publisher and subscrier inizialization
		pub = []
		sub = []
		for i in range(1,8):
			pub.append(rospy.Publisher(inizializer(i, 'command'), Float64, queue_size = 10))
			sub.append(rospy.Subscriber(inizializer(i, 'state'), JointControllerState, checkpos))
		#node
		rospy.init_node('pusher', anonymous=True)
		rate = rospy.Rate(50)

		rospy.sleep(2)

		time = 100000
		for t in range (time):
			for i in range (0,7):
				try: 
					self.move_joint(pub[i], q_des)	
				except rospy.ROSInterruptException:
					pass
			rate.sleep()
			

if __name__ == '__main__':
	rostest.rosrun('control_pkg', 'integration', intTest, sysargs = None)



