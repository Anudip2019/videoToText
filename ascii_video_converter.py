from PIL import Image
import cv2
import os
import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--width', type=int, default=None, help='Width of the output video')
args = parser.parse_args()

name = "video"
vidcap = cv2.VideoCapture(f'{name}.mp4')
if args.width is None:
    ogw, ogh = vidcap.get(3), vidcap.get(4)
    min = math.gcd(ogh, ogw) // 2
    magic_ratio = 95 / 16
    ratio_2 = ogw/ogh
    if ratio_2 > magic_ratio:
        i = 0
        while i * min < 1900:
            i += 1
        i -= 1
        tw = i * min
        th = int(tw/ratio_2)
    else:
        i = 0
        while i * min < 320:
            i += 1
        i -= 1
        th = i * min
        tw = int(th*ratio_2)
else:
    tw = args.width
    th = int(tw * vidcap.g / 2)
success, image = vidcap.read()
count = 0
if os.path.isdir(name):
    os.rmdir(name)
os.mkdir(name)
while success:
    cv2.imwrite(f"{name}/frame%d.jpg" % count, image)
    success, image = vidcap.read()
    print(f"Converting to images: Frame {count} OK: {success}")
    count += 1


if os.path.isdir(f"t_{name}"):
    os.rmdir(f"t_{name}")
os.mkdir(f"t_{name}")
for i in range(count):
    im = Image.open(f'{name}/frame{i}.jpg', 'r').resize((tw, th)).convert("LA")
    width, height = im.size
    pixel_values = list(im.getdata())
    pic = []
    a = ""
    for j in range(len(pixel_values)):
        al = "$@B%8&WM#*oahkbdpwmZO0QLCUYXzcvuxrjft/|()1{}[]?-_+~<>i!lI;:,^`. "
        ta = al[63-(pixel_values[j][0] // 4)]
        a += f"{ta}  "
        if j % width == width - 1:
            pic.append(a)
            a = ""
    with open(f"t_{name}/frame_{i}.txt", "w") as fp:
        for j in pic:
            fp.write("%s\n" % j)
    print(f"Frame {i} converted successfully.")

print("Start video.py in alacritty")
