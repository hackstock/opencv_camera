from setuptools import setup

package_name = 'opencv_camera'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Edward Pie',
    maintainer_email='hackstockpie@gmail.com',
    description='Publishes raw camera images using OpenCV',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'image_publisher = opencv_camera.image_publisher:main',
            'image_viewer = opencv_camera.image_viewer:main'
        ],
    },
)
