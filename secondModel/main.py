def reward_function(params):
    # Learning purpose 
    
    # Read input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    speed = params['speed']
    all_wheels_on_track = params['all_wheels_on_track']
    steering_angle = abs(params['steering_angle'])
    
    reward = 1
    
    # Give higer reward for staying on track_width
    if not all_wheels_on_track:
        reward *= 0.1

    # Give higher reward for staying close the center line
    if distance_from_center <= (track_width / 2.0):
        reward = 1 * ( (track_width / 2.0) - distance_from_center )
    
    # Give reward for higher speed
    reward *= speed
    
    # Penalize car if steering too much
    if steering_angle > 30:
        reward *= 0.8
    
    return float(reward)
