#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64
import math
import random
import time
import numpy as np

def move_joint(joint_num, min, max, pub):
	pos = random.uniform(min,max)
	if not rospy.is_shutdown():
		hello_str = "Joint world! %s" % rospy.get_time()
		position = pos
		rospy.loginfo(position)
		pub.publish(position)
		rate.sleep()

if __name__ == '__main__':
	#Publishers
	publisher = np.zeros(9)
	for i in range (1, 10):
		publisher[i] = rospy.Publisher('/manipulator/joint'+i+'_position_controller/command', Float64, queue_size=10)
	#Node
	rospy.init_node('move_joint', anonymous=True)
	#Rate
	rate = rospy.Rate(10) # 10hz
	try:
		time.sleep(10)
		move_joint('1',-math.pi/2, math.pi/2, publisher[0])
		move_joint('2',0, 0.4, publisher[1])
		move_joint('3',-math.pi/4, math.pi/4, publisher[2])
		move_joint('4', 0, math.pi, publisher[3])
		move_joint('5',-math.pi/2,math.pi/2, publisher[4])
		move_joint('6',-math.pi, 0, publisher[5])
		move_joint('8',-math.pi/6, math.pi/6, publisher[6])
		move_joint('9',-math.pi/6, math.pi/6)
		rospy.spin()
	except rospy.ROSInterruptException:
		pass
