# Initialize variables
Kp = 1.5
Ki = 0.05
Kd = 0.1

integral_sum = 0
last_error = 0

# Your robot's control loop running at a fixed time interval (e.g., every 20ms)
def update_pid(setpoint, current_value, dt):
    global integral_sum, last_error
    
    # 1. Calculate current error
    error = setpoint - current_value
    
    # 2. Proportional term
    P_out = Kp * error
    
    # 3. Integral term (Accumulate error)
    integral_sum += error * dt
    I_out = Ki * integral_sum
    
    # 4. Derivative term (Rate of change of error)
    derivative_error = (error - last_error) / dt
    D_out = Kd * derivative_error
    
    # 5. Total Output
    output = P_out + I_out + D_out
    
    # Save the current error for the next loop iteration
    last_error = error
    
    return output