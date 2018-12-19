#!/usr/bin/env python
# http://docs.ros.org/kinetic/api/moveit_tutorials/html/doc/robot_model_and_robot_state/robot_model_and_robot_state_tutorial.html
import rospy
import moveit_commander
import moveit_msgs
import geometry_msgs

rospy.init_node('move_group_python_interface_tutorial',
                anonymous=True)

robot = moveit_commander.RobotCommander()

group_name = 'arm'
group = moveit_commander.MoveGroupCommander(group_name)


def print_info():
    # We can get the name of the reference frame for this robot:
    planning_frame = group.get_planning_frame()
    print "============ Reference frame: %s" % planning_frame

    # We can also print the name of the end-effector link for this group:
    eef_link = group.get_end_effector_link()
    print "============ End effector: %s" % eef_link

    # We can get a list of all the groups in the robot:
    group_names = robot.get_group_names()
    print "============ Robot Groups:", robot.get_group_names()

    # Sometimes for debugging it is useful to print the entire state of the
    # robot:
    print "============ Printing robot state"
    print robot.get_current_state()
    print ""


def move_joint(x, y=None, z=None, roll=None, pitch=None, yaw=None):
    """
    Receives values for joint movement.
    Input can either be a list, tuple, or 6 separate values:
        move_joint([a, b, c, d, e, f])
        move_joint(a, b, c, d, e, f)
    """
    if isinstance(x, list) or isinstance(x, tuple):
        assert len(x) == 6, 'Joint goal should contain 6 values, received: %s' % len(x)
        joint_goal = x
    else:
        joint_goal = [x, y, z, roll, pitch, yaw]
    group.go(joint_goal, wait=True)
    group.stop()
    return joint_goal


def move_goal(position, orientation):
    """
    position: (x, y, z)
    orientation: (x, y, z, w)
    """
    pose_goal = geometry_msgs.msg.Pose()

    x, y, z = position
    pose_goal.position.x = x
    pose_goal.position.y = y
    pose_goal.position.z = z

    x, y, z, w = orientation
    pose_goal.orientation.x = x
    pose_goal.orientation.y = y
    pose_goal.orientation.z = z
    pose_goal.orientation.w = w

    group.set_pose_target(pose_goal)
    group.go(wait=True)
    group.stop()
    group.clear_pose_targets()
    return pose_goal

if __name__ == '__main__':
    print_info()
    print '\nPose\n', group.get_current_pose().pose
    print '\nMove\n', move_goal([0, 0.2, 0], [0, 0, 0, 0])
    print '\nMove\n', move_goal([-0.07, -0.17, 0.3], [0, 0.37, 0, 0.929])

