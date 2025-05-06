import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy

class JoyListener(Node):
    def __init__(self):
        super().__init__('joy_listener')
        self.create_subscription(Joy, '/joy', self.cb_joy, 10)

    def cb_joy(self, msg):
        self.get_logger().info(f"Axes: {msg.axes}  Btns: {msg.buttons}")

def main(args=None):
    rclpy.init(args=args)
    node = JoyListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()