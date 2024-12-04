# Collage Image Maker

Collage Image Maker transforms a collection of images into a smooth video montage, intelligently dividing the images into scenes based on the total image count. It arranges images side-by-side, ensuring each frame is visually balanced, while applying smooth fade-in and fade-out transitions for a polished final product.

## Features
- **Scene Creation:** Automatically divides the images into scenes, with each scene containing up to 3 images. Images are arranged side-by-side in the frame.
- **Smart Layout:** Handles images of different aspect ratios by resizing them to fit the video’s aspect ratio, ensuring they look great in every scene.
- **Smooth Transitions:** Each scene fades in and fades out, providing smooth visual transitions between frames.
- **Final Banner:** Includes an optional final banner image at the end of the video, adding a personalized touch or finishing detail.
  
## How It Works
1. **Image Input:** The script takes images from a specified directory.
2. **Scene Creation:** It divides the images into scenes. Each scene can have 1 to 3 images, depending on how many images are left.
3. **Image Scaling & Layout:** Each image is resized to fit the video’s aspect ratio. In scenes with fewer than 3 images, the remaining spaces are filled by centering the images.
4. **Video Creation:** Each scene is displayed for a specified duration with fade-in and fade-out effects, creating a seamless flow.
5. **Final Touch:** A banner image is added at the end, completing the video with a stylish conclusion.
6. **Export:** The final video is saved as a `.mp4` file, ready to be shared.

## Installation

Make sure you have the necessary libraries installed:

```bash
pip install moviepy Pillow numpy
```

## Usage

1. Place your images in the 'images' folder.
2. Set the path for the final banner image (optional).
3. Run the script to generate the video.

## Example

Run the script:

```bash
python collage_image_maker.py
```

The script will generate a video named `output_video.mp4`, with your images arranged in scenes, complete with smooth transitions and an optional final banner.
