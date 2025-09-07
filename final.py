import math
def reward_function(params):
    
    MAX_REWARD = 100.0
    MIN_REWARD = 1e-3
    DIRECTION_THRESHOLD = 10.0
    MAX_STEERING_ANGLE = 30
    OFF_TRACK_PENALTY = 0.1  # Penalty multiplier for going off track (significant but not zero reward)
    REWARD_MULTIPLIERS = {
        'center_close': 1.2,
        'center_mid': 0.8,
        'center_far': 0.5,
        'straight_line': 1.2,
        'direction_penalty': 0.5,
        'steering_penalty': 0.8,
        'throttle_penalty': 0.8
    }

    center_offset = params['distance_from_center']
    track_width = params['track_width']
    speed = params['speed']
    all_wheels_on_track = params['all_wheels_on_track']
    steering_angle = abs(params['steering_angle'])
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints'] 
    heading = params['heading']

    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    def calculate_direction(waypoints, closest_waypoints):
        next_wp = waypoints[closest_waypoints[1]]
        prev_wp = waypoints[closest_waypoints[0]]
        return math.degrees(math.atan2(next_wp[1] - prev_wp[0], next_wp[0] - prev_wp[0]))

    # Reward initialization: Start with max reward
    reward = MAX_REWARD

    # Apply off-track penalty (2-second penalty assumption)
    if not all_wheels_on_track:
        reward *= OFF_TRACK_PENALTY  # Apply significant penalty but keep the reward proportional to recovery

    # Reward based on distance from center
    if center_offset <= marker_1:
        reward *= REWARD_MULTIPLIERS['center_close']
    elif center_offset <= marker_2:
        reward *= REWARD_MULTIPLIERS['center_mid']
    elif center_offset <= marker_3:
        reward += REWARD_MULTIPLIERS['center_far']
    else:
        return MIN_REWARD

    # Straight-line reward for low steering angle and high speed
    if steering_angle < 0.1 and speed > 3:
        reward *= REWARD_MULTIPLIERS['straight_line']

    # Direction reward based on track alignment
    track_direction = calculate_direction(waypoints, closest_waypoints)
    direction_diff = abs(track_direction - heading)
    if direction_diff > DIRECTION_THRESHOLD:
        reward *= REWARD_MULTIPLIERS['direction_penalty']

    # Penalize excessive steering
    if steering_angle > MAX_STEERING_ANGLE:
        reward *= REWARD_MULTIPLIERS['steering_penalty']

    # Throttle adjustment based on speed and steering
    if speed > (2.5 - 0.4 * steering_angle):
        reward *= REWARD_MULTIPLIERS['throttle_penalty']

    return float(reward)