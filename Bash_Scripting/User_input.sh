: '

User input 
----------
'

echo "Enter your skills:"
read SKILL

echo "Your $SKILL skill is high demand in the IT industry."

read -p 'Username: ' USR
    # -p (is to display a prompt for input)

read -sp 'Password: ' PASS
    # -s (to supress user input text)

echo
echo "Login Successfull,
Welcome $USR."