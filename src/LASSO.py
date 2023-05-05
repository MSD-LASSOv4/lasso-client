"""\
This script is the Command Line Interface for LASSO

Usage: LASSO.py -FLAG
"""

__author__ = "William Liou"
__email__ = "Williamliou1@gmail.com"

# importing the required modules
import os
import argparse

# error messages
INVALID_FILETYPE_MSG = "Error: Invalid file format. %s must be a .csv file."
INVALID_PATH_MSG = "Error: Invalid file path/name. Path %s does not exist."

def valid_filetype(file_name):
	# validate csv file type
	return file_name.endswith('.csv')

def raw_data_file(file_name):
        # Verifys Raw Data csv File
        return file_name.startswith('Raw') and file_name.endswith('.csv')

def calculated_data_file(file_name):
        # Verifies Calculated Data csv File
        return file_name.startswith('Calculated') and file_name.endswith('.csv')

def post_processed_data_file(file_name):
        # Verifies Post Processed Data csv File
        return file_name.startswith('Post') and file_name.endswith('.csv')

def valid_path(path):
	# validate file path
	return os.path.exists(path)
		
def show(args):
	# get path to directory
	dir_path = os.getcwd()
	
	# validate path
	if not valid_path(dir_path):
		print("Error: No such directory found.")
		exit()

	# get text files in directory
	files = [f for f in os.listdir(dir_path) if raw_data_file(f)]
	print("\n{} raw capture data file(s) found.".format(len(files)))
	print('\n'.join(f for f in files))
	files = [f for f in os.listdir(dir_path) if calculated_data_file(f)]
	print("\n{} calculated data file(s) found.".format(len(files)))
	print('\n'.join(f for f in files))
	files = [f for f in os.listdir(dir_path) if post_processed_data_file(f)]
	print("\n{} post processed data file(s) found.".format(len(files)))
	print('\n'.join(f for f in files))
	

def delete(args):
	# get the file name/path
	file_name = args.delete[0]
	
	# delete the file
	os.remove(file_name)
	print("Successfully deleted {}.".format(file_name))
	
def rename(args):
	# old file name
	old_filename = args.rename[0]
	# new file name
	new_filename = args.rename[1]

	# renaming
	os.rename(old_filename, new_filename)
	print("Successfully renamed {} to {}.".format(old_filename, new_filename))

def raw_capture():
	os.system("Raw_Capture.py")

def calculated_capture():
	os.system("Calculated_Data.py")

def post_capture():
	os.system("Post_Processing.py")

def connect_lasso(args):
	capture_time = args.lasso[0]
	freq = args.lasso[1]
	os.system("Connect_Server.py "+capture_time+" "+freq)

def main():
	# create parser object
	parser = argparse.ArgumentParser(description = "Welcome to the LASSO CubeSat Ground Station Tracking Interface!\n")
        
	# defining arguments for parser object
	
	parser.add_argument("-s", "--show", type = str, nargs = 1,
						metavar = "path", default = None,
						help = "Shows all the raw/calculated/post processed data files '.' for given directory.")
	
	parser.add_argument("-d", "--delete", type = str, nargs = 1,
						metavar = "file_name", default = None,
						help = "Deletes the specified csv file. (Make sure to include '.csv')")
	
	parser.add_argument("--rename", type = str, nargs = 2,
						metavar = ('old_name','new_name'), default = None,
						help = "Renames the specified csv file to a new name. (Make sure to include '.csv')")

	parser.add_argument("-r", "--raw", action='store_true', default = None,
        					help = "Runs raw data script")

	parser.add_argument("-c", "--calculated", action='store_true', default = None,
        					help = "Runs calculated data script")

	parser.add_argument("-p", "--post", action='store_true', default = None,
        					help = "Runs post processing script")

	parser.add_argument("-l", "--lasso", type = str, nargs = 2,
						metavar = ('capture_time(seconds)','freq(MHz)'), default = None,
        					help = "Connects to LASSO Node Server and runs capture")
	
	# parse the arguments from standard input
	args = parser.parse_args()
	
	# calling functions depending on type of argument
	if args.show != None:
		show(args)
	elif args.delete != None:
		delete(args)
	elif args.rename != None:
		rename(args)
	elif args.raw != None:
                raw_capture()
	elif args.calculated != None:
                calculated_capture()
	elif args.post != None:
                post_capture()
	elif args.lasso != None:
                connect_lasso(args)


if __name__ == "__main__":
	# calling the main function
	main()
