# Image to Video Maker

This project allows you to create videos from a sequence of images, seamlessly transitioning between each frame with fade-in and fade-out effects. It supports customizing the video dimensions, display durations, and handling images of varying aspect ratios to fit neatly into the video.

## Features
- **Image Handling:** Automatically resizes images to fit the video’s aspect ratio while maintaining their visual integrity.
- **Smooth Transitions:** Applies fade-in and fade-out effects for a polished, cinematic feel.
- **Flexible Layout:** Supports displaying up to 3 images per frame, with intelligent centering and scaling based on the number of images.
- **Final Banner:** Adds a customizable banner image at the end of the video to provide context or branding.

## How It Works
1. The script loads images from a specified directory and processes them.
2. It checks the aspect ratio of each image to ensure it fits well into the video.
3. Multiple images are arranged within each frame and are stitched together with smooth transitions.
4. A final banner image is added at the end of the video.
5. The video is then exported as a `.mp4` file.

## Installation

Make sure you have the necessary libraries installed:

```bash
pip install moviepy Pillow numpy
```

## Usage

1. Place your images in the 'images' folder.
2. Set the path for the final banner image.
3. Run the script, and it will generate a video named `output_video.mp4` in the current directory.

## Example

Run the script:

```bash
python image_to_video.py
```

The output will be a video that displays your images with smooth transitions and a final banner.
