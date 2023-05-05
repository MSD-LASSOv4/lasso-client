# lasso-client
This repository is intended to encompass the client for communication with the server. 

## /src

### LASSO.py (Run on Local PC)
This is the Command Line Interface that is used by local PC to interact with server and run captures.

### Connect_Server.py (Run on Local PC)
This script does an ssh into the server and executes specified command. Currently it takes in capture time and frequency as parameters and uses them to execute the Connect_Williamson.py script as shown below. 
<img width="627" alt="image" src="https://user-images.githubusercontent.com/70246251/236528438-61fbed7f-aa45-410a-b6d6-fc94fc3359a7.png">

### Connect_Williamson.py (Run on Server)
This script will ssh into the Williamson pi and run a capture based off the given frequency and capture time parameters.


