# Basic-Python-Backdoor
It is basic backdoor created using python.

# Usage : 
At first you need to chnge ip address of your listener system inside both the backdoor and listener python scripts.
Then rename the backdoor scripts to a familiar windows program such as scvhost,system,...etc.
In any windows system you can use pyinstaller to convert backdoor into .exe file.
Now now you can send this payload to the target. When target executes the payload you will get connection on the listener.
# Working :
Once target executed the payload then it tries to connect to listener in every 20 seconds if it not not connected.
Once it is connected to listener then you can execute commands on terget machine remotely from listener.
