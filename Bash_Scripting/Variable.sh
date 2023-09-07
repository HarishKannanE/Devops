: '
Variable
--------
'

SKILL="Devops"
    # Storing value "Devops" in the variable SKILL

echo $SKILL
    # printing value form variable

PACKAGE="wget httpd unzip"
    # Storing value "wget httpd unzip" in the variable PACKAGE

yum install $PACKAGE -y
    # using value form variable