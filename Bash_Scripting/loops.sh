for VAR in java .net python ruby php
do
    echo "Value of VAR is $VAR."
    sleep 1
done

MYUSERS="alpha beta gamma"

for usr in $MYUSERS
do
    echo "Adding user $usr."
    useradd $usr
    id $usr
done