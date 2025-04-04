## I will explain my learnings and aproach question by question:

# Light dose:-
All the commands were straight forward and easily understandble with the resources attached in the task file.
but the installation process was long.I did using VMware.
The syntax was kinda similar to c programming the question was also straight forward so implementing it was easy.
Learnings were basic commands in ubuntu and basic syntaxs in bash.

# Medium dose:-

## question 1:-
Understanding what is going on was confusing tbh...

The rover uses a camera mounted at its front and top to detect a red circle marker on the ground. Although it detects the marker correctly and moves towards the marker. it ends up stopping 55 cm behind the actual marker because of incorrect positioning due to the camera's frame of reference. The task is to adjust the navigation system by changing the frame of reference so that the rover stops exactly on the marker's position and performs the 360-degree turn accurately.

approach:
understood that marker detected coordinate will be wrt camera so i changed the offseted the fram of reference to the center of the rover.so at this point it could do the 360- degree turn accurately.

## question 2:-
here i just had to learn how morse code works then it was simple just import the dictionary containg the conversion then through a function converted it...working of function was lik breaking the morse code till we get alphabets then getting then morse code beeing the key its respective alphabet being the value, i could decode the morse code.

## question 3:-
I had to understand the pattern of how each letter was shifted>once i saw that the 1st letter was shifted by 1, 2nd by 2, and so on, it was easy. i just looped through each character, converted everything to uppercase, then reversed the shift based on its position in the string. also had to make sure that if the shift goes before A, it loops back from Z so used modular arithmetic for that. that gave me back the original message.

## question 4:-
muchiko filter just goes over the data in chunks of window size and takes average of each chunk, that way the sudden jumps or noise kinda gets balanced out. sanchiko filter works the same way but instead of average, it takes the middle value (median), which makes it better when there are extreme values that could mess up the average. hybrid was just using muchiko first then sanchiko on its output, so it gets both smoothness and stability.
the tough part was handling the window properly…like making sure the window doesn’t go out of range of the data. also sometimes the output length gets smaller after filtering, so had to be careful while applying filters one after another. figuring out which filter worked best also took some trial and error with different data.

## question 5:-
so basically here we’re converting our rotation system (which uses roll, pitch, yaw — 3 values) into the Martian style, which is a 4-number system called quaternion. we learned that quaternions are better for 3D rotation because they avoid something called gimbal lock (which is when two axes align and you lose one degree of freedom). so we had to write a code that takes roll, pitch, yaw (in degrees), and gives the quaternion (w, x, y, z) which is what Martians use.
formulas used:=
cy = cos(yaw / 2)
sy = sin(yaw / 2)
cp = cos(pitch / 2)
sp = sin(pitch / 2)
cr = cos(roll / 2)
sr = sin(roll / 2)
w = cr * cp * cy + sr * sp * sy
x = sr * cp * cy - cr * sp * sy
y = cr * sp * cy + sr * cp * sy
z = cr * cp * sy - sr * sp * cy
(w,x,y,z) is the final result

i understood what a gimbal lock was and why quaternion are used and tried understanding these formulas and how it was derived but dint understand a thing...but after getting to know these formulas it was just plug and play.

