: '
"If" "else" statement
---------------------
'

read -p "Enter a number: " NUM
echo

if [ $NUM -gt 100 ]
then
    echo "We have entered in IF block."
    sleep 3
    echo "Yes your Number is greater than 100"
    echo
    date
else
    echo "Your number is less than 100."
fi

echo "Script execution completed successfully."

: '
"elif" statement
---------------- 
'

value=$(ip addr show | grep -v LOOPBACK | grep -c mtu)

if [ $value -eq 1 ]
then
    echo "1 active interface found."
elif [ $value -gt 1 ]
then
    echo "Found multiple active interfaces."
else
    echo "No active interface found."
fi