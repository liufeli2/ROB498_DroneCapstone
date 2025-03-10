import os
from PIL import Image, ImageDraw

# Paths
output_folder = '/Users/felicialiu/Desktop/DEV/ROB498_DroneCapstone/segmentation/task2'
output_gif_path = os.path.join(output_folder, 'output.gif')

frames = []

# Read the output text file
with open(os.path.join(output_folder, 'output.txt'), 'r') as f_out:
    for line in f_out:
        parts = line.strip().split()
        frame_filename = parts[0]
        x1_idx, y1_idx, x2_idx, y2_idx = map(int, parts[1:])

        # Load the frame
        frame = Image.open(os.path.join(output_folder, frame_filename))

        # Draw the rectangle on the frame
        frame = frame.convert("RGB")
        draw = ImageDraw.Draw(frame)
        draw.rectangle([x1_idx, y1_idx, x2_idx, y2_idx], outline="green", width=2)

        frames.append(frame)

# Create GIF with 60 fps
frames[0].save(output_gif_path, save_all=True, append_images=frames[1:], duration=1000//60, loop=0)

print("GIF created.")