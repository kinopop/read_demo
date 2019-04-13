import pymysql.cursors

#获取链接
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='1234qwer',
                             db='wikiurl',
                             charset='utf8mb4')

try:
    # 获取会话指针
    with connection.cursor() as cursor:
        # 创建SQL语句
        sql = "select `urlname`,`urlhref` from `urls` where `id` is not null"
        # 执行SQL语句
        count = cursor.execute(sql)
        print(count)

        #查询数据
        #result = cursor.fetchall()
        result = cursor.fetchmany(size=3)
        print(result)

finally:
    connection.close()