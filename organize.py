# organize imports
import os
import glob
import csv
import datetime


# print start time
print ("[INFO] program started on - " + str(datetime.datetime.now()))

# get the input and output path
input_path  = "/home/laus/uni/thesis/RawData/images/color"
output_path = "/home/laus/uni/thesis/towel_recognition/dataset/train"

# get the class label limit
class_limit = 2

# take all the images from the dataset
image_paths = glob.glob(input_path + "/*.jpg")

# class names
class_names = ["True","False"]

xValuesIndex = []
xValues = []
currentFrame = 0
currentRow = 0

with open('/home/laus/uni/thesis/RawData/result.csv', newline='') as csvfile:
	#rowCount = sum(1 for row in csvfile)
	#framesTotal = (rowCount/4)+1
	CSVreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	
	for row in CSVreader:
		currentRow += 1
		currentFrame = int(currentRow / 4)
		
		print(row[currentRow][0])
		cRow = ", ".join(row)
		
		# Save indices of x-values
		if currentRow == (currentFrame*4) + 2:
			# print(currentRow)
			xValuesIndex.append(currentRow)
			# xValues = cRow.
# # variables to keep track
# label = 0
# i = currentFrame
# #j = 80

# # change the current working directory
# os.chdir(output_path)

# for x in xValuesIndex:
# if 
# # get the current path
# cur_path = output_path + "/" + class_names[label] + "/"
# # loop over the images in the dataset
# for image_path in image_paths[i]:
# 	original_path = image_path
# 	image_path = image_path.split("/")
# 	image_path = image_path[len(image_path)-1]
# 	os.system("cp -f " + original_path + " " + cur_path + image_path)
# label += 1
'''
# print end time
print ("[INFO] program ended on - " + str(datetime.datetime.now()))
'''