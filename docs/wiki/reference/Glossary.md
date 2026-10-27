# Glossary

## General

| Term | Meaning | Also used by |
|---|---|---|
| **Control** | | |
| Autonomous | The rover acts on its own, with no one driving it | Software |
| Teleoperation | Someone drives or controls the rover remotely, like a remote-control car | Software |

## Safety

| Term | Meaning | Also used by |
|---|---|---|
| **Batteries** | | |
| LiPo | Lithium polymer battery: light and powerful, but can catch fire if punctured, overcharged, or shorted | Electrical |
| Thermal runaway | A battery overheating uncontrollably, which can lead to fire | Electrical |
| **Chemicals** | | |
| Chemical Safety Plan | The plan describing how each chemical is transported, stored, used, and disposed of | Science |
| Cradle to grave | Tracking a chemical from purchase until it is safely disposed of | Science |
| SDS | Safety Data Sheet: the manufacturer's document on a chemical's hazards and handling | Science |
| **Equipment** | | |
| E-stop | Emergency stop: a button or command that immediately cuts the rover's movement | Electrical, Software |
| PPE | Personal protective equipment, such as safety glasses and gloves | All |

## Mechanical

| Term | Meaning | Also used by |
|---|---|---|
| **Arm** | | |
| 6-DOF | The arm can move in 6 independent ways: up/down, left/right, forward/back, plus three rotations | Software |

## Electrical

| Term | Meaning | Also used by |
|---|---|---|
| **Compute** | | |
| Jetson | The rover's main onboard computer, made by NVIDIA | Software |
| **Connections** | | |
| EtherCAT | A wired network that carries movement commands from the computer to the motors | Software |
| GMSL2 | A type of cable connection that carries high-quality camera video | Software |
| **Radio** | | |
| 2.4 GHz band | A crowded radio range also used by Wi-Fi; good range, but shared with many devices | Software |
| 5 GHz band | A radio range that carries more data than 2.4 GHz but over shorter distances | Software |
| FCC Part 15 | The US rules on how strong radios can be without a license | |
| Ham license | An amateur radio license that allows using stronger radio signals | |
| Repeater | A device placed between the rover and base station to pass the signal along and extend range | Mechanical |

## Science

| Term | Meaning | Also used by |
|---|---|---|
| **Life Detection** | | |
| Bioassay | A test that reacts only to substances made by living things | |
| Biomolecule | A molecule that comes from living things, such as proteins or DNA | |
| Life detection | Looking for evidence of actual living things, not just conditions where life could exist | |
| **Sampling** | | |
| Caliche | A hard, cement-like layer of soil | Mechanical |
| Cross-contamination | When material from one sample gets mixed into another, spoiling the results | Mechanical |
| In-situ | Taken from where it naturally is, not moved or prepared beforehand | |
| Specific sample | A sample from one known spot and depth, rather than soil mixed from several places | |

## Software

| Term | Meaning | Also used by |
|---|---|---|
| **Arm Control** | | |
| IK | Inverse kinematics: working out how to bend each arm joint so the hand reaches a target | Mechanical |
| MoveIt | Software that plans arm movements so the arm doesn't hit anything | |
| **Framework** | | |
| Node | One small program on the rover that does a single job | |
| ROS 2 | The software framework all the rover's programs are built on; lets them talk to each other | |
| ROS 2 Control | The part of the software that turns movement commands into signals for the motors | Electrical |
| Topic | A named channel programs use to send each other data, like a group chat | |
| URDF | A file that describes the rover's shape and parts so the software knows its layout | Mechanical |
| **Mission Logic** | | |
| Behavior Tree | A flowchart-like structure that decides what the rover does next | |
| Network Manager | The program that handles sending data between the rover and the base station | Electrical |
| **Navigation** | | |
| CORS | Online stations that improve GPS accuracy; need internet, so unusable in the field | |
| DEM | Digital Elevation Model: a map showing the height of the ground | |
| EKF | Extended Kalman Filter: combines several sensors to estimate where the rover is | |
| GNSS | Satellite positioning; GPS is one example | Electrical |
| LIDAR | A sensor that uses lasers to measure distances and map surroundings | Electrical |
| Magnetometer | A digital compass that senses direction from magnetic fields | Electrical |
| Nav2 | Software that plans a path and drives the rover along it on its own | |
| Odometry | Estimating how far the rover has moved by tracking its wheels and motion | |
| RTK GNSS | A more precise form of GPS that uses a second receiver at a known spot | Electrical |
| SLAM | Building a map of the area while working out where the rover is on it | |
| **Operator Interface** | | |
| GStreamer | Software that streams camera video to the operators' screen | |
| PySide6 / Qt | The toolkit used to build the operators' control screen | |
| **Vision** | | |
| ArUco marker | A black-and-white square pattern the cameras can recognize, like a simple QR code | |
| Gesture recognition | Software that understands body movements seen by a camera | |
| Point cloud | A 3D map made of many dots, built from camera depth data | |
| Stereo camera | A camera with two lenses that judges distance, like human eyes | Electrical |
| YOLO | Software that spots and labels objects in camera images | |
| ZED SDK | The software that comes with the ZED cameras, providing depth and mapping | |
| ZED Wrapper | The program that passes ZED camera data to the rest of the rover's software | |

## Admin

| Term | Meaning | Also used by |
|---|---|---|
| **Budget** | | |
| Cost cap | The most the rover (plus drone and base station items) is allowed to cost | All |
| Project Budget Table | A summary of spending submitted with the design reviews | |
| Rover Expense Report | A detailed record of every expense, proving the rover stays under the cost cap | |
| **Planning** | | |
| Gantt chart | A timeline chart showing tasks, how long they take, and when they're due | |
| WBS | Work Breakdown Structure: splitting a project into smaller and smaller parts | |
