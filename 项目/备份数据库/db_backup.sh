#!/bin/bash

# 1.数据库信息
db_ip="10.101.4.31"
db_port="3306"
db_user="test"
db_passwd="test"
db_name="so_auto_comp"
db_backpath="/home/guosheng/db_backup/his"
 
# 2.处理备份路径及备份时间
echo "ready to backup database, the folder is $db_backpath"
mkdir $db_backpath -p && cd $db_backpath
backup_time=$(date "+%Y%m%d-%H%M")
 
# 3.执行mysql备份
back_file_name="$db_name-$backup_time.sql"
/usr/bin/mysqldump -h$db_ip -P$db_port -u$db_user -p$db_passwd --databases $db_name --column-statistics=0 > "$db_backpath/$back_file_name"
echo "database $db_name backup success"
 
# 删掉当前目录10天之前的备份文件
find $db_backpath -mtime +10  -name "*.sql" -exec rm -rvf {} \;


local_ip=`/usr/sbin/ifconfig -a | grep -m 1 -w "inet" | awk '{print $2}'`
echo "local_ip=$local_ip"
echo "db_name=$db_name"
echo "back_file_path=$db_backpath/$back_file_name"
