# Manipulator - ROS Project 
It's a model of Industrial Manipulator KUKA. Full description you can read in File "Robot Description". 
Also this repo contains manipulator control stuff.

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
ROBOT CONTROL: 

1. Run model with controllers:  roslaunch robot_gazebo control.launch
2. Open new terminal window
3. Write command source devel/setup.bash
4. To see movements run rosrun control_pkg main.py
5. ENJOY! 
________________________________________________________________________________________________________________________________

