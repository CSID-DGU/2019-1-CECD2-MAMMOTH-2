#!/bin/sh

:<<'END'
1.1 버전 최신이면 종료 *
1.2 버전 최신 아니면 다운로드 시작 *
2. 반복문 이용해서 다운로드 *
3. 다운 받은 파일 해시 때고 따로 텍스트 파일에 저장 *

4. 다운 받은 파일 해시 돌리기 *
5. 해시 값 비교 *
6. 이상 없으면 다음 파일 다운로드 *
7. 다 다운로드 받으면 병합
8. 파일 실행
END

file_number=1
dev_id=1
check=$( curl http://localhost:8000/check_version/1/ )
if [ $check == "n" ];then
    for ((i=0;i<3;i++))
    do
        curl http://localhost:8000/download/iphone/$dev_id/$file_number/ --output test_pic_z_$file_number.png
        ./binary_recov test_pic_z_$file_number.png
        ./make_hash test_pic_z_$file_number.png
        SERVER_HASH=$( cat server_hash.txt )
        SERVER_CSR=$( cat server_cert.csr )
        NEW_HASH=$( cat new_hash.txt )
        CLIENT_CSR=$( cat client_cert.csr )
        if [ "$SERVER_CSR" == "$CLIENT_CSR" ] && [ "$SERVER_HASH" == "$NEW_HASH" ]; then
            file_number=`expr 1 + $file_number`
        fi
    done
fi

