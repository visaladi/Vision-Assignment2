import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

def region_growing(img, seed, threshold=5):
    h, w = img.shape
    visited = np.zeros((h, w), dtype=bool)
    region = np.zeros((h, w), dtype=np.uint8)

    seed_val = img[seed]
    stack = [seed]

    while stack:
        y, x = stack.pop()
        if visited[y, x]:
            continue
        visited[y, x] = True

        if abs(int(img[y, x]) - int(seed_val)) <= threshold:
            region[y, x] = 255
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < h and 0 <= nx < w and not visited[ny, nx]:
                        stack.append((ny, nx))
    return region

def run_region_growing():
    input_path = r"C:\Users\visal Adikari\OneDrive\Desktop\uni sem 7\vision\ass2\input\img1.jpg"
    output_folder = r"C:\Users\visal Adikari\OneDrive\Desktop\uni sem 7\vision\ass2\output"
    output_filename = "region_growing_output.png"
    display_filename = "region_growing_display.png"
    output_path = os.path.join(output_folder, output_filename)
    display_path = os.path.join(output_folder, display_filename)

    img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Error: Could not read the image.")
        return

    seed = (img.shape[0] // 2, img.shape[1] // 2)
    region = region_growing(img, seed, threshold=10)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cv2.imwrite(output_path, region)
    print(f"Region grown image saved to {output_path}")

    # Display and save the result
    plt.figure(figsize=(8, 4))
    plt.subplot(1, 2, 1)
    plt.title("Input Image")
    plt.imshow(img, cmap='gray')
    plt.axis('off')
    plt.subplot(1, 2, 2)
    plt.title("Region Grown Output")
    plt.imshow(region, cmap='gray')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(display_path)
    plt.show()
    print(f"Region growing visualization saved to {display_path}")

run_region_growing()
