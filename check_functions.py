def hand_direction(landmarks):
    # Get wrist and middle joint location
    wrist_x = landmarks[0].x
    wrist_y = landmarks[0].y

    middle_joint_x = landmarks[13].x
    middle_joint_y = landmarks[13].y

    # Calculate the slope 
    if wrist_x != middle_joint_x:
        slope = (middle_joint_y - wrist_y) / (middle_joint_x - wrist_x)
    else:
        slope = None

    # Determine the direction
    if slope is None:  # Vertical line
        return "up" if wrist_y > middle_joint_y else "down"
    elif abs(slope) > 1:  # Steep slope (vertical-ish)
        return "up" if wrist_y > middle_joint_y else "down"
    else:  # Shallow slope (horizontal-ish)
        return "left" if wrist_x > middle_joint_x else "right"

def is_thumbs_up(landmarks):

    thumb_tip_y = landmarks[4].y
    thumb_joint_y = landmarks[3].y

    if thumb_tip_y < thumb_joint_y:
        if hand_direction(landmarks) == "left":
            # make sure other fingers are not extended
            other_fingers_extended = (
                landmarks[8].x > landmarks[6].x and  # Index finger
                landmarks[12].x > landmarks[10].x and  # Middle finger
                landmarks[16].x > landmarks[14].x and  # Ring finger
                landmarks[20].x > landmarks[18].x     # Pinky
            )
            return other_fingers_extended 
        
        elif hand_direction(landmarks) == "right":
            # make sure other fingers are not extended
            other_fingers_extended = (
                landmarks[8].x < landmarks[6].x and  # Index finger
                landmarks[12].x < landmarks[10].x and  # Middle finger
                landmarks[16].x < landmarks[14].x and  # Ring finger
                landmarks[20].x < landmarks[18].x     # Pinky
            )
            return other_fingers_extended 
        

    return False 

def is_thumbs_down(landmarks):

    thumb_tip_y = landmarks[4].y
    thumb_joint_y = landmarks[3].y


    if thumb_tip_y > thumb_joint_y:
        if hand_direction(landmarks) == "left":

            other_fingers_extended = (
                landmarks[8].x > landmarks[6].x and  
                landmarks[12].x > landmarks[10].x and  
                landmarks[16].x > landmarks[14].x and  
                landmarks[20].x > landmarks[18].x     
            )
            return other_fingers_extended  
        
        elif hand_direction(landmarks) == "right":
            
            other_fingers_extended = (
                landmarks[8].x < landmarks[6].x and  
                landmarks[12].x < landmarks[10].x and  
                landmarks[16].x < landmarks[14].x and  
                landmarks[20].x < landmarks[18].x  
            )
            return other_fingers_extended
        

    return False

def is_flip_off(landmarks):
    if landmarks[12].y < landmarks[11].y and landmarks[11].y < landmarks[10].y and landmarks[10].y < landmarks[0].y and hand_direction(landmarks) == "up":
        if landmarks[8].y > landmarks[6].y and landmarks[16].y > landmarks[14].y and landmarks[20].y > landmarks[18].y:
            return True
        
    return False
'''
def is_thumbs_up(landmarks):
    # Thumb tip (4) and wrist (0)
    thumb_tip_y = landmarks[4].y

    if thumb_tip_y < landmarks[3].y < landmarks[2].y:

        other_fingers_extended = (
            landmarks[8].y > thumb_tip_y and  # Index finger tip
            landmarks[12].y > thumb_tip_y and  # Middle finger tip
            landmarks[16].y > thumb_tip_y and  # Ring finger tip
            landmarks[20].y > thumb_tip_y     # Pinky tip
        )
        return other_fingers_extended  # True if all other fingers are down

    return False  # Thumb is not up
'''