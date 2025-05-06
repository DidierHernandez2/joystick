import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # 1) El driver oficial joy_node
        Node(
            package='joy',
            executable='joy_node',
            name='joy_node',
            output='screen',
            # si tu dispositivo es distinto a /dev/input/js0, ajústalo aquí:
            parameters=[{ 'dev': '/dev/input/js0' }]
        ),

        # 2) Tu listener personalizado
        Node(
            package='joystick',
            executable='joy_listener',
            name='joy_listener',
            output='screen',
            remappings=[
                # opcional si quieres remapear el topic
                # ('/joy','/my_joy')
            ]
        ),
    ])