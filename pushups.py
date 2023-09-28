import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

def calculate_angle(a, b, c):
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle_degrees = np.abs(np.degrees(radians))
    return angle_degrees if angle_degrees <= 180 else 360 - angle_degrees
def main():
    stage, counter = None, 0
    angle_elbow, angle_hip = 0, 0  # Initialize these variables

    # Video Feed
    output_video = cv2.VideoWriter('output_pushups.avi', cv2.VideoWriter_fourcc(*'MJPG'), 20.0, (640, 480))
    capture = cv2.VideoCapture(0)

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while capture.isOpened():
            ret, frame = capture.read()

            # Recolour image
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            # Make detection
            results = pose.process(image)

            # Recolour back to RGB
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
