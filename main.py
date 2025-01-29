import cv2
import mediapipe as mp
from check_functions import *

# Initialize Mediapipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils


# Start Video Capture
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Flip the frame horizontally for a mirror-like effect
    frame = cv2.flip(frame, 1)
    
    # Convert frame to RGB for Mediapipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    cv2.putText(frame, "Current Recognizable Gestures:", (700,480),cv2.FONT_HERSHEY_DUPLEX, 1, (255,255,0),2)
    cv2.putText(frame, "thumbs up", (700,530),cv2.FONT_HERSHEY_PLAIN, 2, (255,255,0),2)
    cv2.putText(frame, "thumbs down", (700,560),cv2.FONT_HERSHEY_PLAIN, 2, (255,255,0),2)
    cv2.putText(frame, "flip off", (700,590),cv2.FONT_HERSHEY_PLAIN, 2, (255,255,0),2)
    cv2.putText(frame, "(press q to quit)", (700,620),cv2.FONT_HERSHEY_PLAIN, 2, (255,255,0),2)

    
    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks
            cv2.putText(frame, hand_direction(hand_landmarks.landmark), (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            cv2.putText(frame, "Wrist y: " + str(hand_landmarks.landmark[0].y), (75, 125), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(frame, "Wrist x: " + str(hand_landmarks.landmark[0].x), (75, 175), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            if is_thumbs_up(hand_landmarks.landmark):
                cv2.putText(frame, "Thumbs Up!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            if is_thumbs_down(hand_landmarks.landmark):
                cv2.putText(frame, "Thumbs Down!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            if is_flip_off(hand_landmarks.landmark):
                cv2.putText(frame, "kill yourself", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)


    # Display the frame
    cv2.imshow("Simple Gesture Recognition", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
        break

cap.release()
cv2.destroyAllWindows()
