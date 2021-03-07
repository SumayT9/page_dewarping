"""
This is an implementation of the paper by Fu et. al "A Model-based Book Dewarping Method Using Text Line Detection"
"""
import cv2
import zuck_dewarp

# 3.1
# input: book to be read
# output: list [[points of line 1], [points of line 2], [ points of line 3], etc]
def detect_text_lines(image):
    return zuck_dewarp.text_line_detection(image)


# 3.1.2
def pixel_classification(image):
    pass


# 3.2.1
def left_right_boundary_estimation(image):
    pass


# 3.2.2
def top_bottom_curves_selection(image):
    pass


# 3.3
def rectify_document(image):
    pass


if __name__ == "__main__":
    img = cv2.imread('data/gov_2.jpeg')  # read input image
    detect_text_lines(img)
