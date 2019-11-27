#!/bin/sh

file_number=1

check=$( curl http://gudah100.pythonanywhere.com/check_version/$1/)

if [ $check == "y" ];then
    while [ $file_number -lt 11 ]
    do
        curl http://gudah100.pythonanywhere.com/download/iphone/$1/$file_number/ --output OK_version.ino.$file_number
        ./binary_recov OK_version.ino.$file_number
        ./make_hash OK_version.ino.$file_number
        SERVER_HASH=$( cat server_hash.txt )
        SERVER_CSR=$( cat server_cert.csr )
        NEW_HASH=$( cat new_hash.txt )
        CLIENT_CSR=$( cat client_cert.csr )
        if [ "$SERVER_CSR" == "$CLIENT_CSR" ] && [ "$SERVER_HASH" == "$NEW_HASH" ]; then
            file_number=$(($file_number+1))
        elif [ "$SERVER_HASH" != "$NEW_HASH" ]; then
            echo " HASH ERROR "
:<<'END'
            ./cli compile —fqbn arduino:avr:uno /home/pi/arduino/AuthFailed/
            ./cli upload -p /dev/ttyACM0 —fqbn arduino:avr:uno AuthFailed/
END
            exit 1
        elif [ "$SERVER_CSR" != "$CLIENT_CSR" ]; then
            echo " CSR ERROR "
:<<'END'
            ./cli compile —fqbn arduino:avr:uno /home/pi/arduino/AuthFailed/
            ./cli upload -p /dev/cu.usbmodem14101 —fqbn arduino:avr:uno AuthFailed/
END
            exit 1
        fi
    done
:<<'END'
    rm -r OK_version
END
    ./splitter -j OK_version.ino.1 OK_version.ino
:<<'END'
    ./cli compile —fqbn arduino:avr:uno /home/pi/arduino/AuthFailed/
    ./cli upload -p /dev/ttyACM0 —fqbn arduino:avr:uno AuthFailed/
END
    curl -X POST http://gudah100.pythonanywhere.com/upgrade_version/$1/
else
    echo "already newest version"
fi

