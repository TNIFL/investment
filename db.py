import pymysql

#배포나 실제로 운영할 시 보안을 위해 이 정보들은 .env나 설정파일에 분리 해야함.

def get_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='031002',
        db='investment',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )