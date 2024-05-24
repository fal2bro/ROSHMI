#!/usr/bin/env python3

import rospy
import myDynamixel
import time

Motor_Velocity = -50

dxl = myDynamixel.Dxlfunc()
MotorNum = dxl.init('COM
