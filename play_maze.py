"""
Automating Maze Swipe Android Game https://play.google.com/store/apps/details?id=com.spcomes.maze

Planning to:
    - Get Screenshot of maze from phone
    - Use Computer vision (OpenCv) https://opencv.org/ to map out the maze pattern
    - Find ball's current position and the expected final destination
    - Bruteforce all options until ball reaches destination
    - Perform swipe actions on the Android to simulate the game play
        (Using adb swipe command) https://stackoverflow.com/questions/39190083

    - Click play next puzzle button
    - Repeat the process
"""

import cv2
