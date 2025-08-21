import pymysql

from db import get_connection
from datetime import datetime

#db에 저장 할 값은 url, title, time, content, summary 등 많음
#db 설계 다시 해야함

def save_news_with_category(title, content, summary, category, url, upload_time):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = 'INSERT INTO NEWS (title, content, summary, category, url, upload_time) VALUES (%s, %s, %s, %s, %s, %s)'
            cursor.execute(sql, (title, content, summary, category, url, upload_time))
            conn.commit()

            print('DB에 뉴스 저장 성공')
            return True
    except Exception as e:
        print('db에 저장하던 중 오류발생 : ', e)
        return False
    finally:
        conn.close()

def get_all_news_data():
    conn = get_connection()

    try:
        with conn.cursor() as cursor:
            sql = 'SELECT * FROM NEWS'
            cursor.execute(sql)
            news_data = cursor.fetchall()

            if news_data:
                return news_data
            else:
                return False

    finally:
        conn.close()

def parse_korean_datetime(kor_time_str):
    kor_time_str = kor_time_str.replace('오전', 'AM').replace('오후', 'PM')
    return datetime.strptime(kor_time_str, '%Y.%m.%d. %p %I:%M')