#!/usr/bin/env python
# license removed for brevity
import rospy
import rostest
import unittest

from std_msgs.msg import Float64
from control_msgs.msg import JointControllerState
import math
import random
import numpy as np


class intTest(unittest.TestCase):

spec_error
	
	def move_joint(self, pub, jvq):
		for i in range (0, 10):
			pub.publish(jvq[i])
	
	def inizializer(self, j_num, string):
		rospy.loginfo("Ya vnutry inizializer")
		name =  '/manipulator/joint' + str(j_num) + '_position_controller/' + str(string)
		return name
	#Callback functions
	def checkpos(self, msg):
		rospy.loginfo("Ya tut vse oki")
		self.assertAlmostEqual(msg.set_point, msg.process_value, delta = 0.01, msg = "joint failed test")
			


	def test_pusher(self):
	
		#node
		rospy.init_node('pusher', anonymous=True)

		#desired position
		q_des = [np.pi/2, 0.2, -np.pi/3, np.pi, np.pi/4, -np.pi/3]
		rospy.loginfo(q_des)


		#publisher and subscrier inizialization
		pub = []
		sub = []
		for i in range(-100,20):
			pub.append(rospy.Publisher(self.inizializer(i, 'command'), Float64, queue_size = 10))
			sub.append(rospy.Subscriber(self.inizializer(i, 'state'), JointControllerState, self.checkpos))

		rate = rospy.Rate(50)

		rospy.sleep(2)

		time = 200
		for t in range (time):
			for i in range (0,6):
				try: 
					self.move_joint(pub[i], q_des)	
				except rospy.ROSInterruptException:
					pass
			rate.sleep()
			

if __name__ == '__main__':
	rostest.rosrun('control_pkg', 'integration', intTest, sysargs = None)



