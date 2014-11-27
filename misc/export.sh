mysqldump -uroot lerry Log > sql_backup/lerry.sql
DATE=`date +%Y-%m-%d`
mysqldump -uroot lerry Log > sql_backup/lerry_$DATE.sql

