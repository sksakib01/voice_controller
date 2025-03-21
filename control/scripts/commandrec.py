#!/usr/bin/env python3

import speech_recognition as sr
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist


initial_energy = 50


def control_function(msg):
    global initial_energy
    str = msg.data.lower()
    velocity = Twist()

    if str == "stop":
        velocity.linear.x = 0
        velocity.angular.z = 0
        pub.publish(velocity)
        rospy.loginfo("Bot stopped.")
        return


    if initial_energy > 0:
        if str == "forward":
            velocity.linear.x = 0.5
            pub.publish(velocity)

            rospy.sleep(2)

            velocity.linear.x = 0
            pub.publish(velocity)
            initial_energy -= 10

        elif str == "forward 5s":
            velocity.linear.x = 0.5
            pub.publish(velocity)

            rospy.sleep(5)
            velocity.linear.x = 0
            pub.publish(velocity)
            initial_energy -= 10

        elif str in ["backward", "back"]:
            velocity.linear.x = -0.5
            pub.publish(velocity)

            rospy.sleep(2)

            velocity.linear.x = 0
            pub.publish(velocity)
            initial_energy -= 10

        elif str == "right":
            velocity.angular.z = 0.3
            pub.publish(velocity)

            rospy.sleep(2)

            velocity.angular.z = 0
            pub.publish(velocity)
            initial_energy -= 10

        elif str == "left":
            velocity.angular.z = -0.3
            pub.publish(velocity)

            rospy.sleep(2)

            velocity.angular.z = 0
            pub.publish(velocity)
            initial_energy -= 10

        print(initial_energy)
        
    elif str in ["heal", "kaboom"]:
        initial_energy = 50
        rospy.loginfo("Energy Restored!!")

    else:
        rospy.logwarn("Low energy.......")
        velocity.linear.x = 0
        velocity.angular.z = 0
        pub.publish(velocity)



if __name__ == "__main__":
    rospy.init_node("controlNode", anonymous=False)
    
    pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
    sub = rospy.Subscriber("command_control", String, control_function)

    
    rospy.spin()