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
            try:
                if results.pose_landmarks:
                    landmarks = results.pose_landmarks.landmark

                    shoulder, elbow, wrist, hip, knee = (
                        [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y],
                        [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y],
                        [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y],
                        [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x, landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y],
                        [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x, landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
                    )

                    angle_elbow = calculate_angle(shoulder, elbow, wrist)
                    angle_hip = calculate_angle(shoulder, hip, knee)

                    # Visualize
                    cv2.putText(image, f"Elbow Angle: {angle_elbow:.3f}", tuple(np.multiply(elbow, [int(capture.get(3)), int(capture.get(4))]).astype(int)),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
                    cv2.putText(image, f"Hip Angle: {angle_hip:.3f}", tuple(np.multiply(hip, [int(capture.get(3)), int(capture.get(4))]).astype(int)),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)

                    if angle_elbow > 170:
                        stage = "up"
                    if angle_elbow < 65 and stage == "up" and angle_hip > 150:
                        stage = "down"
                        counter += 1
            except Exception as e:
                print(f"Error: {e}")
            # Render rectangle with a black border
            cv2.rectangle(image, (0, 0), (225, 105), (0, 0, 0), 2)
            cv2.rectangle(image, (0, 0), (225, 105), (58, 152, 250), -1)
