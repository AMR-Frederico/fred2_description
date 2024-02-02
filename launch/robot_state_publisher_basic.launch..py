#!/usr/bin/env python3

import launch
from launch.substitutions import Command, LaunchConfiguration
import launch_ros
import os
import launch_ros.descriptions

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import TimerAction, LogInfo


def generate_launch_description():
    pkg_share = launch_ros.substitutions.FindPackageShare(package='fred2_description').find('fred2_description')

    robot_state_publisher_node = launch_ros.actions.Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': launch_ros.descriptions.ParameterValue( launch.substitutions.Command(['xacro ',os.path.join(pkg_share,'src/description/fred_basic_shape.urdf')]), value_type=str)  }]    )
    

    return LaunchDescription([

        TimerAction(period= 1.5, actions= [
            
            LogInfo(msg=' ######################### LAUNCHING ROBOT DESCRIPTION #################################### '), 
            robot_state_publisher_node
        ])
    ])