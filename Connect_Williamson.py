"""\
This script remotes into the Williamson ground station, runs capture script
command, and prints the output.

Usage: python Connect_Williamson.py
"""

__author__ = "William Liou"
__email__ = "Williamliou1@gmail.com"

import sys
import os
import paramiko

def main():
	print("Connecting to Williamson Ground Station...")
	williamson = paramiko.SSHClient()                                     # Define SSH Client
        williamson.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            williamson.connect("100.95.247.44", username="pi", password="Lasso123!")         # SSH into Mees PI
            print("Williamson connection established")
            print(williamson)
        except paramiko.AuthenticationException:
            print("Authentication Problem")
        except socket.error:
            print("Communication Problem")
	capture_time = sys.argv[1]      # User-inputted Capture-time parameter
	freq = sys.argv[2]              # User-inputted frequency parameter
	scp_command = "sshpass -p 'p21151SERVER!' scp output_samples.raw lasso-user@lasso.rit.edu:/home/lasso-user/capture-files"       # SCP command to be sent
	command = "cd /home/pi/Jack-Test;sudo ./hTest "+str(capture_time)+" "+str(freq)+";"+str(scp_command) # SSH into williamson pi, run capture script and send output to server
	stdin, stdout, stderr = williamson.exec_command(command) # Send Command to PI and recieves outputs
	errString = stderr.read().decode('ascii').strip("\n")           # Converts error Channelfile to String 
        print("Williamson stderr: " + errString)
        outString = stdout.read().decode('ascii').strip("\n")           # Convers output Channelfile to String
        print("Williamson output:\n" + outString)

if __name__ == "__main__":
	# calling the main function
	main()
