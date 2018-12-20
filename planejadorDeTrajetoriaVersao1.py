#! /usr/bin/env python

# import ros stuff
import rospy
from geometry_msgs.msg import Point
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
from gazebo_msgs.msg import ModelState
from gazebo_msgs.srv import SetModelState
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf import transformations
from std_srvs.srv import *

import math

position_ = Point()
initial_position_ = Point()
initial_position_.x = rospy.get_param('initial_x')
initial_position_.y = rospy.get_param('initial_y')
initial_position_.z = 0
desired_position_ = Point()
desired_position_.x = rospy.get_param('des_pos_x')
desired_position_.y = rospy.get_param('des_pos_y')
desired_position_.z = 0

active_ = False
pub_ = None
regions_ = {
        'right': 0,
        'fright': 0,
        'front': 0,
        'fleft': 0,
        'left': 0,
}
state_ = 3
state_dict_ = {
    0: 'default',
    1: 'distanciaGrande1',
    2: 'distanciaGrande2',
    3: 'distanciaGrande3',
    4: 'distanciaMedia1',
    5: 'distanciaMedia2',
    6: 'distanciaMedia3',
    7: 'distanciaPequemed1',
    8: 'distanciaPequemed2',
    9: 'distanciaPequemed3',
    10: 'distanciaPequena1',
    11: 'distanciaPequena2',
    12: 'distanciaPequena3',
    13: 'distanciaPequena4',
}

def wall_follower_switch(req):
    global active_
    active_ = req.data
    res = SetBoolResponse()
    res.success = True
    res.message = 'Done!'
    return res

def clbk_laser(msg):
    global regions_
    regions_ = {
        'right':  min(min(msg.ranges[0:143]), 14),
        'fright': min(min(msg.ranges[144:287]), 14),
        'front':  min(min(msg.ranges[288:431]), 14),
        'fleft':  min(min(msg.ranges[432:575]), 14),
        'left':   min(min(msg.ranges[576:719]), 14),
    }
    
    take_action()

def change_state(state):
    global state_, state_dict_
    if state is not state_:
        print 'Wall follower - [%s] - %s' % (state, state_dict_[state])
        state_ = state

def take_action():
    global regions_
    regions = regions_
    msg = Twist()
    linear_x = 0
    angular_z = 0
    
    state_description = ''
    
    d = 1.0
    
    if position_.x == desired_position_.x and position_.y == desired_position_.y:
        rospy.loginfo("Cheguei na posicao")
    
    elif regions['front'] <= 14 and regions['front'] > 12:
      #caso1
      if position_.x - desired_position_.x >= 0.36 and position_.y - desired_position_.y >= 0.36 and position_.x - desired_position_.x < 0.64 and position_.y - desired_position_.y < 0.64:
        state_description = 'distanciaGrande1'
        change_state(1)
      #caso2
      elif position_.x - desired_position_.x >= 0.64 and position_.y - desired_position_.y >= 0.64 and position_.x - desired_position_.x < 0.98 and position_.y - desired_position_.y < 0.98:
        state_description = 'distanciaGrande2'
        change_state(2)
      elif position_.x - desired_position_.x >= 0.98 and position_.y - desired_position_.y >= 0.98 and position_.x - desired_position_.x < 1.50 and position_.y - desired_position_.y < 1.50:
        state_description = 'distanciaGrande3'
        change_state(3)
      else:
        state_description = 'default'
        change_state(0)
    
    elif regions['front'] <= 12 and regions['front'] > 8:
      if position_.x - desired_position_.x >= 0.36 and position_.y - desired_position_.y >= 0.36 and position_.x - desired_position_.x < 0.64 and position_.y - desired_position_.y < 0.64:
        state_description = 'distanciaMedia1'
        change_state(4)
      elif position_.x - desired_position_.x >= 0.64 and position_.y - desired_position_.y >= 0.64 and position_.x - desired_position_.x < 0.98 and position_.y - desired_position_.y < 0.98:
        state_description = 'distanciaMedia2'
        change_state(5)
      elif position_.x - desired_position_.x >= 0.98 and position_.y - desired_position_.y >= 0.98 and position_.x - desired_position_.x < 1.50 and position_.y - desired_position_.y < 1.50:
        state_description = 'distanciaMedia3'
        change_state(6)
      else:
        state_description = 'default'
        change_state(0)
    
    elif regions['front'] <= 8 and regions['front'] > 4:
      if position_.x - desired_position_.x >= 0.36 and position_.y - desired_position_.y >= 0.36 and position_.x - desired_position_.x < 0.64 and position_.y - desired_position_.y < 0.64:
        state_description = 'distanciaPequemed1'
        change_state(7)
      elif position_.x - desired_position_.x >= 0.64 and position_.y - desired_position_.y >= 0.64 and position_.x - desired_position_.x < 0.98 and position_.y - desired_position_.y < 0.98:
        state_description = 'distanciaPequemed2'
        change_state(8)
      elif position_.x - desired_position_.x >= 0.98 and position_.y - desired_position_.y >= 0.98 and position_.x - desired_position_.x < 1.50 and position_.y - desired_position_.y < 1.50:
        state_description = 'distanciaPequemed3'
        change_state(9)
      else:
        state_description = 'default'
        change_state(0)
        
    elif regions['front'] <= 4 and regions['front'] >= 1:
      if position_.x - desired_position_.x >= 0.36 and position_.y - desired_position_.y >= 0.36 and position_.x - desired_position_.x < 0.64 and position_.y - desired_position_.y < 0.64:
        state_description = 'distanciaPequena1'
        change_state(10)
      elif position_.x - desired_position_.x >= 0.64 and position_.y - desired_position_.y >= 0.64 and position_.x - desired_position_.x < 0.98 and position_.y - desired_position_.y < 0.98:
        state_description = 'distanciaPequena2'
        change_state(11)
      elif position_.x - desired_position_.x >= 0.98 and position_.y - desired_position_.y >= 0.98 and position_.x - desired_position_.x < 1.50 and position_.y - desired_position_.y < 1.50:
        state_description = 'distanciaPequena3'
        change_state(12)
      else:
        state_description = 'distanciaPequena4'
        change_state(13)
        
    else:
        state_description = 'caso nao encontrado ERRO'
        rospy.loginfo(regions)

