#!/usr/bin/env python3

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
import os

def generate_launch_description():
    #Define paths
    packageName = "quadmotor_drone"
    urdfFile = "urdf/drone.urdf.xacro"
    rvizConfigFile = "rviz/drone.rviz"

    #Find package paths
    urdfPath = os.path.join(FindPackageShare(packageName).find(packageName), urdfFile)
    rvizPath = os.path.join(FindPackageShare(packageName).find(packageName), rvizConfigFile)

    return LaunchDescription([
        DeclareLaunchArgument("model", default_value=urdfPath, description="Absolute path to urdf file"),
        DeclareLaunchArgument("rviz", default_value=rvizPath, description="Absolute path to rviz config file"),
        
        #Creates a Robot State Publisher node to load URDF model into a ROS2 parameter server
        Node(
            package="robot_state_publisher", 
            executable="robot_state_publisher",
            output="screen",
            parameters=[{'robot_description': Command(['xacro ', LaunchConfiguration("model")])}],
        ),

        Node(
            package = "joint_state_publisher",
            executable = "joint_state_publisher",
            output = "screen"
        ),

        #Start Rviz with the URDF model and RVIZ config file
        Node(
            package="rviz2",
            executable="rviz2",
            output="screen",
            arguments=["-d", LaunchConfiguration("rviz")]
        )
    ])

