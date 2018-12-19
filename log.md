# Niryo One
> [Niryo One GitHub](https://github.com/NiryoRobotics/niryo_one_ros)

Records of current changes to the default Niryo One files for Gazebo simulation and control.

## Test installation
### RViz MotionPlanning
1. Run Niryo One stack on RViz
    ```
    roslaunch niryo_one_bringup desktop_rviz_simulation.launch
    ```
1. Open MotionPlanning in RViz (Displays > Add > MotionPlanning)
1. Move the robot to target position
1. MotionPlanning > Planning > Plan
1. MotionPlanning > Planning > Execute

### MoveIt! Python script
1. Move Python script `demo.py` to `niryo_one_ros/niryo_one_commander/scripts`
1. Set executable permissions for `demo.py`
    ```
    chmod +x demo.py
    ```

#### Launch
```
roslaunch niryo_one_bringup desktop_rviz_simulation.launch
rosrun niryo_one_commander demo.py
```

## Gazebo
### Create Gazebo
1. Create `niryo_one_gazebo` folder
1. Create `CMakeLists.txt` and `package.xml` files with [RRBot](https://github.com/ros-simulation/gazebo_ros_demos/tree/kinetic-devel/rrbot_gazebo) as reference
1. Create `niryo_one_gazebo/worlds` folder and add `coffee.world`
1. Create `niryo_one_gazebo/launch` folder and add `niryo_one_gazebo.launch`
1. Replace `niryo_one_description/urdf/v1/niryo_one.urdf.xacro` with new file
1. Change path of STL files in `niryo_one.urdf.xacro`
1. Add `niryo_one_description/meshes/stl` folder
1. Add `niryo_one_description/meshes/v1/stl/effector_link.stl`

#### Launch
```
roslaunch niryo_one_gazebo niryo_one_gazebo.launch
```

## ROS Control and MoveIt!
> [Guide](https://github.com/ahoarau/mekabot/wiki/ros_control-and-MoveIt!)

### Setup
1. Create `niryo_one_control` folder
1. Create `CMakeLists.txt` and `package.xml` files
1. Add `niryo_one_control/config/controllers.yaml` file
1. Add `niryo_one_control/launch` files
1. Add `niryo_one_control/scripts/demo.sh` file

### RViz
1. Launch Gazebo and RViz
    ```
    roslaunch niryo_one_gazebo niryo_one_gazebo.launch
    rosrun rviz rviz
    ```
1. Displays > Global Options > Fixed Frame: `ground_link`
1. Displays > Add > rviz > RobotModel

Any changes to the robot state in Gazebo should be reflected in RViz.

### Joint controllers
#### Launch
```
roslaunch niryo_one_gazebo niryo_one_gazebo.launch
roslaunch niryo_one_control niryo_one_joint_control.launch
rosrun rviz rviz  # optional
rosrun niryo_one_control demo.sh 1.5
```

### Trajectory controller
1. Change topic name in `niryo_one_moveit_config/config/controllers.yaml`
    ```
    - name: "/niryo_one/niryo_one_follow_joint_trajectory_controller"
    ```

#### Launch
```
roslaunch niryo_one_gazebo niryo_one_gazebo.launch
roslaunch niryo_one_control niryo_one_trajectory_control.launch
roslaunch niryo_one_moveit_config move_group.launch
roslaunch niryo_one_moveit_config moveit_rviz.launch
rosrun niryo_one_moveit_commander demo.py
```
