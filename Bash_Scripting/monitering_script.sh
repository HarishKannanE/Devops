: '
Monitering script to moniter weather httpd service is running or not.
'

ls /var/run/httpd/httpd.pid &> /dev/null

if [ $? -eq 0 ]
    # or if [ -f /var/run/httpd/httpd.pid ]
    # -f checks weather the file exists or not
then
    echo "Httpd process is running."
else
    echo "Httpd process is not running."
    echo "Starting the process."
    systemctl start httpd
    if [ $? -eq 0 ]
    then
        echo "Process started successfully."
    else
        echo "Process starting failed, contact the admin."
    fi
fi