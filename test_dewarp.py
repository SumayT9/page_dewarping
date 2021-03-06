# a simple file for testing dewarp's function
import dewarp

#text line enhancement


#pixel classification


#left right boundary estimation
points = [(10,10),(10,20),(11,30),(30,50),(11,60),(12,70),(12,80),(13,90),(14,100)]
print(dewarp.left_right_boundary_estimation(points))
points = [(10,10),(10,20),(10,30),(10,50),(10,60),(10,70),(10,80),(10,90),(10,100)]
print(dewarp.left_right_boundary_estimation(points))


#top bottom curves selection


#rectify document