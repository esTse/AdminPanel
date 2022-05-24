printf "System info:\n\n"
uname=$(uname -a)
echo "${uname}\n\n"
printf "Tree of files in server"
tree=$(tree)
echo "${tree}\n\n"
printf "Top command output:\n\n"
top=$(top -b -n 3 | head -5)
echo "${top}\n\n"
printf "Space information (free):\n\n"
free=$(free)
echo "${free}\n\n"
printf "Time from last power-up:\n\n"
uptime=$(uptime)
echo "${uptime}\n\n"
printf "Hardware info:\n\n"
lscpu=$(lscpu)
echo "${lscpu}\n\n"
printf "Storage information:\n\n"
lsblk=$(lsblk)
echo "${lsblk}\n\n"
