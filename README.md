# Real-Time-Car-Detection-OpenCV-Python

This project demonstrates real-time car detection in video footage using OpenCV and Haar Cascade classifiers. The system identifies and tracks cars, highlighting them with bounding boxes for visualization.

Features
Real-time car detection in video footage
Utilizes Haar Cascade classifiers for vehicle recognition
Highlights detected cars with bounding boxes
Adjustable frame skipping for performance optimization
Technologies Used
Python
OpenCV

Installation
Clone the repository:

bash
git clone https://github.com/your-repository/real-time-car-detection.git
cd real-time-car-detection
Set up a virtual environment and install dependencies:

bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install opencv-python
Ensure you have the Haar Cascade XML file (cars.xml) in the project directory.

Run the detection script:

bash
python detect_cars.py
The video will play, and detected cars will be highlighted with bounding boxes. Press q to quit the video playback.

Files
detect_cars.py: Main script for car detection
cars.xml: Haar Cascade XML file for car detection
data/video1.avi: Sample video file for testing

How It Works
Load Video: The script loads the specified video file.
Frame Skipping: Processes every third frame to optimize performance.
Grayscale Conversion: Converts each frame to grayscale for better detection.
Car Detection: Uses Haar Cascade classifiers to detect cars in the frame.
Drawing Bounding Boxes: Highlights detected cars with red bounding boxes.
Display Result: Shows the processed frame in a window.

Acknowledgments
OpenCV for providing tools for computer vision tasks.
Haar Cascades for object detection.
