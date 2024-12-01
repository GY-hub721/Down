import mysql.connector

try:
    # 连接到 MySQL 数据库
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="task"
    )

    cursor = connection.cursor()

    # 创建表，设置id为自增主键
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS db_user (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50),
            age INT,
            gender VARCHAR(10)
        )
    """)

    # 插入单条数据，使用占位符
    sql = "INSERT INTO db_user (name, age, gender) VALUES (%s, %s, %s)"
    val = ("喜羊羊", 18, "男")
    cursor.execute(sql, val)
    connection.commit()

    # 插入多条数据，使用占位符
    val = [
        ("废羊羊", 18, "男"),
        ("懒羊羊", 18, "男"),
    ]
    cursor.executemany(sql, val)
    connection.commit()

    # 更新数据，使用占位符
    sql = 'UPDATE db_user SET name=%s WHERE name=%s'
    val = ("沸羊羊", "废羊羊")  # 假设你是想将"沸羊羊"更新为"废羊羊"
    cursor.execute(sql, val)
    connection.commit()

    # 删除数据，使用占位符
    sql = "DELETE FROM db_user WHERE name=%s"
    val = ("懒羊羊",)
    cursor.execute(sql, val)
    connection.commit()

    # 查询数据并输出
    cursor.execute("SELECT * FROM db_user")
    result = cursor.fetchall()
    columns = [column[0] for column in cursor.description]

    # 格式化输出
    for row in result:
        print(dict(zip(columns, row)))

except mysql.connector.Error as err:
    # 输出错误信息
    print("MySQL Error: {}".format(err))

finally:
    # 关闭游标和连接
    cursor.close()
    connection.close()
