#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int64
import myDynamixel
import time

Motor_Velocity = -50
rospy.init_node('dynamixeltest')
pub = rospy.Publisher('Dynamixelinfo', Int64, queue_size=1)
dxl = myDynamixel.Dxlfunc()

MotorNum = dxl.init('/dev/ttyUSB0', baudrate=57600)

if MotorNum > 0:
    pub.publish(1)
else:
    pub.publish(0)

Motor_ID = 1
dxl.write(Motor_ID, dxl.Address.TorqueEnable, False)
dxl.Change_OperatingMode(Motor_ID, dxl.operating_mode.velocity_control)
dxl.write(Motor_ID, dxl.Address.TorqueEnable, True)
dxl.write(Motor_ID, dxl.Address.GoalVelocity, Motor_Velocity)
time.sleep(5)
Velocity = dxl.read(Motor_ID, dxl.Address.PresentVelocity)
pub.publish(Velocity)
time.sleep(5)
dxl.write(Motor_ID, dxl.Address.TorqueEnable, False)
dxl.exit()

