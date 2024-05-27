from setuptools import setup

setup(
    name='mypkg',
    version='0.0.0',
    packages=['mypkg'],
    install_requires=[
        'myDynamixel==2.0.7',
        'numpy',
        'dynamixel-sdk>=3'
    ],
    
    author='Nozomu Arai',
    author_email='arai261@stu.kanazawa-u.ac.jp',
    description='mydynamixel for ros',
    license='BSD',
    keywords='ROS',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Your License',
        'Operating System :: OS Independent',
    ],
)

