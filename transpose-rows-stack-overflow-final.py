#https://unix.stackexchange.com/questions/60590/is-there-a-command-line-utility-to-transpose-a-csv-file

import csv, sys

#constants
DEBUG = True
INPUT_FILE_NAME_TRAIN_30 = "pp5i_train.top30.gr.unique.csv"
OUTPUT_FILE_NAME_TRAIN_30 = "pp5i_train.top30.gr.unique.transposed.csv"

def transposeRows(input_file_name, output_file_name):
	with open(input_file_name) as file:
		out_file = open(output_file_name, "w")
		rows = list(csv.reader(file))
		writer = csv.writer(out_file)
		for col in range(0, len(rows[0])):
			writer.writerow([row[col] for row in rows])
			
transposeRows(INPUT_FILE_NAME_TRAIN_30, OUTPUT_FILE_NAME_TRAIN_30)