#!/bin/bash/

echo "Starting execution script..."

#F2099
python "7_create_folders.py"

#Brian

python "user_input.py"
python "2confirm.py"

#Dante

python "4a_department_only.py" 
if [ $? -ne 0 ]; then
    echo "Department verification failed. Stopping."
    exit 1
fi

python "9_show_checkin_output.py"


#Tylo

python "5_check_last_checkin.py"
python "6_checkin_status.py"


#F2099
python "8a_test-export.py"



echo "Ending execution script..."