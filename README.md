# Vision-Assignment2

# Image Segmentation Techniques in Python

This repository contains implementations of two fundamental image segmentation techniques in Python using OpenCV and NumPy:

1. **Otsu’s Thresholding with Gaussian Noise**
2. **Region Growing Segmentation**

All images are read from a default folder (`Assignment1/input`) and results are saved to (`Assignment1/output`).

---

## 📁 Folder Structure

Assignment1/
├── input/
│ └── img1.jpg # Your input image (grayscale or RGB)
├── output/
│ ├── otsu_threshold.png # Binary image from Otsu thresholding
│ ├── otsu_display.png # Visualization of original, noisy, and thresholded images
│ ├── region_growing_output.png # Output of region growing
│ └── region_growing_display.png # Side-by-side plot of input and region result

yaml
Copy
Edit

---

## 1️⃣ Otsu’s Thresholding with Gaussian Noise

This script simulates a noisy environment by adding Gaussian noise to a grayscale image and applies Otsu's method to segment the foreground from the background.

## 📌 Features
- Adds Gaussian noise (μ = 0, σ = 10)
- Applies Otsu's automatic thresholding
- Saves both raw result and a matplotlib visualization

## ▶️ How to Run
---
##bash
python otsu_with_gaussian_noise.py
🔍 Output Example
otsu_threshold.png: Binary segmented image

otsu_display.png: Original vs Noisy vs Thresholded (side-by-side)

2️⃣ Region Growing Segmentation
A simple but effective pixel-based segmentation method using seed points and intensity thresholding.

##📌 Features
Uses a recursive region growing algorithm

Segments based on intensity similarity

Center pixel is used as the seed point

Saves both result and visual plot
---
##▶️ How to Run
bash
Copy
Edit
python region_growing.py
🔍 Output Example
region_growing_output.png: Binary segmented region

region_growing_display.png: Input vs Output (side-by-side)
---
##🧰 Requirements
Install the required Python libraries with:

pip install opencv-python numpy matplotlib
---
##✍️ Author
Visal Sandeep Adikari
Department of Computer Engineering
Faculty of Engineering, University of Ruhuna

