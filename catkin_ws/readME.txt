ROS version:
-ROS kinetic run on Ubuntu 16.04.

Commands to install extra ROS packages:
-sudo apt-get install ros-kinetic-hector-*
-sudo apt-get install ros-kinetic-hardware-interface
-sudo apt-get install ros-kinetic-controller-interface
-sudo apt-get install ros-kinetic-gazebo-ros-control
-sudo apt-get install ros-kinetic-gmapping
-sudo apt-get install ros-kinetic-amcl
-sudo apt-get install ros-kinetic-move-base
-sudo apt-get install ros-kinetic-map-server
-sudo apt-get install ros-kinetic-dwa-local-planner
-sudo apt-get install ros-kinetic-teleop-twist-keyboard

After installing all the packages and ROS with gazebo run catkin_make command in terminal that has navigated into the catkin_ws folder of the project.
Every time a new terminal is opened ensure that it is in the catkin_ws folder and you run the following command before anything else:
-source devel/setup.bash

Launch files that launch specific world and functionality:

SLAM:
-roslaunch drone_gazebo SLAM.launch                                  (loads world with drone and rviz)

-rosservice call /enable_motors “enable: true”                      (drone take off commands)
-rosrun drone_control takeoff.py

-rosrun teleop_twist_keyboard teleop_twist_keyboard.py     (allows drone to be manually controlled)


PathPlanning:

All path planning files require the same steps after loading the worold:

-roslaunch drone_gazebo PathPlanningMaze.launch OR PathPlanningObs.launch OR PathPlanning.launch         

-rosservice call /enable_motors “enable: true” 
-rosrun drone_control takeoff.py         

To set nav goal for drone use the 2d nav goal in rviz and set it on the map for the drone to navigate to:

For more clarity in using commands you may refer to the user manual provided in the report, or you can contact me at arslan.nazir.2018@live.rhul.ac.uk

BUGS:
BUG 1: Only error so far noted is that when the drone is given a goal after taking off, if the goal is too close to a wall it gets stuck in a loop and keeps taking off and launching again. 
SOLUTION: To solve this either try placing another nav goal, or restart the simulation.