def distanciaPequemed1():
    msg = Twist()
    msg.linear.x = 0.2
    return msg

def distanciaPequemed2():
    msg = Twist()
    msg.linear.x = 0.4
    return msg

def distanciaPequemed3():
    msg = Twist()
    msg.linear.x = 0.6
    return msg
    

def distanciaPequena1():
    msg = Twist()
    msg.linear.x = 0.2
    msg.angular.z = -0.36
    return msg

def distanciaPequena2():
    msg = Twist()
    msg.linear.x = 0.2
    msg.angular.z = 0.64 
    return msg

def distanciaPequena3():
    msg = Twist()
    msg.linear.x = 0.2
    msg.angular.z = 0.64
    return msg
    
def distanciaPequena4():
    msg = Twist()
    msg.linear.x = 0.2
    msg.angular.z = -0.75
    return msg
    
def distanciaMedia1():
    msg = Twist()
    msg.linear.x = 0.6
    return msg

def distanciaMedia2():
    msg = Twist()
    msg.linear.x = 0.8
    return msg

def distanciaMedia3():
    msg = Twist()
    msg.linear.x = 1.0
    return msg
    
def distanciaGrande1():
    msg = Twist()
    msg.linear.x = 1.0
    return msg

def distanciaGrande2():
    msg = Twist()
    msg.linear.x = 1.2
    return msg
    
def distanciaGrande3():
    msg = Twist()
    msg.linear.x = 1.4
    return msg

def caso_default(): #longe do objetivo
    msg = Twist()
    msg.linear.x = 1.8
    return msg
    
#def find_wall(): #vira a direita
 #   msg = Twist()
  #  msg.linear.x = 0.2
   # msg.angular.z = -0.3
    #return msg

#def turn_left(): # vira a esquerda
 #   msg = Twist()
  #  msg.angular.z = 0.3
   # return msg

#def follow_the_wall(): # segue o obstaculo ate sair dele
 #   global regions_
    
  #  msg = Twist()
   # msg.linear.x = 0.5
    #return msg

def main():
    global pub_, active_
    
    rospy.init_node('reading_laser')
    
    pub_ = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    
    sub = rospy.Subscriber('/m2wr/laser/scan', LaserScan, clbk_laser)
    
    srv = rospy.Service('wall_follower_switch', SetBool, wall_follower_switch)
    
    rate = rospy.Rate(20)
    while not rospy.is_shutdown():
        if not active_:
            rate.sleep()
            continue
        
        msg = Twist()
        if state_ ==   0:
            msg = caso_default()
        elif state_ == 1:
            msg = distanciaGrande1()
        elif state_ == 2:
            msg = distanciaGrande2()
            #pass
        elif state_ == 3:
            msg = distanciaGrande3()
        elif state_ == 4:
            msg = distanciaMedia1()
        elif state_ == 5:
            msg = distanciaMedia2()
        elif state_ == 6:
            msg = distanciaMedia3()
        elif state_ == 7:
            msg = distanciaPequemed1()
        elif state_ == 8:
            msg = distanciaPequemed2()
        elif state_ == 9:
            msg = distanciaPequemed3()
        elif state_ == 10:
            msg = distanciaPequena1()
        elif state_ == 11:
            msg = distanciaPequena2()
        elif state_ == 12:
            msg = distanciaPequena3()
        elif state_ == 13:
            msg = distanciaPequena4()
        else:
            rospy.logerr('Unknown state!')
        
        pub_.publish(msg)
        
        rate.sleep()

if __name__ == '__main__':
    main()