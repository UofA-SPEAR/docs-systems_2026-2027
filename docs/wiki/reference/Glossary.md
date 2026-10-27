# Glossary

[General](#general) · [Mechanical](#mechanical) · [Electrical](#electrical) · [Science](#science) · [Software](#software) · [Admin](#admin)

## General

| Term | Meaning |
|---|---|
| **Base station** | Operators' laptop and radio setup that controls the rover remotely |
| **C2 station** | Command and control station where operators run the rover |
| **Teleoperation** | Driving or controlling the rover manually from the base station |
| **URC** | University Rover Challenge, the competition the rover is built for |

## Mechanical

### Arm

| Term | Meaning |
|---|---|
| **6-DOF** | Six degrees of freedom; the arm can move and rotate along all three axes. *Also used by: Software* |

## Electrical

### Compute

| Term | Meaning |
|---|---|
| **Jetson** | NVIDIA onboard computer that runs the rover's software. *Also used by: Software* |

### Connections

| Term | Meaning |
|---|---|
| **EtherCAT** | Wired network that carries commands from the Jetson to the motor drivers. *Also used by: Software* |
| **GMSL2** | High-speed camera link between the cameras and the capture card. *Also used by: Software* |

## Science

| Term | Meaning |
|---|---|

## Software

### Framework

| Term | Meaning |
|---|---|
| **Node** | One independent program in ROS 2, handling a single job |
| **ROS 2** | Robot Operating System 2; the framework all rover software is built on |
| **ROS 2 Control** | Layer that converts motion commands into signals for the actuators. *Also used by: Electrical* |
| **Topic** | Named channel ROS 2 nodes use to send and receive data |
| **URDF** | File describing the rover's geometry, used by the software. *Also used by: Mechanical* |

### Navigation and Localization

| Term | Meaning |
|---|---|
| **EKF** | Extended Kalman Filter; combines sensor data to estimate the rover's position |
| **GNSS** | Satellite positioning (includes GPS) used for absolute rover location |
| **Nav2** | ROS 2 navigation stack that plans and drives paths autonomously |
| **Odometry** | Estimate of how far and in which direction the rover has moved |
| **SLAM** | Simultaneous Localization and Mapping; builds a map while tracking the rover's position in it |

### Vision

| Term | Meaning |
|---|---|
| **ArUco marker** | Printed square pattern the cameras detect to find posts and align with targets |
| **Point cloud** | 3D set of points from the stereo cameras describing the surroundings |
| **YOLO** | Object detection model used to find mission objects in camera images |
| **ZED SDK** | Stereolabs software for the ZED cameras, including depth and SLAM |
| **ZED Wrapper** | ROS 2 node that publishes ZED camera images and point clouds |

### Arm Control

| Term | Meaning |
|---|---|
| **IK** | Inverse kinematics; calculates joint angles needed to place the arm's tool at a target |
| **MoveIt** | Motion planning framework that plans collision-free arm movements |

### Mission and Communication

| Term | Meaning |
|---|---|
| **Behavior Tree** | Structure the Mission Controller uses to order and switch between tasks |
| **Network Manager** | Node that routes data between the rover and base station over the radios. *Also used by: Electrical* |

### Operator Interface

| Term | Meaning |
|---|---|
| **GStreamer** | Video streaming framework used to show camera feeds in the GUI |
| **PySide6 / Qt** | Framework used to build the operator GUI |

## Admin

| Term | Meaning |
|---|---|
