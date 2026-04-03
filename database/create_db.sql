drop database surdb;
drop role suradmin;
create role suradmin with login password 'surpass';
create database surdb owner suradmin;