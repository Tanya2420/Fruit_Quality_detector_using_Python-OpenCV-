import cv2
import numpy as np

def detect_fruit_quality(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    if image is None:
        print("Could not open or find the image.")
        return
    
    # Convert the image to the HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Define the color range for a "good" fruit (e.g., red)
    lower_color = np.array([0, 100, 100])  # Lower bound for red in HSV
    upper_color = np.array([10, 255, 255]) # Upper bound for red in HSV
    
    # Create a mask to isolate the "good" color in the image
    mask = cv2.inRange(hsv_image, lower_color, upper_color)
    
    # Count the number of "good" color pixels
    good_color_pixels = cv2.countNonZero(mask)
    
    # Calculate the percentage of "good" color in the image
    total_pixels = image.shape[0] * image.shape[1]
    quality_percentage = (good_color_pixels / total_pixels) * 100
    
    # Determine fruit quality based on the percentage
    if quality_percentage >= 70:
        return "Excellent Quality"
    elif 50 <= quality_percentage < 70:
        return "Good Quality"
    else:
        return "Poor Quality"

# Test the function with an example image
image_path = "C:/Users/MY HP/Downloads/fruit.image.png"  # Replace with the path to your fruit image
fruit_quality = detect_fruit_quality(image_path)
print("Fruit Quality:", fruit_quality)
