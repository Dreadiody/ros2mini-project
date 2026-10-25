import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess, IncludeLaunchDescription, RegisterEventHandler
from launch.event_handlers import OnProcessExit
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    pkg = get_package_share_directory('robot_arm_urdf')
    xacro_file = os.path.join(pkg, 'urdf', 'robot_arm_urdf.urdf.xacro')
    robot_description = ParameterValue(Command(['xacro ', xacro_file]), value_type=str)

    rsp = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description, 'use_sim_time': True}],
    )

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')
        )
    )

    spawn = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-topic', 'robot_description', '-entity', 'robot_arm_urdf'],
        output='screen',
    )

    load_jsb = ExecuteProcess(
        cmd=['ros2', 'control', 'load_controller', '--set-state', 'active', 'joint_state_broadcaster'],
        output='screen',
    )
    load_arm = ExecuteProcess(
        cmd=['ros2', 'control', 'load_controller', '--set-state', 'active', 'arm_controller'],
        output='screen',
    )
    load_hand = ExecuteProcess(
        cmd=['ros2', 'control', 'load_controller', '--set-state', 'active', 'hand_controller'],
        output='screen',
    )

    return LaunchDescription([
        rsp,
        gazebo,
        spawn,
        RegisterEventHandler(OnProcessExit(target_action=spawn, on_exit=[load_jsb])),
        RegisterEventHandler(OnProcessExit(target_action=load_jsb, on_exit=[load_arm])),
        RegisterEventHandler(OnProcessExit(target_action=load_arm, on_exit=[load_hand])),
    ])
