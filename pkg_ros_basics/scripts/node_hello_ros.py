#!/usr/bin/env python3

import rospy


def main():    
    
    # 1. Make the script a ROS Node.
    rospy.init_node('node_hello_ros', anonymous=True)

    # 2. Print info on console.
    rospy.loginfo("Hello World!")
    
    # 3. Keep the node alive till it is killed by the user.
    rospy.spin()


if __name__ == '__main__':
    try:
        main()
        param_config_my = rospy.get_param('details')

	first_name = param_config_my['name']['first']
	phone = param_config_my['contact']['phone']

    except rospy.ROSInterruptException:
        pass

