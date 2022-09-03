#!/bin/bash


int_re='^[0-9]+$'

if [ "$EUID" -ne 0 ]; then
    echo "Script not running as root."
    echo "Please run script using sudo/as root."
    exit 1

elif [ $# -ne 1 ]; then
    echo "Invalid number of arguments." >&2
    echo "Script usage: sshd.sh <port_number>" >&2
    exit 1

elif ! [[ $1 =~ $int_re ]]; then
    echo "Input is not an integer." >&2
    echo "Please enter a valid port number." >&2
    exit 1

elif [[ $1 -le 1023 || $1 -ge 49152 ]]; then
    echo "Reserved port number." >&2
    echo "Please choose a port number in range 1024-49151" >&2
    exit 1

else
    port=$1
fi

sed -i "s/#Port/Port/" /etc/ssh/sshd_config
sed -i "s/Port [0-9][0-9]*/Port $port/" /etc/ssh/sshd_config

sed -i "s/#PermitRootLogin/PermitRootLogin/" /etc/ssh/sshd_config
sed -i "s/PermitRootLogin yes/PermitRootLogin no/" /etc/ssh/sshd_config

systemctl restart sshd


users=()
has_access=0
while read line
do
    user="$(echo $line)"
    if [ "$(sudo -l -U $user)" != *"not allowed"* ]; then
        echo "$user has sudo access"
	has_access=1
    fi
done <<< "$(awk -F':' '{ print $1}' /etc/passwd)"

if [[ has_access -eq 0 ]]; then
    echo "No user has sudo access"
fi
