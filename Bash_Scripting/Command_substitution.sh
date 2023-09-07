# Command substitution
# --------------------

CURRENT_USER=$(who)
    # storing the value of 'who' command in 'CURRENT_USER' variable.
echo $CURRENT_USER

FREE_RAM=$(free -m | grep Mem | awk '{print $4}')
    # storing free ram info in FREE_RAM variable
echo $FREE_RAM
echo "Free ram is $FREE_RAM mb."
