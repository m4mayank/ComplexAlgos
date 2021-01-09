#!/home/cloud_user/.local/share/virtualenvs/algo-9u7x6JDZ/bin/python3
# On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:

# "G": go straight 1 unit;
# "L": turn 90 degrees to the left;
# "R": turn 90 degress to the right.
# The robot performs the instructions given in order, and repeats them forever.

# Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

 

# Example 1:

# Input: "GGLLGG"
# Output: true
# Explanation: 
# The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
# When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
# Example 2:

# Input: "GG"
# Output: false
# Explanation: 
# The robot moves north indefinitely.
# Example 3:

# Input: "GL"
# Output: true
# Explanation: 
# The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dir = [0,1]
        x, y = 0, 0
        for z in instructions:
            if z == "G":
                x, y = x + dir[0], y+dir[1]
            elif z == "L":
                dir[0], dir[1] = -dir[1] , dir[0]
            else:
                dir[0], dir[1] = dir[1], -dir[0]
        print(x)
        print(y)
        print(dir)
        if (x == 0 and y == 0) or dir != [0,1]:
            return True
        else:
            return False