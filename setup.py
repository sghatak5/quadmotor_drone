from setuptools import find_packages, setup
import os

package_name = 'quadmotor_drone'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), ['launch/rviz.launch.py']),
        (os.path.join('share', package_name, 'urdf'), ['urdf/drone.urdf.xacro']),
        #(os.path.join('share', package_name, 'rviz'), ['rviz/drone.rviz']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sghatak5',
    maintainer_email='sagnikghatak22@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    entry_points={
        'console_scripts': []
    },
)
