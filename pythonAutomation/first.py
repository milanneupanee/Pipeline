#In linux machine
#TO run command in the python we need to install the liabrary calleed os
#example: 
import os
#os.system("ls")//for linux
#os.system("dir")//for windows

#!/usr/bin/python3 #It is the path for interpeter
import os

userlist=["alpha","Beta","gamma"]

print("Adding the user in the system")
print("#############################################")

# loop for the list of the user
for user in  userlist:
    exitcode = os.system("id {user}")
    if exitcode != 0:
        print("No user exitst in the system")
        print("Adding the user {user}")
        os.system("adduser {user}")
    else:
        print("User exist already")

#Condition to check the group
exitcodes=os.system("grep science /etc/group")
if exitcodes!= 0:
    print("Does not exist")
    os.system("groupadd science")
else:
    print("Already exist")


#adding user in the group
for user in userlist:
    os.system("usermod -G science {user}")


#python fabric library
#To install fabric
# pip install fabric or we can follow any documentation
# try to search also python library for jenkins
# pip install python-jenkins
# also read the documentation

#while using the fabric file name shoulf be fabfile.py
# the function or method which are decleare in the above file can be looked by
# followinf command 
# fab -l
# to  call it   
# fab mrthod:argument
from fabric.api import *
def system_info():
    print ("disk space:")
    local("df -h")

    print("ram size")
    local("free -m")

    print("system up time")
    local("uptime")

# to execute any command in remote machine
def remote_exec():
    run("hostname")
    run("uptime")
    run("free -m")
    sudo("systemctl reboot sshd") # it will also work with sudo privilage

#to execute this code in shell 
# for that we need to create user in remote machine with the sudo previlages
# for that visudo-> add line under root -> devops ALL=(ALL) NOPASSWD:ALL
# also enable the password based login for the sshd
# for ssh key login generate the key copy to other machine and disable password based login
# for that ssh-key-id devops@ipaddr

fab remote_exec -H ipaddr -u username scriptsmethid