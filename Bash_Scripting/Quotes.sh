: '
Quotes
------
'

SKILL="Devops"

echo "I have got $SKILL skill."
    # double quotes considers value of the special character.
# output
I have got Devops skill.

echo 'I have got $SKILL skill.'
    # single-quote does not consider value of the special character
#output
I have got $SKILL skill.

# using variables and characters in same statement

VIRUS="covid19"

echo "Due to $VIRUS virus company have lost $9 million."
# output
Due to covid19 virus company have lost  million.

echo 'Due to $VIRUS virus company have lost $9 million.'
# output
Due to $VIRUS virus company have lost $9 million.

echo 'Due to $VIRUS virus company have lost \$9 million.'
#output
Due to covid19 virus company have lost $9 million