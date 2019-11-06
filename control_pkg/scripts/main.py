#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64
import math
import random
import time

def move_joint(joint_num, min, max):
	pub = rospy.Publisher('/manipulator/joint'+joint_num+'_position_controller/command', Float64, queue_size=10)
	rospy.init_node('move_joint', anonymous=True)
	rate = rospy.Rate(10) # 10hz
	pos = random.uniform(min,max)
	if not rospy.is_shutdown():
		hello_str = "Joint world! %s" % rospy.get_time()
		position = pos
		rospy.loginfo(position)
		pub.publish(position)
		rate.sleep()

if __name__ == '__main__':
	try:
		time.sleep(10)
		while not 0:
			move_joint('1',-math.pi/2, math.pi/2)
			move_joint('2',0, 0.4)
			move_joint('3',-math.pi/4, math.pi/4)
			move_joint('4', 0, math.pi)
			move_joint('5',-math.pi/2,math.pi/2)
			move_joint('6',-math.pi, 0)
			move_joint('8',-math.pi/6, math.pi/6)
			move_joint('9',-math.pi/6, math.pi/6)
	except rospy.ROSInterruptException:
		pass
