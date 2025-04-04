import math
def euler_to_quaternion(roll, pitch, yaw):
    #converting everything to radians
    roll = math.radians(roll)
    pitch = math.radians(pitch)
    yaw = math.radians(yaw)
    # calculate cos and sin for half of each angle
    cy = math.cos(yaw * 0.5)
    sy = math.sin(yaw * 0.5)
    cp = math.cos(pitch * 0.5)
    sp = math.sin(pitch * 0.5)
    cr = math.cos(roll * 0.5)
    sr = math.sin(roll * 0.5)
    # quaternion formula
    w = cr * cp * cy + sr * sp * sy
    x = sr * cp * cy - cr * sp * sy
    y = cr * sp * cy + sr * cp * sy
    z = cr * cp * sy - sr * sp * cy

    return (w, x, y, z)



roll = float(input("Enter roll angle (degrees): "))
pitch = float(input("Enter pitch angle (degrees): "))
yaw = float(input("Enter yaw angle (degrees):"))

quaternion = euler_to_quaternion(roll, pitch, yaw)
print("quaternion (w, x, y, z)=", quaternion)
