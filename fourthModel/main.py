def reward_function(params):
    # Changes from previous model 
    # max speed = 3 m/s
    # min speed = 1.5 m/s
    # training time = 60 mins
    # includes higher reward if car is going fast in a straight line
    # Increased max range of reward from 1 to 100
    # If car too much near to edge or outside reward reset to min
    # Some minor reward scaling change
    # Penalize car for throttling while steering
    
    # Read input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    speed = params['speed']
    all_wheels_on_track = params['all_wheels_on_track']
    steering_angle = abs(params['steering_angle'])
    
    reward = 100
    
    # Give lowest reward for not staying on track
    if not all_wheels_on_track:
        reward = 0.1

    # Give higher reward for staying close the center line
    if distance_from_center <= (track_width / 2.0):
        reward *= ( (track_width / 2.0) - distance_from_center )
    else:
        # Crashed
        reward = 0.1  
        
    # Give higher reward if car is moving straight and fast
    if abs(steering_angle) < 0.1 and speed > 1.9:
        reward *= 1.25

    # Penalize car if steering too much
    if abs(steering_angle) > 30:
        reward += 0.75
        
    # Penalize car for throttle while steering
    if speed > 2.5 - (0.4 * abs(steering_angle)):
        reward *= 0.75
    
    return float(reward)
