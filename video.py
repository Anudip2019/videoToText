import time
import moviepy.editor
import moviepy.video.io.ImageSequenceClip
from PIL import ImageFile
import cv2
import os
import pyautogui
import numpy as np
import sys

name = "vitality"
count = 3650
fps = 30
print("Starting Video Processing...")
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)
"""
if not os.path.isdir(f"s_{name}"):
    os.mkdir(f"s_{name}")
"""
for i in range(count):
    os.system('cls')
    a = open(f"t_{name}/frame_{i}.txt", "r")
    print(a.read())
    # time.sleep(0.15)
    # scr = pyautogui.screenshot()
    # scr1 = cv2.cvtColor(np.array(scr), cv2.COLOR_RGB2BGR)
    # cv2.imwrite(f"s_{name}/scr{i}.png", scr1)
'''
ImageFile.LOAD_TRUNCATED_IMAGES = True

image_files = []

for img_number in range(count):
    image_files.append(f's_{name}/scr' + str(img_number) + '.png')

clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
clip.write_videofile(f't_no_music_{name}.mp4')
music = moviepy.editor.VideoFileClip(f't_no_music_{name}.mp4').set_audio(
    moviepy.editor.VideoFileClip(f'{name}.mp4').audio)
music.write_videofile(f't_{name}.mp4')
'''
