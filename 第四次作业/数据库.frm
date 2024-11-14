mysql> drop database task;
Query OK, 0 rows affected (0.01 sec)

mysql> create database task;
Query OK, 1 row affected (0.00 sec)

mysql> use task;
Database changed
mysql> create table tb_user(
    -> id int comment '编号',
    -> name varchar(50) comment'名字',
    -> age int comment '年龄',
    -> gender varchar(1) comment '性别'
    -> )comment '用户信息表';
Query OK, 0 rows affected (0.01 sec)

mysql> show tables;
+----------------+
| Tables_in_task |
+----------------+
| tb_user        |
+----------------+
1 row in set (0.00 sec)

mysql> desc tb_user;
+--------+-------------+------+-----+---------+-------+
| Field  | Type        | Null | Key | Default | Extra |
+--------+-------------+------+-----+---------+-------+
| id     | int         | YES  |     | NULL    |       |
| name   | varchar(50) | YES  |     | NULL    |       |
| age    | int         | YES  |     | NULL    |       |
| gender | varchar(1)  | YES  |     | NULL    |       |
+--------+-------------+------+-----+---------+-------+
4 rows in set (0.00 sec)

mysql> show create table tb_user;
+---------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Table   | Create Table

                                                                  |
+---------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| tb_user | CREATE TABLE `tb_user` (
  `id` int DEFAULT NULL COMMENT '编号',
  `name` varchar(50) DEFAULT NULL COMMENT '名字',
  `age` int DEFAULT NULL COMMENT '年龄',
  `gender` varchar(1) DEFAULT NULL COMMENT '性别'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='用户信息表' |
+---------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
1 row in set (0.00 sec)