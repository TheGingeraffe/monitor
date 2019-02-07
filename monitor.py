import os
import subprocess

sys_uptime = "uptime | awk -F',' '{print $1}'"
load_average = "uptime | awk -F\"[^0-9]:\" '{print $2}'"
disk_used = "/bin/df -h | grep -vE 'Filesystem|tmpfs'"
mem_used = "free -m"

Uptime = subprocess.Popen(sys_uptime,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
Load = subprocess.Popen(load_average,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
Disk = subprocess.Popen(disk_used,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
Mem = subprocess.Popen(mem_used,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
uptime_output = Uptime.communicate()[0]
load_output = Load.communicate()[0]
disk_output = Disk.communicate()[0]
mem_output = Mem.communicate()[0]
print("Uptime: {}".format(bytes.decode(uptime_output)))
print("Load Average: {}".format(bytes.decode(load_output)))
print("Disk Used:\n {}".format(bytes.decode(disk_output)))
print("Memory Used:\n {}".format(bytes.decode(mem_output)))
 
