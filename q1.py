import math
def distance(x, y, z, x_cam=0, y_cam=0, z_cam=0):
    return math.sqrt((x - x_cam) ** 2 + (y - y_cam) ** 2 + (z - z_cam) ** 2)



x= int(input("enter x:"))
y= int(input("enter y:"))
z= int(input("enter z:"))

z_final=z+55 #offset

print("new position wrt center:",x,y,z_final)
print("distance before:",distance(x, y, z))
print("distance after:",distance(x,y,z_final,0,0,-55))#changing Frame of reference