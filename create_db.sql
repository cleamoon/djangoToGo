create database djangodb default charset utf8;
create user 'django'@'localhost' identified by 'djangoPassword';
grant all privileges on djangodb.* to 'django'@'localhost' identified by 'djangoPassword';
flush privileges;