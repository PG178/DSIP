import cv2
import numpy as np
import matplotlib.pyplot as plt


image_path = "/photo-1728998888313-9bc4eff8e23a.avif"
src_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


if src_image is None:
   print("Error: Image not found!")
else:
   # 1. Image Negation
   negative_image = 255 - src_image


   # 2. Thresholding
   _, thresholded_image = cv2.threshold(
       src_image, 50, 255, cv2.THRESH_BINARY
   )


   # 3. Gamma Correction
   gamma = 2.0


   # Normalize image to [0, 1]
   normalized_image = src_image / 255.0


   # Apply gamma correction
   gamma_corrected_image = np.power(normalized_image, 1 / gamma)


   # Convert back to [0, 255]
   gamma_corrected_image = np.uint8(gamma_corrected_image * 255)


   # Display Images
   plt.figure(figsize=(16, 5))


   # Original
   plt.subplot(1, 4, 1)
   plt.imshow(src_image, cmap="gray")
   plt.title("Original Image")
   plt.axis("off")


   # Negative
   plt.subplot(1, 4, 2)
   plt.imshow(negative_image, cmap="gray")
   plt.title("Negative Image")
   plt.axis("off")


   # Threshold
   plt.subplot(1, 4, 3)
   plt.imshow(thresholded_image, cmap="gray")
   plt.title("Threshold Image")
   plt.axis("off")


   # Gamma
   plt.subplot(1, 4, 4)
   plt.imshow(gamma_corrected_image, cmap="gray")
   plt.title("Gamma Corrected")
   plt.axis("off")


   plt.tight_layout()
   plt.show()
