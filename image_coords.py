import cv2

# Initialize a global variable to store the pixel coordinates
coordinates = []

# Define the bounding box for the mail icon (x_min, y_min, x_max, y_max)
chrome_icon_bounds = (43, 703, 89, 745)

# Mouse callback function to capture mouse click events
def get_coordinates(event, x, y, flags, param):
    global coordinates
    if event == cv2.EVENT_LBUTTONDOWN:  # Left mouse button click
        coordinates = (x, y)
        print(f"Clicked at pixel coordinates: ({x}, {y})")
        
        # Check if the click is within the mail icon bounds
        if chrome_icon_bounds[0] <= x <= chrome_icon_bounds[2] and chrome_icon_bounds[1] <= y <= chrome_icon_bounds[3]:
            print("Google icon clicked!")
        else:
            print("Click outside the Google icon.")

# Load the image
image = cv2.imread('image1.jpg')  

# Create a window
cv2.namedWindow('Image Window')

# Set the mouse callback function
cv2.setMouseCallback('Image Window', get_coordinates)

while True:
    cv2.imshow('Image Window', image)

    # Wait for the 'Esc' key to close the window
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # 27 is the ASCII value for the 'Esc' key
        break

# Close all OpenCV windows
cv2.destroyAllWindows()
