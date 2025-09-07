# Imports
import math

def reward_function(params):
    # Read input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    speed = params['speed']
    all_wheels_on_track = params['all_wheels_on_track']
    steering_angle = abs(params['steering_angle'])
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints'] 
    heading = params['heading']
    
    # Initiate max reward at start
    reward = 10
    
    # Give lowest reward for not staying on track
    if not all_wheels_on_track:
        reward = 0.1

    # Give higher reward for staying close the center line
    if distance_from_center <= (track_width / 2.0):
        reward *= ( (track_width / 2.0) - distance_from_center )
    else:
        reward *= 0.1  
        
    # Give higher reward if car is moving straight and fast
    if abs(steering_angle) < 0.1 and speed > 1.8:
        reward *= 1.25
        
    # Reward for staying in same direction
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]
    direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0]) 
    direction = math.degrees(direction)
    direction_diff = abs(direction - heading)
    if direction_diff > 10.0:
        reward *= 0.5

    # Penalize car if steering too much
    if abs(steering_angle) > 30:
        reward *= 0.75
        
    # Penalize car for throttle while steering
    if speed > 2.0 - (0.4 * abs(steering_angle)):
        reward *= 0.75
    
    return float(reward)