import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

class JoyListener(Node):
    def __init__(self):
        super().__init__('joy_listener')
        self.create_subscription(Joy, '/joy', self.cb_joy, 10)
        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.get_logger().info('JoyListener iniciado: botón 0 → +0.3 m/s, botón 1 → -0.3 m/s')

    def cb_joy(self, msg: Joy):
        cmd = Twist()
        # Botón 0 (e.g. “A”) adelante, botón 1 (e.g. “B”) atrás
        if len(msg.buttons) > 0 and msg.buttons[0] == 1:
            cmd.linear.x = 0.3
        elif len(msg.buttons) > 1 and msg.buttons[1] == 1:
            cmd.linear.x = -0.3
        else:
            cmd.linear.x = 0.0
        # Siempre angular 0
        cmd.angular.z = 0.0

        self.cmd_pub.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    node = JoyListener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()