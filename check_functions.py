def hand_direction(landmarks):

    wrist_x = landmarks[0].x
    wrist_y = landmarks[0].y

    middle_joint_x = landmarks[13].x
    middle_joint_y = landmarks[13].y

    # find the slope 
    if wrist_x != middle_joint_x:
        slope = (middle_joint_y - wrist_y) / (middle_joint_x - wrist_x)
    else:
        slope = None

    if slope is None:  # vertical line
        return "up" if wrist_y > middle_joint_y else "down"
    elif abs(slope) > 1:  # steep slope (vertical-ish)
        return "up" if wrist_y > middle_joint_y else "down"
    else:  # shallow slope (horizontal-ish)
        return "left" if wrist_x > middle_joint_x else "right"

def is_thumbs_up(landmarks):

    thumb_tip_y = landmarks[4].y
    thumb_joint_y = landmarks[3].y

    if thumb_tip_y < thumb_joint_y:
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

def is_finger_up(landmarks):
    if landmarks[8].y < landmarks[7].y and landmarks[7].y < landmarks[6].y and landmarks[6].y < landmarks[0].y and hand_direction(landmarks) == "up":
        if landmarks[12].y > landmarks[10].y and landmarks[16].y > landmarks[14].y and landmarks[20].y > landmarks[18].y:
            return True
        
    return False

def is_finger_down(landmarks):
    if landmarks[8].y > landmarks[7].y and landmarks[7].y > landmarks[6].y and landmarks[6].y > landmarks[0].y and hand_direction(landmarks) == "down":
        if landmarks[12].y < landmarks[10].y and landmarks[16].y < landmarks[14].y and landmarks[20].y < landmarks[18].y:
            return True
        
    return False

def is_high_five(landmarks):
    if landmarks[8].y < landmarks[7].y and landmarks[12].y < landmarks[11].y and landmarks[16].y < landmarks[15].y and landmarks[20].y < landmarks[19].y and hand_direction(landmarks) == "up":
        if landmarks[4].x > landmarks[3].x > landmarks[2].x or landmarks[4].x < landmarks[3].x < landmarks[2].x:
            return True
    
    return False

def is_peace_sign(landmarks):
    if landmarks[5].y > landmarks[6].y > landmarks[7].y > landmarks[8].y and landmarks[9].y > landmarks[10].y > landmarks[11].y > landmarks[12].y and hand_direction(landmarks) == "up":
        if landmarks[16].y > landmarks[14].y and landmarks[20].y > landmarks[18].y:
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
