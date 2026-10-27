# Glossary

| Term | Meaning | Subteam |
|---|---|---|
| 6-DOF | Six degrees of freedom; the arm can move and rotate along all three axes | Mechanical, Software |
| ArUco marker | Printed square pattern the cameras detect to find posts and align with targets | Software |
| Base station | Operators' laptop and radio setup that controls the rover remotely | Software, Electrical |
| Behavior Tree | Structure the Mission Controller uses to order and switch between tasks | Software |
| C2 station | Command and control station where operators run the rover | Software |
| EKF | Extended Kalman Filter; combines sensor data to estimate the rover's position | Software |
| EtherCAT | Wired network that carries commands from the Jetson to the motor drivers | Electrical, Software |
| GMSL2 | High-speed camera link between the cameras and the capture card | Electrical |
| GNSS | Satellite positioning (includes GPS) used for absolute rover location | Software |
| GStreamer | Video streaming framework used to show camera feeds in the GUI | Software |
| IK | Inverse kinematics; calculates joint angles needed to place the arm's tool at a target | Software |
| Jetson | NVIDIA onboard computer that runs the rover's software | Software, Electrical |
| MoveIt | Motion planning framework that plans collision-free arm movements | Software |
| Nav2 | ROS 2 navigation stack that plans and drives paths autonomously | Software |
| Network Manager | Node that routes data between the rover and base station over the radios | Software |
| Node | One independent program in ROS 2, handling a single job | Software |
| Odometry | Estimate of how far and in which direction the rover has moved | Software |
| Point cloud | 3D set of points from the stereo cameras describing the surroundings | Software |
| PySide6 / Qt | Framework used to build the operator GUI | Software |
| ROS 2 | Robot Operating System 2; the framework all rover software is built on | Software |
| ROS 2 Control | Layer that converts motion commands into signals for the actuators | Software, Electrical |
| SLAM | Simultaneous Localization and Mapping; builds a map while tracking the rover's position in it | Software |
| Teleoperation | Driving or controlling the rover manually from the base station | Software |
| Topic | Named channel ROS 2 nodes use to send and receive data | Software |
| URC | University Rover Challenge, the competition the rover is built for | All |
| URDF | File describing the rover's geometry, used by the software | Software |
| YOLO | Object detection model used to find mission objects in camera images | Software |
| ZED SDK | Stereolabs software for the ZED cameras, including depth and SLAM | Software |
| ZED Wrapper | ROS 2 node that publishes ZED camera images and point clouds | Software |
