# webcam_ws
This repository consists of a ros2 package which consists of two nodes under the path webcam_ws/src/opencv_tools/opencv_tools. 
The imagepub.py node publishes the node on the topic "topic_webcam", and the node imagesub.py subscribes to the node on the topic "topic_webcam".
The subscribed video feed can be changed depending on the user input. It consists of 2 modes:
Mode 1: Greyscale 
Mode 2: Color
If the user presses "1" on the video feed, it will get changed to Greyscale and similarly, if the user presses "2" the feed will get converted to RGB.
After cloning the workspace, source the workspace, and launch both nodes simultaneously on different terminals after sourcing.
