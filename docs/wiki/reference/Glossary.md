# Glossary

## General

| Term | Meaning | Also used by |
|---|---|---|
| **Competition** | | |
| URC | University Rover Challenge, the competition the rover is built for | |
| **Operations** | | |
| Base station | Operators' laptop and radio setup that controls the rover remotely | |
| C2 station | Command and control station where operators run the rover | |
| Teleoperation | Driving or controlling the rover manually from the base station | |

## Mechanical

| Term | Meaning | Also used by |
|---|---|---|
| **Arm** | | |
| 6-DOF | Six degrees of freedom; the arm moves and rotates along all three axes | Software |

## Electrical

| Term | Meaning | Also used by |
|---|---|---|
| **Compute** | | |
| Jetson | NVIDIA onboard computer that runs the rover's software | Software |
| **Connections** | | |
| EtherCAT | Wired network carrying commands from the Jetson to the motor drivers | Software |
| GMSL2 | High-speed camera link between the cameras and the capture card | Software |

## Science

| Term | Meaning | Also used by |
|---|---|---|

## Software

| Term | Meaning | Also used by |
|---|---|---|
| **Arm Control** | | |
| IK | Inverse kinematics; calculates joint angles to place the arm's tool at a target | |
| MoveIt | Motion planning framework for collision-free arm movements | |
| **Framework** | | |
| Node | One independent program in ROS 2, handling a single job | |
| ROS 2 | Robot Operating System 2; the framework all rover software is built on | |
| ROS 2 Control | Converts motion commands into signals for the actuators | Electrical |
| Topic | Named channel ROS 2 nodes use to send and receive data | |
| URDF | File describing the rover's geometry | Mechanical |
| **Mission** | | |
| Behavior Tree | Structure the Mission Controller uses to order and switch tasks | |
| Network Manager | Routes data between the rover and base station over the radios | Electrical |
| **Navigation** | | |
| EKF | Extended Kalman Filter; combines sensor data to estimate position | |
| GNSS | Satellite positioning (includes GPS) for absolute rover location | |
| Nav2 | ROS 2 navigation stack that plans and drives paths autonomously | |
| Odometry | Estimate of how far and in which direction the rover has moved | |
| SLAM | Builds a map while tracking the rover's position in it | |
| **Operator Interface** | | |
| GStreamer | Video streaming framework for camera feeds in the GUI | |
| PySide6 / Qt | Framework used to build the operator GUI | |
| **Vision** | | |
| ArUco marker | Printed square pattern the cameras detect to find and align with targets | |
| Point cloud | 3D set of points from the stereo cameras describing the surroundings | |
| YOLO | Object detection model for finding mission objects in images | |
| ZED SDK | Stereolabs software for the ZED cameras, including depth and SLAM | |
| ZED Wrapper | ROS 2 node that publishes ZED camera images and point clouds | |

## Admin

| Term | Meaning | Also used by |
|---|---|---|
