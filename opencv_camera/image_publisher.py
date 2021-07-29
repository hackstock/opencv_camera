#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image

import cv2
from cv_bridge import CvBridge


class ImagePublisher(Node):
    def __init__(self):
        super().__init__("image_publisher")
        self.publisher = self.create_publisher(
            Image,
            "image_raw",
            10
        )

        self.create_timer(
            0.1,
            self.publish_frame
        )

        self.cap = cv2.VideoCapture(0)
        self.cv_bridge = CvBridge()
        self.get_logger().info("Image publisher node has started...")

    def publish_frame(self):
        ret, frame = self.cap.read()
        if ret:
            self.publisher.publish(
                self.cv_bridge.cv2_to_imgmsg(frame)
            )

def main(args=None):
    rclpy.init(args=args)
    node = ImagePublisher()
    try:
        rclpy.spin(node)
    except Exception:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()