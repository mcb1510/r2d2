import rclpy

from std_msgs.msg import String


def main(args=None):
    rclpy.init(args=args)

    node = rclpy.create_node('sos_publisher')
    publisher = node.create_publisher(String, 'my_topic', 10)

    msg = String()
    
    def timer_callback():
        msg.data = 'ObiWan Kenobi, please help me. You\'re my only hope'
        node.get_logger().info('Publishing sos message: "%s"' % msg.data)
        publisher.publish(msg)

    timer_period = 1.1# seconds
    timer = node.create_timer(timer_period, timer_callback)

    rclpy.spin(node)

    # Destroy the timer attached to the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()