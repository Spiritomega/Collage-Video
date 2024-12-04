import os
from PIL import Image
import numpy as np
from moviepy.editor import ImageClip, concatenate_videoclips

# Set the dimensions for the video
VIDEO_WIDTH, VIDEO_HEIGHT = 1920, 1080
FADE_DURATION = 1  # Duration of fade in and fade out in seconds
DISPLAY_DURATION = 2  # Time each image is fully displayed in seconds

# Path to the directory containing images and the final banner image
image_dir = 'images'
final_image_path = 'banner/BANNER 1 .jpg'

# Get list of image files
image_files = [os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.lower().endswith(('png', 'jpg', 'jpeg'))]

# List to hold clips
clips = []

# Function to calculate the width each image should take based on its aspect ratio to fit 3 images
def calculate_width(height, original_width, original_height):
    return int(height * original_width / original_height)

# Function to check if an image's aspect ratio is close to the video's aspect ratio
def is_close_to_video_aspect_ratio(image_width, image_height, video_width=VIDEO_WIDTH, video_height=VIDEO_HEIGHT, tolerance=0.1):
    image_aspect_ratio = image_width / image_height
    video_aspect_ratio = video_width / video_height
    return abs(image_aspect_ratio - video_aspect_ratio) < tolerance

# Set a standard height for all images
STANDARD_HEIGHT = VIDEO_HEIGHT  # Use full height of the video

# Iterate over the images
while image_files:
    # Take the first 3 images or fewer if less than 3 are left
    current_images = image_files[:3]
    image_files = image_files[3:]

    # Check if any image has an aspect ratio close to the video's aspect ratio
    special_case = False
    for img_file in current_images:
        img = Image.open(img_file)
        if is_close_to_video_aspect_ratio(img.width, img.height):
            special_case = True
            special_img_file = img_file
            break

    if special_case:
        # Handle the special case where one image fills the screen
        img = Image.open(special_img_file)
        img_width = VIDEO_WIDTH
        img_height = int(VIDEO_WIDTH * img.height / img.width)
        img = img.resize((img_width, img_height), Image.LANCZOS)
        frame = Image.new('RGB', (VIDEO_WIDTH, VIDEO_HEIGHT), (0, 0, 0))
        y_offset = (VIDEO_HEIGHT - img_height) // 2
        frame.paste(img, (0, y_offset))
        current_images.remove(special_img_file)
    else:
        # Calculate the total width of these images
        total_width = 0
        widths = []
        for img_file in current_images:
            img = Image.open(img_file)
            original_width, original_height = img.size
            width = calculate_width(STANDARD_HEIGHT, original_width, original_height)
            total_width += width
            widths.append(width)

        # Calculate scale factor to fit into VIDEO_WIDTH
        scale_factor = VIDEO_WIDTH / total_width if len(current_images) == 3 else 1

        # Create a new frame with a black background
        frame = Image.new('RGB', (VIDEO_WIDTH, VIDEO_HEIGHT), (0, 0, 0))

        # Calculate the x_offset for centering the images if there are less than 3
        if len(current_images) < 3:
            total_scaled_width = sum(int(widths[idx] * scale_factor) for idx in range(len(current_images)))
            x_offset = (VIDEO_WIDTH - total_scaled_width) // 2
        else:
            x_offset = 0

        # Paste images onto the frame
        for idx, img_file in enumerate(current_images):
            img = Image.open(img_file)
            img_width = int(widths[idx] * scale_factor)
            img_height = int(STANDARD_HEIGHT * scale_factor)
            img = img.resize((img_width, img_height), Image.LANCZOS)
            y_offset = (VIDEO_HEIGHT - img_height) // 2
            frame.paste(img, (x_offset, y_offset))
            x_offset += img_width

    # Convert the frame to a numpy array
    frame_array = np.array(frame)

    # Create an ImageClip from the frame
    image_clip = ImageClip(frame_array)

    # Set the duration of the clip
    image_clip = image_clip.set_duration(DISPLAY_DURATION + 2 * FADE_DURATION)

    # Apply fade-in and fade-out effects
    image_clip = image_clip.fadein(FADE_DURATION).fadeout(FADE_DURATION)

    # Add the clip to the list of clips
    clips.append(image_clip)

# Add the final info banner image
final_img = Image.open(final_image_path)
final_img_width = int(VIDEO_HEIGHT * final_img.width / final_img.height)
final_img = final_img.resize((final_img_width, VIDEO_HEIGHT), Image.LANCZOS)
frame = Image.new('RGB', (VIDEO_WIDTH, VIDEO_HEIGHT), (0, 0, 0))
x_offset = (VIDEO_WIDTH - final_img_width) // 2
frame.paste(final_img, (x_offset, 0))
frame_array = np.array(frame)

final_clip = ImageClip(frame_array).set_duration(DISPLAY_DURATION + 2 * FADE_DURATION).fadein(FADE_DURATION).fadeout(FADE_DURATION)

# Add the final clip to the list of clips
clips.append(final_clip)

# Concatenate all clips into a single video
final_clip = concatenate_videoclips(clips, method="compose")

# Write the video file
final_clip.write_videofile("output_video.mp4", codec="libx264", fps=24)
