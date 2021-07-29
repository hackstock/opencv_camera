#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image

import cv2
from cv_bridge import CvBridge

class ImageViewer(Node):
    def __init__(self):
        super().__init__("image_viewer")
        self.create_subscription(
            Image,
            "image_raw",
            self.on_image_received,
            10
        )

        self.cv_bridge = CvBridge()
        self.get_logger().info("Image viewer node has started...")

    def on_image_received(self, msg):
        frame = self.cv_bridge.imgmsg_to_cv2(msg)
        cv2.imshow("Camera", frame)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    node = ImageViewer()
    try:
        rclpy.spin(node)
    except Exception:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()