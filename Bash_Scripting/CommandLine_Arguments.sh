: '
Command line Arguments
----------------------
can use arguments from $1-$9
'

# script first_script.sh

echo "Value of 0 is :"
echo $0

echo "Value of 1 is :"
echo $1

echo "Value of 2 is :"
echo $2

echo "Value of 3 is :"
echo $3

# bash first_sript.sh

#output
Value of 0 is :
first_script.sh
Value of 1 is :

Value of 2 is :

Value of 3 is :

# bash first_sript.sh ansible

#output
Value of 0 is :
first_script.sh
Value of 1 is :
ansible
Value of 2 is :

Value of 3 is :

# bash first_sript.sh ansible aws

#output
Value of 0 is :
first_script.sh
Value of 1 is :
ansible
Value of 2 is :
aws
Value of 3 is :