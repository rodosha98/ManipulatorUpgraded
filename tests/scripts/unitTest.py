#!/usr/bin/env python
# coding: utf-8



import unittest
import FK
import numpy as np
pi = np.pi


class FKUTest(unittest.TestCase):

	def test1(self):
		L = np.array([0.5, 0.3, 0.6, 0.25, 0.1, 0.15])
		Q = np.array([0, 0, 0, 0, 0, 0])
		self.assertEqual(FK.forwardKinematics(Q, L), ( 0, 1.10, 0.80))

	def test2(self):
		L = np.array([0.5, 0.3, 0.6, 0.25, 0.1, 0.15])
		Q = np.array([90, 0.2, 30, 90, 45, -90])
		self.assertEqual(FK.forwardKinematics(Q, L), ( -0.44, -0.11, 1.66))

	def test3(self):
		L = np.array([-0.5, 0.3, 0.6, 0.25, 0.1, 0.15])
		Q = np.array([90, 0.2, 30, 90, 45, -90])
		self.assertEqual(FK.forwardKinematics(Q, L), (None))

	def test4(self):
		L = np.array([0.5, 0.3, 0.6, 0.25, 0.1, 0.15])
		Q = np.array([10, 1, 30, 90, 45, -90])
		self.assertEqual(FK.forwardKinematics(Q, L), (None))
	
	def test5(self):
		L = np.array([0.5, 0.3, 0.6, 0.25, 0.1, 0.15])
		Q = np.array([0, 0.4, 45, 180, 90, -180])
		self.assertEqual(FK.forwardKinematics(Q, L), (-0.0, 0.28, 1.48))
	
	def test6(self):
		L = np.array([0.5, 0.3, 0.6, 0.25, 0.1, 0.15])
		Q = np.array([0, 0.4, -90, 0, 45, -90])
		self.assertEqual(FK.forwardKinematics(Q, L), (None))

	def test7(self):
		L = np.array([0.5, 0.3, 0.6, 0.25, 0.1, 0.15])
		Q = np.array([-90, 0, -45, 0, -90, -180])
		self.assertEqual(FK.forwardKinematics(Q, L), (0.57, -0.0, 0.23))

	def test8(self):
		L = np.array([0.5, 0.3, 0.6, 0.25, 0.1, 0.15])
		Q = np.array([90, 0.4, 45, 180, 90, 0])
		self.assertEqual(FK.forwardKinematics(Q, L), (-0.07, 0.0, 1.27))


       
if __name__ == '__main__':
	unittest.main()








# In[ ]:




