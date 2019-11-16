#!/usr/bin/python2.7
# license removed for brevity
import rospy
from std_msgs.msg import Float64
import math
import random
import time
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2
import rospy
from std_msgs.msg import Float64
from sensor_msgs.msg import Image
import os


path = os.path.dirname(os.path.realpath(__file__))
def move_joint(joint_num, min, max):
	pub = rospy.Publisher('/manipulator/joint'+joint_num+'_position_controller/command', Float64, queue_size=10)
	rospy.init_node('move_joint', anonymous=True)
	rate = rospy.Rate(5) # 10hz
	pos = random.uniform(min,max)
	if not rospy.is_shutdown():
		hello_str = "Joint world! %s" % rospy.get_time()
		position = pos
		rospy.loginfo(position)
		pub.publish(position)
		rate.sleep()

# Instantiate CvBridge
bridge = CvBridge()

def image_callback(msg):
	print("Received an image!")
	rate = rospy.Rate(30) # 10hz
	try:
		# Convert your ROS Image message to OpenCV2
		cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
	except CvBridgeError as e:
		print(e)
	else:
		# Save your OpenCV2 image as a jpeg 
		cv2.imwrite(path + '/Images' + '/' +'camera_image'+str(j)+'.jpeg', cv2_img)
		rate.sleep()

if __name__ == '__main__':
	try:
		time.sleep(10)
		j = 0
		image_topic = "/manipulator/camera1/image_raw"
		while (j < 10):
			move_joint('6',-math.pi, 0)
			rospy.Subscriber(image_topic, Image, image_callback)		
			j += 1
			if rospy.ROSInterruptException:
				pass
	except rospy.ROSInterruptException:
		pass

#!/usr/bin/python2.7
# license removed for brevity
import os
path = os.path.dirname(os.path.realpath(__file__))
import rospy
from std_msgs.msg import Float64
from sensor_msgs.msg import Image
import time
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2

# Instantiate CvBridge
bridge = CvBridge()

class ImageSaver:

	def __init__(self):
		self.number = 0
                self.ImagePath = path

	def image_callback(self, msg):
		rate = rospy.Rate(30) # 30hz
		try:
			# Convert ROS Image message to OpenCV2
			cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
		except CvBridgeError as e:
			print(e)
		else:
			self.number += 1
			print("Image"+str(self.number)+" saved")
			filename = path+'/Images/' +'camera_image'+str(self.number)+'.jpeg'
			cv2.imwrite(filename, cv2_img)
		rate.sleep()
	def main(self):
		time.sleep(5)
		rospy.init_node('camera_image_saver')
		# Define your image topic
		image_topic = "/manipulator/camera1/image_raw"
		# Set up your subscriber and define its callback
		rospy.Subscriber(image_topic, Image, self.image_callback)
		# Spin until ctrl + c
		rospy.spin()

	def move

if __name__ == '__main__':
	rospy.init_node('camera_image_saver')
	image_topic = "/manipulator/camera1/image_raw"
	saver = ImageSaver()
	saver.main()
	rospy.spin()

