import os
from datetime import datetime

sys_uptime = "uptime | awk -F',' '{print $1}'"
load_average = "uptime | awk -F',' '{print $4 $5 $6}'"
disk_used = "/bin/df -h | grep -vE 'Filesystem|tmpfs'"
mem_used = "free -m"
check_services = "service --status-all"

os.system(sys_uptime)
os.system(load_average)
os.system(disk_used)
os.system(mem_used)

