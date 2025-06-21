import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

def otsu_with_gaussian_noise():
    input_path = r"C:\Users\visal Adikari\OneDrive\Desktop\uni sem 7\vision\ass2\input\img1.jpg"
    output_folder = r"C:\Users\visal Adikari\OneDrive\Desktop\uni sem 7\vision\ass2\output"
    output_filename = "otsu_threshold.png"
    display_filename = "otsu_display.png"
    output_path = os.path.join(output_folder, output_filename)
    display_path = os.path.join(output_folder, display_filename)

    img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Error: Could not read the image.")
        return

    noise = np.random.normal(0, 10, img.shape).astype(np.int16)
    noisy_img = np.clip(img.astype(np.int16) + noise, 0, 255).astype(np.uint8)

    _, otsu_result = cv2.threshold(noisy_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cv2.imwrite(output_path, otsu_result)
    print(f"Otsu thresholded image saved to {output_path}")

    # Display and save the result
    plt.figure(figsize=(10, 4))
    plt.subplot(1, 3, 1)
    plt.title("Original Image")
    plt.imshow(img, cmap='gray')
    plt.axis('off')
    plt.subplot(1, 3, 2)
    plt.title("Noisy Image")
    plt.imshow(noisy_img, cmap='gray')
    plt.axis('off')
    plt.subplot(1, 3, 3)
    plt.title(f"Otsu Threshold = {_:.2f}")
    plt.imshow(otsu_result, cmap='gray')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(display_path)
    plt.show()
    print(f"Otsu result visualization saved to {display_path}")

otsu_with_gaussian_noise()
