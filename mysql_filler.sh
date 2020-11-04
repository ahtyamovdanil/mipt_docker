#!bin/bash
mysql -u root -p24812481 -h db -e "load data local infile '$1' into table test_db.potluck fields terminated by ',' enclosed by '"' lines terminated by '\n'"