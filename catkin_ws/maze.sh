#!/bin/bash
source /opt/ros/kinetic/setup.bash
source ~/devel/setup.bash

xterm -e "roslaunch drone_gazebo PathPlanningMaze.launch"
