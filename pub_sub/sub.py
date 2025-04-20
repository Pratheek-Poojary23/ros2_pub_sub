import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Subscriber(Node):
    def __init__(self):
        super().__init__("Subscriber_Node")
        self.subscription=self.create_subscription(String,"topic",self.subscription_callback,10)
    
    def subscription_callback(self,msg):
        self.get_logger().info(f"Receiving {msg.data}")


def main():
    rclpy.init()
    node=Subscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ =="__main__":
    main()