# The ROS2 OpenCV Camera Package
This is a ROS2 package with a publisher node that uses OpenCV to 
publish raw images from a camera onto a topic called `image_raw`.
Since the package is based on OpenCV, any camera that's supported 
in OpenCV can be used with this package. And because this package publishes raw camera images, it can be used as the foundation for all computer vision related aspects of your robotics project.

Features : 
- publishing of raw camera images
- configurable camera id (you can specify which camera to publish from)
- image viewer subscriber for visualizing the published images

## Topics

- /image_raw - topic for raw image data published as `sensor_msgs.msg import Image`

## Publishers

- image_publisher - publishes raw camera images. `ros2 run opencv_camera image_publisher`

## Subscribers

- image_viewer - subscribes to `/image_raw` and shows the received image frames. `ros2 run opencv_camera image_viewer`

# Installation
- clone this repository into your ROS2 workspace
- cd into the `src` folder of your workspance
- run `colcon build`
- source `setup.bash` and `local_setup.bash`

# Dependencies
This package depends on OpenCV so if that's not already installed on your system, run `pip install opencv-python` to install it.
