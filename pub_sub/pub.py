import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SimplePublisher(Node):
    def __init__ (self):
        super().__init__("Publisher_node")
        self.publisher_ = self.create_publisher(String, "topic",10)
        self.timer = self.create_timer(2,self.timer_callback)
        self.count=0

    def timer_callback(self):
        msg=String()
        msg.data=f"Hello everyone {self.count}"
        self.count +=1
        self.publisher_.publish(msg)
        self.get_logger().info(f"Publishing {msg.data}")

def main():
    rclpy.init()
    node=SimplePublisher()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ =="__main__":
    main()