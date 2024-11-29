import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
  
class ImageSubscriber(Node):
  
    def __init__(self):
        super().__init__('image_subscriber')
        self.subscription = self.create_subscription(
            Image, 
            'topic_webcam', 
            self.listener_callback, 
            10)
        self.subscription  
        self.br = CvBridge()
        self.display_mode = "RGB"  # Default display mode is RGB
    
    def listener_callback(self, data):
        self.get_logger().info('Receiving video frame')
        # Convert ROS Image message to OpenCV image
        current_frame = self.br.imgmsg_to_cv2(data)
        
        # Display based on the current mode
        if self.display_mode == "RGB":
            display_frame = current_frame
        elif self.display_mode == "GRAYSCALE":
            display_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
        
        cv2.imshow("camera", display_frame)
        key = cv2.waitKey(1)  # Capture key presses
        
        # Check for mode switching keys
        if key == ord('1'):
            self.get_logger().info('Switched to Grayscale mode')
            self.display_mode = "GRAYSCALE"
        elif key == ord('2'):
            self.get_logger().info('Switched to RGB mode')
            self.display_mode = "RGB"
   
def main(args=None):
    rclpy.init(args=args)
    image_subscriber = ImageSubscriber()
    rclpy.spin(image_subscriber)
    image_subscriber.destroy_node()
    rclpy.shutdown()
   
if __name__ == '__main__':
    main()