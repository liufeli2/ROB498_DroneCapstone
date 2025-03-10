import cv2
import os
import numpy as np

# Paths
video_path = '/Users/felicialiu/Desktop/DEV/ROB498_DroneCapstone/segmentation/task3.MOV'
segmentation_folder = '/Users/felicialiu/Desktop/DEV/ROB498_DroneCapstone/segmentation/obj_train_data'
output_folder = os.path.splitext(video_path)[0]

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Read video
cap = cv2.VideoCapture(video_path)
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

with open(os.path.join(output_folder, 'output.txt'), 'w') as f_out:
    for frame_idx in range(frame_count):
        ret, frame = cap.read()
        if not ret:
            break

        # Rotate the frame by 180 degrees
        # frame = cv2.rotate(frame, cv2.ROTATE_180)

        # Read segmentation file
        seg_file = os.path.join(segmentation_folder, f'frame_{frame_idx:06d}.txt')
        if not os.path.exists(seg_file):
            continue

        with open(seg_file, 'r') as f_seg:
            seg_data = f_seg.read().strip().split()
            seg_data = list(map(float, seg_data))

        print(seg_data)
        # Ensure seg_data contains exactly five values and ignore the first value
        if len(seg_data) != 5:
            print(f"Skipping frame {frame_idx}: unexpected number of values in segmentation file")
            continue

        # Ignore the first value and use the remaining four values
        _, x_center, y_center, width, height = seg_data
        x1 = x_center - width / 2
        y1 = y_center - height / 2
        x2 = x_center + width / 2
        y2 = y_center + height / 2

        x1_idx, y1_idx = int(x1 * frame.shape[1]), int(y1 * frame.shape[0])
        x2_idx, y2_idx = int(x2 * frame.shape[1]), int(y2 * frame.shape[0])

        # Resize frame to lower resolution (quarter of original size)
        frame_resized = cv2.resize(frame, (frame.shape[1] // 4, frame.shape[0] // 4))

        # Scale indices to match the resized frame
        scale_x = frame_resized.shape[1] / frame.shape[1]
        scale_y = frame_resized.shape[0] / frame.shape[0]
        x1_idx_resized = int(x1_idx * scale_x)
        y1_idx_resized = int(y1_idx * scale_y)
        x2_idx_resized = int(x2_idx * scale_x)
        y2_idx_resized = int(y2_idx * scale_y)

        # Write indices to output file
        f_out.write(f'frame_{frame_idx:06d}.png {x1_idx_resized} {y1_idx_resized} {x2_idx_resized} {y2_idx_resized}\n')

        # Save the frame as PNG
        frame_filename = os.path.join(output_folder, f'frame_{frame_idx:06d}.png')
        cv2.imwrite(frame_filename, frame_resized)

cap.release()
print("Frames and segmentation indices saved.")