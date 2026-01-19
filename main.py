#!/usr/bin/env python3
# /// script
# dependencies = [
#   "opencv-python",
#   "numpy",
#   "Pillow"
# ]
# ///

import sys
import argparse
import numpy as np 
from PIL import Image, ImageFilter
import cv2

# argument handler
argparser: argparse.ArgumentParser = argparse.ArgumentParser()
argparser.add_argument("-i", "--input", help="set input file")
argparser.add_argument("-o", "--output", help="set output file")
argparser.add_argument("-s", "--strength", help="set integer sharpening strength (default = 900)")
argparser.add_argument("-f", "--framerate", help="set output framerate in whole frames per second (default = 24)")
argparser.add_argument("-l", "--length", help="set output length in seconds (default = 3.0)")
argparser.add_argument("-r", "--sharpen-radius", help="set integer sharpen radius (default = 2)")
argparser.add_argument("-R", "--blur-radius", help="set integer blur radius (default = 2)")
args = argparser.parse_args()

# ensure proper input/output
input_file: str = args.input
output_file: str = args.output
if not args.input:
    print("Error: must specify input file using '-i' option")
    sys.exit()
if not args.output:
    print("Warning: output will go to output.mp4 because no output file was specified")
    user_input: str = input("Are you sure you want to proceed? [y/N]: ")
    if user_input != "Y" and user_input != "y":
        print("exiting")
        sys.exit()
    else:
        output_file: str = "output.mp4"

# processing settings
framerate: int = int(args.framerate if args.framerate else 24)
length: float = float(args.length if args.length else 3.0)
num_frames: int = int(length * framerate)
strength: int = int(args.strength if args.strength else 900)
sharpen_radius: int = int(args.sharpen_radius if args.sharpen_radius else 2)
blur_radius: int = int(args.blur_radius if args.blur_radius else 2)
sharpen = ImageFilter.UnsharpMask(radius=sharpen_radius, percent=strength)
blur = ImageFilter.GaussianBlur(radius=blur_radius)

# main program
def main() -> None:
    try:
        img: Image = Image.open(input_file)
    except FileNotFoundError:
        print(f'Error: {input_file} not found')
        sys.exit()
    
    # initialize input image array and output video writer
    img_arr: np.array = np.array(img)
    fourcc: cv2.VideoWriter = cv2.VideoWriter_fourcc(*'mp4v')
    output_writer: cv2.VideoWriter = cv2.VideoWriter(output_file, fourcc, framerate, (img_arr.shape[1], img_arr.shape[0]))

    # write initial frame
    frame: np.array = cv2.cvtColor(img_arr, cv2.COLOR_RGB2BGR)
    output_writer.write(img_arr)
    # render and write remaining frames
    for i in range(num_frames):
        print(f"Rendering frame {i + 1}/{num_frames}")
        img = img.filter(sharpen)
        img = img.filter(blur)
    
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        output_writer.write(frame)

    output_writer.release()

if __name__ == "__main__":
    main()

sys.exit()
