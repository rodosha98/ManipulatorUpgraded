#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import math
pi = math.pi


# In[2]:


def trotx(alpha):
    a = np.deg2rad(alpha)
    Tx = np.array([[1, 0, 0, 0],
                   [0, np.cos(a), -np.sin(a), 0],
                   [0, np.sin(a), np.cos(a), 0],
                   [0, 0, 0, 1]], dtype = float)
    return Tx

def troty(beta):
    b = np.deg2rad(beta)
    Ty = np.array([[np.cos(b), 0, np.sin(b), 0],
                   [0, 1, 0, 0],
                   [-np.sin(b), 0, np.cos(b), 0],
                   [0, 0, 0, 1]], dtype = float)
    return Ty

def trotz(gamma):
    c = np.deg2rad(gamma)
    Tz = np.array([[math.cos(c), -math.sin(c), 0, 0],
                   [math.sin(c), math.cos(c), 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]], dtype = float)
    return Tz

def transl(a, b, c):
    Tr = np.array([[1, 0, 0, a],
                   [0, 1, 0, b],
                   [0, 0, 1, c],
                   [0, 0, 0, 1]], dtype = float)
    return Tr

    


# In[3]:


#Forward Kinemcatics


# In[4]:


# Initial parameters
#Lengths
l1 = 0.5
l2 = 0.3
l3 = 0.6
l4 = 0.25
l5 = 0.1
l6 = 0.15
# Length vector
L = [l1, l2, l3, l4, l5, l6]
#Joint variables
q1 = 90
q2 = 0.2
q3 = 30
q4 = 90
q5 = 45
q6 = -90
# Joint variables vector
Q = [q1, q2, q3, q4, q5, q6]



#Limit Assertions
def checkCorrectness(q1, q2, q3, q4, q5, q6, l1, l2, l3, l4, l5, l6):
    if (q2 < 0) or (q2 > 0.4):
        return "q2 limits are 0 : 0.4" 
    if (q3 < -45) or (q3 > 45):
        return "q3 limits are -45 : 45" 
    if (q4 < 0) or (q4 > 180):
        return "q4 limits are 0 : 180"
    if(q5 < -90) or (q5 > 90):
        return "q5 limits are -90 : 90"
    if (q6 < -180) or (q6 > 0):
        return"q5 limits are -180 : 0"

    #Length Assertions
    if l1 <= 0:
        return "Length 1 should be greater than 0"
    if l2 <= 0:
        return "Length 2 should be greater than 0" 
    if l3 <= 0:
        return "Length 3 should be greater than 0"
    if l4 <= 0:
        "Length 4 should be greater than 0" 
    if l5 <= 0:
        return "Length 5 should be greater than 0"
    if l6 <= 0:
        return"Length 6 should be greater than 0"
    else: return 0
    
    




def forwardKinematics(Q, L):
	k = checkCorrectness(Q[0], Q[1], Q[2], Q[3], Q[4], Q[5], L[0], L[1], L[2], L[3], L[4], L[5])
	H_10 = trotz(Q[0])
	H_20 = H_10.dot(transl(0, 0, L[0]))
	H_30 = H_20.dot(np.dot(np.dot(transl(0, 0, L[1] + Q[1]),trotz(90)), (trotx(90))))
	H_40 = H_30.dot(trotz(Q[2]).dot(transl(L[2], 0, 0)))
	H_50 = H_40.dot(np.dot(trotz(Q[3]).dot(trotz(90)), trotx(90)))
	H_60 = H_50.dot(np.dot(trotz(Q[4]).dot(transl(0, 0, L[3]+L[4])), trotx(-90)))
	H_E0 = H_60.dot(np.dot(trotz(Q[5]).dot(trotz(-90)), transl(L[5], 0, 0)))
	EE = H_E0[0:3, 3]
	x = np.round(EE[0], 2)
	y = np.round(EE[1], 2)
	z = np.round(EE[2], 2)
	vec = [x, y, z]
	if k==0:
		return vec
	else: 
		return k

res = forwardKinematics(Q, L)
if type(res) == list:
    print("Position of end effector", res)
else:
	print(res)
    





