import cv2 
import mediapipe as mp 

# Initialize Mediapipe Face Detection
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# Start video capture
cap = cv2.VideoCapture(0)  # Use 0 for the default camera, or replace with a video file path

with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            break

        # Convert the image color space from BGR to RGB
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Process the image and find faces
        results = face_detection.process(image_rgb)

        # Draw face detections on the image
        if results.detections:
            for detection in results.detections:
                mp_drawing.draw_detection(image, detection)

        # Display the image
        cv2.imshow('Face Detection', image)

        # Break the loop on pressing 'q'
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

# Release resources
cap.release()
cv2.destroyAllWindows()
