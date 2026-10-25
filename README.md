# ROS 2 Mini Project — Robot Arm URDF

ROS 2 Humble project containing a robot arm description, RViz2 visualization launch, TF-tree evidence, screenshots, and a demonstration video.

## Model

- `world` is the root reference frame, fixed to `base_link`.
- `joint_1` through `joint_5` are revolute arm joints.
- `joint_6` and `joint_7` are prismatic gripper-finger joints.
- STL meshes provide the robot links' visual and collision geometry.

## Build and visualize

On Ubuntu 22.04 with ROS 2 Humble and the package dependencies installed:

```bash
source /opt/ros/humble/setup.bash
cd ~/moveit2_ws
colcon build --packages-select robot_arm_urdf
source install/setup.bash
ros2 launch robot_arm_urdf display.launch.py
```

The display launch opens RViz2 and the Joint State Publisher GUI for visual joint-state changes.

## Package contents

- `robot_arm_urdf/`: Xacro model, meshes, configuration, and ROS 2 launch files.
- `report.pdf`: project questions, answers, joint table, and evidence.
- `report.html`: editable report source.
- `frames_2026-10-25_06.02.41.pdf`: TF frame report.
- `screenshots/`: RViz2, TF tree, and source excerpts.
- `videos/robot_arm_demo.webm`: demonstration recording.

The included Gazebo control plugin and Gazebo launch file target Gazebo Classic.
