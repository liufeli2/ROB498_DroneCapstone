jetson@nano:~$ ros2 topic info -v "/mavros/imu/data"
Type: sensor_msgs/msg/Imu

Publisher count: 1

Node name: imu
Node namespace: /mavros
Topic type: sensor_msgs/msg/Imu
Endpoint type: PUBLISHER
GID: 01.0f.d7.4b.81.50.ad.86.01.00.00.00.00.00.8d.03.00.00.00.00.00.00.00.00
QoS profile:
  Reliability: RMW_QOS_POLICY_RELIABILITY_BEST_EFFORT
  Durability: RMW_QOS_POLICY_DURABILITY_VOLATILE
  Lifespan: 2147483651294967295 nanoseconds
  Deadline: 2147483651294967295 nanoseconds
  Liveliness: RMW_QOS_POLICY_LIVELINESS_AUTOMATIC
  Liveliness lease duration: 2147483651294967295 nanoseconds

Subscription count: 0

--------------------------

jetson@nano:~$ ros2 topic info -v "/mavros/vision_pose/pose"
Type: geometry_msgs/msg/PoseStamped

Publisher count: 0

Subscription count: 1

Node name: vision_pose
Node namespace: /mavros
Topic type: geometry_msgs/msg/PoseStamped
Endpoint type: SUBSCRIPTION
GID: 01.0f.d7.4b.81.50.ad.86.01.00.00.00.00.01.1c.04.00.00.00.00.00.00.00.00
QoS profile:
  Reliability: RMW_QOS_POLICY_RELIABILITY_RELIABLE
  Durability: RMW_QOS_POLICY_DURABILITY_VOLATILE
  Lifespan: 2147483651294967295 nanoseconds
  Deadline: 2147483651294967295 nanoseconds
  Liveliness: RMW_QOS_POLICY_LIVELINESS_AUTOMATIC
  Liveliness lease duration: 2147483651294967295 nanoseconds

---------------------------
jetson@nano:~$ ros2 topic info -v "/mavros/setpoint_position/local"
Type: geometry_msgs/msg/PoseStamped

Publisher count: 0

Subscription count: 1

Node name: setpoint_position
Node namespace: /mavros
Topic type: geometry_msgs/msg/PoseStamped
Endpoint type: SUBSCRIPTION
GID: 01.0f.d7.4b.81.50.ad.86.01.00.00.00.00.00.c9.04.00.00.00.00.00.00.00.00
QoS profile:
  Reliability: RMW_QOS_POLICY_RELIABILITY_BEST_EFFORT
  Durability: RMW_QOS_POLICY_DURABILITY_VOLATILE
  Lifespan: 2147483651294967295 nanoseconds
  Deadline: 2147483651294967295 nanoseconds
  Liveliness: RMW_QOS_POLICY_LIVELINESS_AUTOMATIC
  Liveliness lease duration: 2147483651294967295 nanoseconds

----------------------------

jetson@nano:~$ ros2 topic info -v "/vicon/ROB498_Drone/ROB498_Drone"
Type: geometry_msgs/msg/PoseStamped

Publisher count: 1

Node name: vicon_client
Node namespace: /
Topic type: geometry_msgs/msg/PoseStamped
Endpoint type: PUBLISHER
GID: 01.0f.9f.e0.8b.3a.12.2a.01.00.00.00.00.00.1a.03.00.00.00.00.00.00.00.00
QoS profile:
  Reliability: RMW_QOS_POLICY_RELIABILITY_RELIABLE
  Durability: RMW_QOS_POLICY_DURABILITY_VOLATILE
  Lifespan: 2147483651294967295 nanoseconds
  Deadline: 2147483651294967295 nanoseconds
  Liveliness: RMW_QOS_POLICY_LIVELINESS_AUTOMATIC
  Liveliness lease duration: 2147483651294967295 nanoseconds

Subscription count: 0



----------------------------


vicon (processed)
Position: x=0.3733230261373949, y=0.4261296018065068, z=0.027844524678396324
Orientation: x=-0.012163230149627372, y=0.04449411931635693, z=0.9863827407925292, w=0.15786518883277345
Timestamp: 1740156570.27055376
Frame ID: ROB498_Drone/ROB498_Drone

realsense
header:
  stamp:
    sec: 1740157512
    nanosec: 863638528
  frame_id: odom_frame
child_frame_id: camera_pose_frame
pose:
  pose:
    position:
      x: -0.009451478719711304
      y: -0.03495466336607933
      z: -0.00022792984964326024
    orientation:
      x: 0.005711567588150501
      y: 0.0202382430434227
      z: -0.09548740833997726
      w: 0.9952085614204407
  covariance:
  - 0.1
  - 0.0
  - 0.0
  - 0.0
  - 0.0
  - 0.0
  - 0.0
  - 0.1
  - 0.0
  - 0.0
  - 0.0
  - 0.0
  - 0.0
  - 0.0
  - 0.1
  - 0.0
  - 0.0
  - 0.0
  - 0.0
  - 0.0
  - 0.0
  - 0.001
  - 0.0
  - 0.0
  - 0.0
  - 0.0
  - 0.0
  - 0.0
  - 0.001
  - 0.0
  - 0.0
  - 0.0
  - 0.0
  - 0.0
  - 0.0
  - 0.001
twist:
  twist:
    linear:
      x: 0.007998393104054757
      y: -0.0102199788249091
      z: 0.007182180928679173
    angular:
      x: -0.010747638842260022
      y: 0.004091490835956978
      z: -0.0025083696083936916
  covariance:
  - 0.1
  - 0.0
  - 0.0
  - 0.0
  - 0.0
  - 0.0
  - 0.0
  - 0.1
  - 0.0
  - 0.0
  - 0.0
  - 0.0
  - 0.0
  - 0.0
  - 0.1
  - 0.0
  - 0.0
  - 0.0
  - 0.0
  - 0.0
  - 0.0
  - 0.001
  - 0.0
  - 0.0
  - 0.0
  - 0.0
  - 0.0
  - 0.0
  - 0.001
  - 0.0
  - 0.0
  - 0.0
  - 0.0
  - 0.0
  - 0.0
  - 0.001