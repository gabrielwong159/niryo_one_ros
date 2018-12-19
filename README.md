# Niryo One
## Pre-requisites
The following installation instructions are obtained from the [original Niryo One README](https://github.com/NiryoRobotics/niryo_one_ros).

You will need:
* Ubuntu 16.04
* ROS Kinetic
* Additional ROS packages
    ```
    sudo apt-get install ros-kinetic-robot-state-publisher ros-kinetic-moveit ros-kinetic-rosbridge-suite ros-kinetic-joy ros-kinetic-ros-control ros-kinetic-ros-controllers ros-kinetic-tf2-web-republisher
    ```
* Additional Python packages
    ```
    sudo -H pip install jsonpickle
    ```

## Setup
### Package installation
```
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
git clone https://github.com/gabrielwong159/niryo_one_ros.git
cd ~/catkin_ws

catkin_make
```

### Additional instructions
Go to `niryo_one_ros/niryo_one_gazebo/worlds/coffee.world` and change the path of the STL files. There should be 4 such files:
* Machine.STL
* Lever.STL
* Capsule.STL (x2)

## Demos
### RViz
#### RViz MotionPlanning
1. Run Niryo One stack on RViz
    ```
    roslaunch niryo_one_bringup desktop_rviz_simulation.launch
    ```
1. Open MotionPlanning in RViz (Displays > Add > MotionPlanning)
1. Move the robot to target position
1. MotionPlanning > Planning > Plan
1. MotionPlanning > Planning > Execute

#### RViz MoveIt! control
```
roslaunch niryo_one_bringup desktop_rviz_simulation.launch
rosrun niryo_one_commander demo.py
```

### Gazebo
#### Simple world simulation
```
roslaunch niryo_one_gazebo niryo_one_gazebo.launch
```

#### Gazebo with RViz
1. Launch Gazebo and RViz
    ```
    roslaunch niryo_one_gazebo niryo_one_gazebo.launch
    rosrun rviz rviz
    ```
1. Displays > Global Options > Fixed Frame: `ground_link`
1. Displays > Add > rviz > RobotModel

Remember to perform the following steps to add RobotModel for all future use of RViz with Gazebo, or you will not be able to see the robot in RViz.

#### Gazebo with joint controllers
```
roslaunch niryo_one_gazebo niryo_one_gazebo.launch
roslaunch niryo_one_control niryo_one_joint_control.launch
rosrun rviz rviz  # optional
rosrun niryo_one_control demo.sh 1.5
```

#### Gazebo with trajectory controllers
```
roslaunch niryo_one_gazebo niryo_one_gazebo.launch
roslaunch niryo_one_control niryo_one_trajectory_control.launch
roslaunch niryo_one_moveit_config move_group.launch
roslaunch niryo_one_moveit_config moveit_rviz.launch
rosrun niryo_one_moveit_commander demo.py
```
