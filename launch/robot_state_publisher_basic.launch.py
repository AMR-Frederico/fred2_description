#!/usr/bin/env python3

import launch_ros.descriptions
import launch_ros
import launch
import os

from launch.substitutions import Command, LaunchConfiguration
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import TimerAction, LogInfo



def generate_launch_description():
    pkg_share = launch_ros.substitutions.FindPackageShare(package='fred2_description').find('fred2_description')
    default_model_path = os.path.join(pkg_share, 'src/description/fred_basic_shape.urdf')
    default_rviz_config_path = os.path.join(pkg_share, 'rviz/urdf.rviz')


    robot_state_publisher_node = launch_ros.actions.Node(
        
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': launch_ros.descriptions.ParameterValue(
            launch.substitutions.Command(['xacro ', os.path.join(pkg_share, 'src/description/fred_basic_shape.urdf')]),
            value_type=str
        )}, 
        {'use_sim_time': False},
        
        ],
    )



    joint_state_publisher = launch_ros.actions.Node(

        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        output='screen',
        parameters=[{'use_sim_time': False}],
    )


    return launch.LaunchDescription([

        TimerAction(period= 1.5, actions= [
            
            LogInfo(msg=' ####################### LAUNCHING ROBOT STATE PUBLISHER #################################### '), 
            robot_state_publisher_node
        ]),


        TimerAction(period= 1.5, actions= [
            
            LogInfo(msg=' ####################### LAUNCHING JOINT STATE PUBLISHER #################################### '), 
            joint_state_publisher
        ])
        
    ])
