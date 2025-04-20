from setuptools import find_packages, setup
# Add these for launch file
import os
from glob import glob

package_name = 'pub_sub'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        # for launch u need to add these directories
        (os.path.join('share', package_name, 'launch/'),
         glob('launch/*launch.[pxy][yma]*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pratheekpoojary',
    maintainer_email='pratheekpoojary@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pub = pub_sub.pub:main',
            'sub = pub_sub.sub:main',
        ],
    },
)
