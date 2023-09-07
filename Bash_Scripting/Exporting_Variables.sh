: ' 
Exporting Variables 
-------------------

when we set variable in shell, it can be used on shell only not
in a script (child-shell) so we have to export the variable from
parent shell

'

CURRENT_USER=$(who)
    # setting up an variable.

export CURRENT_USER
    # Exporting the variable to child-shell from parent-shell

 
: '
To make variable permenent for user you have to export it in the .bashrc file.
.bashrc file is user specific.
'

vim .bashrc
    export SEASON="Monsoon"

source .bashrc
    # in order to apply change in .bashrc file u have to use source command or restart the shell

: '
 To make variable permenent globally u have to add export in /etc/profile file.
.bashrc file can override /etc/profile file.
'

vim /etc/profile
    export SEASON="Monsoon"