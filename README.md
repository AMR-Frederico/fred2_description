
# Fred -Robot Description
**note: Package for ROS 2 - Python (CMake) based package**

The `fred2_description` package in ROS 2 is dedicated to creating and launching the robot description for simulation and real-world applications. It utilizes URDF files, Xacro, and launch files to represent the robot's structure and visualize it in tools like RViz.


## Installation

**1. Clone the repository into your ROS2 workspace:**

```bash
cd ros2_ws/src
git clone https://github.com/AMR-Frederico/fred2_description.git
```

**2. Build the package:**

```bash
cd ros2_ws
colcon build
```

## Usage

### Launch the URDF model:

**Basic URDF with Robot State Publisher:**


```
ros2 launch fred2_description robot_state_publisher_basic.launch.py
```


**URDF with Robot State Publisher and RViz:**

```
ros2 launch fred2_description robot_state_publisher_rviz.launch.py
```


**Complete URDF with STL Pieces for Simulation:**

```
ros2 launch fred2_description robot_state_publisher_simulation.launch.py
```

---

## Robot state publisher

The robot_state_publisher node is responsible for publishing the robot's joint state and transforms. It reads the URDF file and broadcasts the joint states to the TF tree.

**Type:** python

**Name:** robot_state_publisher

### Parameters:

`robot_description:` Absolute path to the robot's URDF file.

### Topics: 

**Subscribers:** None

**Publishers:**

`/joint_states` (*sensor_msgs/JointState*): Joint states of the robot.


## Joint state publisher
The joint_state_publisher node allows you to interactively change the joint values of the robot for testing and visualization.

**Type:** python

**Name:** joint_state_publisher

### Arguments:

`model:` Absolute path to the robot's URDF file.


### Topics: 

**Subscribers:** None

**Publishers:**

`/joint_states` (*sensor_msgs/JointState*): Joint states of the robot.
Condition: Launches only if the gui argument is not provided.


## Joint state publisher GUI 

The joint_state_publisher_gui node provides a graphical interface to interactively change the joint values of the robot for testing and visualization.

**Type:** python

**Name:** joint_state_publisher_gui

**Condition:** Launches only if the gui argument is provided.

**Subscribers:** None

**Publishers:** None

## rviz2
The rviz2 node launches the RViz visualization tool to display the robot model and sensor information.

**Type:** ros2/rviz2

**Name:** rviz2

### Arguments:

`-d`: Absolute path to the RViz configuration file.


### Topics: 

**Subscribers:** None

**Publishers:** None

---

## Launch

**Default Launch:**

```
ros2 launch fred2_description robot_state_publisher_rviz.launch.py
```

**Launch for the robot:**

```
ros2 launch fred2_description robot_state_publisher.launch.py
```


**Launch with GUI:**

```
ros2 launch fred2_description robot_state_publisher_rviz.launch.py gui:=True
```

## Models

The package includes different URDF files representing the robot in various configurations. These models are suitable for different use cases:

`fred_basic_shape.urdf:` Basic URDF with simple forms for basic visualization.

`fred_simplificated.urdf`: URDF with STL pieces, without colision properties.

`fred_description.urdf`: URDF with STL pieces for simulation.
