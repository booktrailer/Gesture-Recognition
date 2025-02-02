import cv2
import mediapipe as mp
from check_functions import *
import os

os.makedirs('save_frames', exist_ok=True)


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # make it mirror
    frame = cv2.flip(frame, 1)

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    #guesture list
    cv2.putText(frame, "Current Recognizable Gestures:", (700,430),cv2.FONT_HERSHEY_DUPLEX, 1, (255,255,0),2)
    cv2.putText(frame, "high five", (700,470),cv2.FONT_HERSHEY_PLAIN, 2, (255,255,0),2)
    cv2.putText(frame, "thumbs up", (700,500),cv2.FONT_HERSHEY_PLAIN, 2, (255,255,0),2)
    cv2.putText(frame, "thumbs down", (700,530),cv2.FONT_HERSHEY_PLAIN, 2, (255,255,0),2)
    cv2.putText(frame, "flip off", (700,560),cv2.FONT_HERSHEY_PLAIN, 2, (255,255,0),2)
    cv2.putText(frame, "finger up", (700,590),cv2.FONT_HERSHEY_PLAIN, 2, (255,255,0),2)
    cv2.putText(frame, "finger down", (700,620),cv2.FONT_HERSHEY_PLAIN, 2, (255,255,0),2)
    cv2.putText(frame, "peace sign", (700,650),cv2.FONT_HERSHEY_PLAIN, 2, (255,255,0),2)
    cv2.putText(frame, "(press q to quit)", (700,680),cv2.FONT_HERSHEY_PLAIN, 2, (255,255,0),2)

    
    if results.multi_hand_landmarks:

        for i in range(len(results.multi_hand_landmarks)):
            hand_landmarks = results.multi_hand_landmarks[i]

            x = 0
            if i == 0:
                x = 50
            else:
                x = 550

            # Draw hand landmarks
            cv2.putText(frame, hand_direction(hand_landmarks.landmark), (x, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            #location
            cv2.putText(frame, "Wrist y: " + str(hand_landmarks.landmark[0].y), (x, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(frame, "Wrist x: " + str(hand_landmarks.landmark[0].x), (x, 385), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            #draw the connections
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)


            if is_thumbs_up(hand_landmarks.landmark):
                cv2.putText(frame, "Thumbs Up!", (x, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
            if is_thumbs_down(hand_landmarks.landmark):
                cv2.putText(frame, "Thumbs Down!", (x, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
            if is_flip_off(hand_landmarks.landmark):
                cv2.putText(frame, "kill yourself", (x, 135), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
            if is_finger_up(hand_landmarks.landmark):
                cv2.putText(frame, "the sky is up", (x, 170), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
            if is_finger_down(hand_landmarks.landmark):
                cv2.putText(frame, "the ground is down", (x, 170), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
            if is_high_five(hand_landmarks.landmark):
                cv2.putText(frame, "High Five!", (x, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
            if is_peace_sign(hand_landmarks.landmark):
                cv2.putText(frame, "Peace Sign!", (x, 230), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)


    # display the frame
    cv2.imshow("Gesture Recognition", frame)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    if key == ord(' '):
        filename = f'save_frames/frame_{frame_count}.png'
        cv2.imwrite(filename, frame)
        cv2.putText(frame, "Frame Saved!", (650, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv2.imshow("Gesture Recognition", frame)
        cv2.waitKey(500)
    
    frame_count += 1

cap.release()
cv2.destroyAllWindows()

