import sys, csv

CLASS_FILE_NAME = "pp5i_train_class_transposed.txt"

def stitchFiles(input_file_name_samples, input_file_class, output_file_name):
	#https://stackoverflow.com/questions/3277503/how-do-i-read-a-file-line-by-line-into-a-list
	with open(input_file_name_samples) as samplesFile:
		modified_lines = []

		input_file_class = open(input_file_name_id_class)
				
		out_file = open(output_file_name, "w")
		
		#create a list of lines, stripped of the newline
		sample_content = [line.rstrip('\n') for line in samplesFile]
	
		#create a list of "Class" strings, stripped of the newline
		class_content = [line.rstrip('\n') for line in input_file_id_class]
	
		print("len of sample_content: " + str(len(sample_content)))
		print("len of id_class_content: " + str(len(id_class_content)))
	
		i = 0
		
		sample_no_line = sample_content.pop() #pop the id line, we don't want it
		
		for i in range(0, len(sample_content), 2):
			sample_line = sample_content[i]

			modified_line = id_class_lst[0] + "," + sample_line + "," + id_class_lst[1] + "\n"
				
			#join the stitched line
			modified_lines.append(modified_line)

		out_file.writelines(modified_lines)
		
		return modified_lines
			

		
modified_lines_train = stitchFiles(INPUT_FILE_GCOL_TRAIN, INPUT_FILE_NAME_TRAIN, OUTPUT_FILE_NAME_TRAIN)
modified_lines_test = stitchFiles(INPUT_FILE_GCOL_TEST, INPUT_FILE_NAME_TEST, OUTPUT_FILE_NAME_TEST)