[![Build Status](https://travis-ci.org/rodosha98/ManipulatorUpgraded.svg?branch=badges)](https://travis-ci.org/rodosha98/ManipulatorUpgraded)
[![MIT license](http://img.shields.io/badge/license-MIT-brightgreen.svg?branch=badges)](http://opensource.org/licenses/MIT)
[![Issues](http://img.shields.io/github/issues/USER/REPO.svg?branch = badges)]( https://github.com/rodosha98/ManipulatorUpgraded/issues )

# Manipulator - ROS Project 
It's a model of Industrial Manipulator KUKA. Full description you can read in File "Robot Description". 
Also this repo contains manipulator control stuff.
________________________________________________________________________________________________________________________________
``` bash
ROBOT DESCRIPTION
```
How to run project:
1. Open Linux console
2. Create workspace folder (Example: mkdir -p manipulator_control/src)
3. Go to workspace folder (cd manipulator_control_ws)
4. Go to src and put there 3 packages (control_pkg, robot_description, robot_gazebo)
6. return to manipulator_control_ws/ and launch catkin_make 
7. Write command source devel/setup.bash
________________________________________________________________________________________________________________________________
IF you want to see the model:
1. Use that command to launch RVIZ: roslaunch robot_gazebo rviz.launch
2. Run model in GAZEBO: roslaunch robot_gazebo begin.launch
3. Enjoy!
________________________________________________________________________________________________________________________________
``` bash
ROBOT CONTROL: 
```
In control package there added python script camera.py, which moves the 8-th joint of the robot.

1. Run model with controllers:  roslaunch robot_gazebo control.launch
2. Open new terminal window
3. Write command source devel/setup.bash
4. To see movements run rosrun control_pkg main.py
5. ENJOY! 
________________________________________________________________________________________________________________________________
``` bash
CAMERA Project:
```
In control package there added python script camera.py, which moves the 6-th joint of the robot and collect images from the camera, which is mounted on robot. Also there are new folder images.

YoutubeLink on video: https://www.youtube.com/watch?v=-XRLZpmvfpM&feature=youtu.be

Also I've assigned colours to links

Run project:
To run camera project write in terminal: roslaunch robot_gazebo camera.launch
________________________________________________________________________________________________________________________________
``` bash 
TESTS
```

To check the correctness of progtams and interaction 2 type of tests are added.
``` bash
Part 1. Unit test
```
I've created unit test to check Forward Kinematics algorithm on me manipulator. I've implemented 8 tests inside the unit test in which I checked the functionality of the function, taking into account the limits of the joints and the lengths of the links. The lengths cannot be negative, and the variable joints go beyond the established boundaries as in a real robot. In this case, the function returns nothing and the test checks this.
To run unit test use command:

1. rosrun tests unitTest.py

OR use Rostest launch using unit.test launch file
1. Add in CMake in robot_gazebo folder:
if(CATKIN_ENABLE_TESTING)
	find_package(rostest REQUIRED)
	add_rostest(launch/unit.test) # This is the path to the unit test
endif()
2. catkin_make run_tests && catkin_test_results

Second approach is better

``` bash
Part 2. Integration test
```

In the integration test, we must check the joint work of several modules of the system, I check the operation of the controllers and the work of publishers. Through publishers, the robot enters the preset position (initial) and remains in it. (since the robot can move independently due to gravity). Subscribers must confirm that the robot is in the correct position. Then it will be possible to conclude that the system is working correctly.
In this way, you can check any position of the robot by changing the publisher’s commands.

To run integrate test use command:
1. Add to Cmake path to integration test
if(CATKIN_ENABLE_TESTING)
	find_package(rostest REQUIRED)
	add_rostest(launch/unit.test)
	add_rostest(launch/integration.test)
endif()
2. catkin_make run_tests && catkin_test_results. It launches all tests you havw that had written in the CMake launch (important) 

As a result you will see, that all you tests passed or not.
________________________________________________________________________________________________________________________________
``` bash
Continious integration in Travis (CI)
```

Continous integration is the practice of merging in small code changes frequently. The goal is to build healthier software by developing and testing in smaller increments.

With Travis Each commit will be accompanied by a cloud build. On special badges the build status will be displayed: red means there are errors, green means everything is fine.
