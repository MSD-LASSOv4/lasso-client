"""\
This script remotes into the Williamson ground station, sends an executable
command, and prints the output.

Usage: python Connect_Server.py
"""

__author__ = "William Liou"
__email__ = "Williamliou1@gmail.com"

import sys
import os
import paramiko
def main():
	print("Connecting to Server...")
	server = paramiko.SSHClient()                                   # Define SSH Client
	server.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
            server.connect("lasso.rit.edu", username="lasso-user", password="p21151SERVER!")    # SSH into Server
            print("Server connection established")
            print(server)
	except paramiko.AuthenticationException:
            print("Authentication Problem")
	except socket.error:
            print("Communication Problem")
	capture_time = sys.argv[1]
	freq = sys.argv[2]
	command = "cd /home/lasso-user/Will-Test; python Connect_Williamson.py "+str(capture_time)+" "+str(freq)
	stdin, stdout, stderr = server.exec_command(command)    # Sends command to Server and recieves output
	errString = stderr.read().decode('ascii').strip("\n")           # Converts error Channelfile to String
	print("Server stderr: " + errString)
	outString = stdout.read().decode('ascii').strip("\n")           # Converts output Channelfile to String
	print("Server output:\n"+ outString + "\n")

if __name__ == "__main__":
	# calling the main function
	main()
