import launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    publisher=Node(
        package='pub_sub',
        executable='pub',
        name='Publisher_node',
        )
    
    subcriber=Node(
        package='pub_sub', #package name
        executable='sub', #executable name
        name='Subscriber_Node',  #node name
        )
    
    return LaunchDescription([
        publisher,
        subcriber
    ])