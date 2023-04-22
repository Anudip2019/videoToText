# ASCII Text Video Converter

# Please credit my youtube channel if you are using this

This script converts a video file into an ASCII text video.

## Prerequisites

* Windows version 10 or later
* Python 3.x
* Alacritty Terminal
* OpenCV-Python (`pip install opencv-python`)
* NumPy (`pip install numpy`)
* Pillow (`pip install Pillow`)
* PyAutoGui (`pip install pyautogui`)

## Usage

1. Place the video file you want to convert in the same directory as the script.
2. Open a terminal or command prompt and navigate to the directory containing the script.
3. Run the script with the following command: `python ascii_video_converter.py` (You can choose the options you like).
4. Wait for the script to finish running. The converted ASCII video text files will be saved in a folder named `t_video.txt` in the same directory as the script.
5. Open Alacritty with font size 2 using the command (`alacritty -o font.size=2`).
6. Run video.py in the new window. It will be hard to see the command, so it is recommended to copy the command and paste it in the window: `python video.py`.
7. As it generates a smooth video, it can take upto 2 hours per 5 minutes of video, so you are probably gonna have to wait a while.
8. The final video will be saved as `t_video.mp4`.

## Options

The first script has the following optional command line arguments:

* `--width`: The width of the output ASCII video.

The second script has this optional command:
* `--fps`: The frame rate of the output ASCII video (default is 30).

You can use these options by passing them as arguments when running the script. For example, to set the width to 200 and the frame rate to 60, use the following commands: `python ascii_video_converter.py --width 200` and `python video.py --fps 60`.

## Notes

* This script only works with videos that use the .mp4 file extension. If your video uses a different extension, you will need to convert it to .mp4 first.
* This script may take a long time to run for longer videos or larger output sizes.
