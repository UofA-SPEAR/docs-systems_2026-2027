# Glossary

## General

| Term | Meaning |
|---|---|
| Base station | Operators' laptop and radio setup that controls the rover remotely |
| C2 station | Command and control station where operators run the rover |
| Teleoperation | Driving or controlling the rover manually from the base station |
| URC | University Rover Challenge, the competition the rover is built for |

## Mechanical

| Term | Meaning |
|---|---|
| 6-DOF | Six degrees of freedom; the arm can move and rotate along all three axes |

## Electrical

| Term | Meaning |
|---|---|
| EtherCAT | Wired network that carries commands from the Jetson to the motor drivers |
| GMSL2 | High-speed camera link between the cameras and the capture card |
| Jetson | NVIDIA onboard computer that runs the rover's software |

## Science

| Term | Meaning |
|---|---|

## Software

| Term | Meaning |
|---|---|
| ArUco marker | Printed square pattern the cameras detect to find posts and align with targets |
| Behavior Tree | Structure the Mission Controller uses to order and switch between tasks |
| EKF | Extended Kalman Filter; combines sensor data to estimate the rover's position |
| GNSS | Satellite positioning (includes GPS) used for absolute rover location |
| GStreamer | Video streaming framework used to show camera feeds in the GUI |
| IK | Inverse kinematics; calculates joint angles needed to place the arm's tool at a target |
| MoveIt | Motion planning framework that plans collision-free arm movements |
| Nav2 | ROS 2 navigation stack that plans and drives paths autonomously |
| Network Manager | Node that routes data between the rover and base station over the radios |
| Node | One independent program in ROS 2, handling a single job |
| Odometry | Estimate of how far and in which direction the rover has moved |
| Point cloud | 3D set of points from the stereo cameras describing the surroundings |
| PySide6 / Qt | Framework used to build the operator GUI |
| ROS 2 | Robot Operating System 2; the framework all rover software is built on |
| ROS 2 Control | Layer that converts motion commands into signals for the actuators |
| SLAM | Simultaneous Localization and Mapping; builds a map while tracking the rover's position in it |
| Topic | Named channel ROS 2 nodes use to send and receive data |
| URDF | File describing the rover's geometry, used by the software |
| YOLO | Object detection model used to find mission objects in camera images |
| ZED SDK | Stereolabs software for the ZED cameras, including depth and SLAM |
| ZED Wrapper | ROS 2 node that publishes ZED camera images and point clouds |

## Admin

| Term | Meaning |
|---|---|
