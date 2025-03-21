# Voice Controller GUI

This is a simple bot controller. Bot will move according to your direction.

## Installation and Setup

## 1. Clone the Repository
#### (i) Create a workspace (e.g., `voice_controller_ws`)
#### (ii) Inside the `src` folder, clone the repository  
#### Run the following terminal commands:
```bash
cd ~/voice_controller_ws/src
git clone https://github.com/sksakib01/voice_controller.git
```
## 2. Build the Package
#### (i) Inside the workspace, build the package using catkin_make:
```bash
cd ~/voice_controller_ws
catkin_make
```
## 3. Source the Workspace and Run
#### Source the workspace in the terminal:

```bash
source ~/voice_controller_ws/devel/setup.bash
```
#### Go through the scripts folder in the project file control
#### Make Python file executable
```bash
chmod +x commandrec.py
chmod +x sendingcommand.py
```
#### Then, run the two Python files:
```bash
rosrun control data_publisher.py
rosrun control sendingcommand.py
```
## Important packages and dependencies
#### ROS
#### SpeechRecognition and PyAudio
#### TurtleBot3 (if running with Gazebo)
#### roslaunch and rosrun utilities
