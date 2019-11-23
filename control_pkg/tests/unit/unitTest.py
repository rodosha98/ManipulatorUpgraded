#!/usr/bin/env python
# coding: utf-8

import rosunit
import unittest
import FK
import numpy as np
pi = np.pi


class FKUTest(unittest.TestCase):

	def initialposition(self):
		jvq1 = np.array([0, 0, 0, 0, 0, 0])
		len1 = np.array([0.5, 0.3, 0.6, 0.25, 0.1, 0.15])
		res1 = [0, 1.10, 0.80]
		self.assertEqual(FK.forwardKinematics(jvq1, len1), res1)

	def test2(self):
		jvq2 = np.array([90, 0.2, 30, 90, 45, -90])
		len2 = np.array([0.5, 0.3, 0.6, 0.25, 0.1, 0.15])
		res2 = [-0.44, -0.11, 1.66]
		self.assertEqual(FK.forwardKinematics(jvq2, len2), res2)

	def test3(self):
		jvq3 = np.array([90, 0.2, 30, 90, 45, -90])
		len3 = np.array([-0.5, 0.3, 0.6, 0.25, 0.1, 0.15])
		res3 = "Length 1 should be greater than 0"
		self.assertEqual(FK.forwardKinematics(jvq3, len3), res3)

	def test4(self):
		jvq4 = np.array([10, 1, 30, 90, 45, -90])
		len4 = np.array([0.5, 0.3, 0.6, 0.25, 0.1, 0.15])
		res4 = "q2 limits are 0 : 0.4"
		self.assertEqual(FK.forwardKinematics(jvq4, len4), res4)
	
	def test5(self):
		jvq5 = np.array([0, 0.4, 45, 180, 90, -180])
		len5 = np.array([0.5, 0.3, 0.6, 0.25, 0.1, 0.15])
		res5 = [-0.0, 0.28, 1.48]
		self.assertEqual(FK.forwardKinematics(jvq5, len5), res5)
	
	def test6(self):
		jvq6 = np.array([0, 0.4, -90, 0, 45, -90])
		len6 = np.array([0.5, 0.3, 0.6, 0.25, 0.1, 0.15])
		res6 = "q3 limits are -45 : 45" 
		self.assertEqual(FK.forwardKinematics(jvq6, len6), res6)

	def test7(self):
		jvq7 = np.array([-90, 0, -45, 0, -90, -180])
		len7 = np.array([0.5, 0.3, 0.6, 0.25, 0.1, 0.15])
		res7 = [0.57, -0.0, 0.23]
		self.assertEqual(FK.forwardKinematics(jvq7, len7), res7)
	

	def test8(self):
		jvq8 = np.array([90, 0.4, 45, 180, 90, 0])
		len8 = np.array([0.5, 0.3, 0.6, 0.25, 0.1, 0.15])
		res8 = [-0.07, 0.0, 1.27]
		self.assertEqual(FK.forwardKinematics(jvq8, len8), res8)


       
if __name__ == '__main__':
	rosunit.unitrun("control_pkg", "test_unit", FKUTest)







