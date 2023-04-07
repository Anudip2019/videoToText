from PIL import Image
import cv2
import os
name = "vitality"
tw = 320
th = 180

vidcap = cv2.VideoCapture(f'{name}.mp4')
success, image = vidcap.read()
count = 0
if not os.path.isdir(name):
    os.mkdir(name)
while success:
    cv2.imwrite(f"{name}/frame%d.jpg" % count, image)
    success, image = vidcap.read()
    print(f"Converting to images: Frame {count} OK: {success}")
    count += 1


if not os.path.isdir(f"t_{name}"):
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

print("Start video in video.py", count)
