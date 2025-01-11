import cv2

# Load the image
image = cv2.imread('assignment-001-given.jpg')
overlay = image.copy()

# Define text properties
text = 'RAH972U'
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale, font_thickness = 2, 5
text_color, bg_color = (0, 255, 0), (0, 0, 0)
opacity = 0.5
padding = 120

# Get text size and position
img_height, img_width, _ = image.shape
(text_width, text_height), baseline = cv2.getTextSize(text, font, font_scale, font_thickness)
text_x, text_y = img_width - text_width - padding, text_height + padding

# Draw semi-transparent background rectangle for text
rect_x1, rect_y1 = text_x - 10, text_y - text_height - 10
rect_x2, rect_y2 = text_x + text_width + 10, text_y + baseline + 10
cv2.rectangle(overlay, (rect_x1, rect_y1), (rect_x2, rect_y2), bg_color, -1)
cv2.addWeighted(overlay, opacity, image, 1 - opacity, 0, image)

# Add text to the image
cv2.putText(image, text, (text_x, text_y), font, font_scale, text_color, font_thickness)

# Draw a green rectangle
cv2.rectangle(image, (200, 200), (950, 950), text_color, 10)

# Display and save the image
cv2.imshow('Image Result', image)
cv2.imwrite('assignment-001-result.jpg', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
