CREATE DATABASE iei_n4_c3;

CREATE USER 'iei-n4-c3'@'localhost' IDENTIFIED BY 'iein4c3';

GRANT ALL PRIVILEGES ON iei_n4_c3.* TO 'iei-n4-c3'@'localhost';

FLUSH PRIVILEGES;