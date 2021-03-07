"""
This is an implementation of the paper by Fu et. al "A Model-based Book Dewarping Method Using Text Line Detection"
"""
import cv2
import zuck_dewarp

# 3.1
# input: book to be read
# output: [[points of line 1], [points of line 2], [points of line 3], etc]
def detect_text_lines(image):
    return zuck_dewarp.text_line_detection(image)


# 3.1.2
def pixel_classification(image):
    pass


# 3.2.1 (Jupiter)
# points: a list of (x,y) tuples: one for the end of each text line
# 
# returns: a tuple (a,b) that describes the line according to the formula x = a + b*y
# 
# note: call this function twice, once for the right boundary and once fo the left boundary
# note2: the result have the x and y swapped from a typical linear equation to reduce the chance of dividing by 0
def left_right_boundary_estimation(points):
    CONSTANT_Ta = 10  #threshold for removing tab lines
    valid = False
    a = -1
    b = -1
    curPoints = points.copy()

    while(not valid):
        #use OLS to find line that approximates the points
        #https://en.wikipedia.org/wiki/Ordinary_least_squares#Simple_linear_regression_model
        sumX = 0
        sumY = 0
        sumXY = 0
        sumYY = 0
        for x,y in curPoints:
            sumX += x
            sumY += y
            sumXY += x*y
            sumYY += y*y
        b = (sumXY - sumX*sumY/len(curPoints))/(sumYY-sumY*sumY/len(curPoints))
        a = sumX/len(curPoints) - b*sumY/len(curPoints)

        #remove points that are too far from the line
        valid = True
        if(b == 0):
            #flat line corner case (to avoid division by 0)
            for x,y in curPoints:
                if(abs(x - a) > CONSTANT_Ta):
                    print("removed ({},{})".format(x,y))
                    curPoints.remove((x,y))
                    valid = False
        else:
            for x,y in curPoints:
                if(abs(-a*x+y+b)/math.sqrt(a**2+1) > CONSTANT_Ta):
                    print("removed ({},{})".format(x,y))
                    curPoints.remove((x,y))
                    valid = False

    return a, b


# 3.2.2
def top_bottom_curves_selection(image):
    pass


# 3.3
def rectify_document(image):
    pass


if __name__ == "__main__":
    img = cv2.imread('data/gov_2.jpeg')  # read input image
    text_lines = detect_text_lines(img)
