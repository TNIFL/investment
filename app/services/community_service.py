from db import get_connection
import sys

def get_post_data_from_db():
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = 'SELECT * FROM POST'
            cursor.execute(sql)
            posts = cursor.fetchall()

            print('현재 게시글 불러오기')

            #for post in posts:
            #    print(post)


            if posts:
                print('현재 게시글 불러오기 성공')
                return posts
            else:
                print('현재 게시글 불러오기 실패')
                return None
    finally:
        conn.close()

def get_post_by_post_id(post_id):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = 'SELECT * FROM POST WHERE id=%s'
            cursor.execute(sql, (post_id,))
            result = cursor.fetchone()

            return result
    finally:
        conn.close()

def create_post(user_id, title, content):
    conn = get_connection()
    print('현재 사용자 id : ', user_id)
    try:
        with conn.cursor() as cursor:
            sql = 'INSERT INTO POST (user_id, title, content) VALUES (%s, %s, %s)'
            cursor.execute(sql, (user_id, title, content))
            conn.commit()

            print('게시글 작성 성공')
            return True
    except Exception as e:
        print('게시글 작성 실패 : ', e)
        return False
    finally:
        conn.close()

def update_post(post_id, updated_title, updated_content):
    conn = get_connection()

    try:
        with conn.cursor() as cursor:
            sql = 'UPDATE POST SET title=%s, content=%s WHERE id=%s'
            cursor.execute(sql,(updated_title, updated_content, post_id))
            conn.commit()
            return True

    except Exception as e:
        print('POST 업데이트 중 오류 발생 : ', e)
        return False

    finally:
        conn.close()


def get_comment_by_post_id(post_id):
    conn = get_connection()

    try:
        with conn.cursor() as cursor:
            sql = 'SELECT * FROM COMMENT WHERE post_id=%s'
            cursor.execute(sql, (post_id))
            result = cursor.fetchall()
            return result

    except Exception as e:
        print('댓글 가져오기 실패 : ', e)
        return False
    finally:
        conn.close()

    return None

def insert_comment_by_post_id(post_id, user_id, insert_comment):
    if user_id is None or insert_comment is None:
        return False

    if user_id:
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                sql = 'INSERT INTO COMMENT (post_id, user_id, content) VALUES (%s, %s, %s)'
                cursor.execute(sql, (post_id, user_id, insert_comment))
                conn.commit()
                return True
        except Exception as e:
            print('DB에 댓글 삽입 중 오류 발생 : ', e)
            return False
        finally:
            conn.close()

def get_post_id_from_post_title(title):
    conn = get_connection()

    try:
        with conn.cursor() as cursor:
            sql = 'SELECT id FROM POST WHERE title=%s'
            cursor.execute(sql, (title))
            result = cursor.fetchone()
            return result
    except Exception as e:
        print('DB(POST)에서 title로 id 가져오다가 오류 발생 : ', e)
        return False

    finally:
        conn.close()

def increment_click_count(post_id):
    try:
        conn = get_connection()
        with conn.cursor() as cursor:
            sql = 'UPDATE POST SET click_count = click_count + 1 WHERE id=%s'
            cursor.execute(sql, (post_id,))
            conn.commit()
            return True
    except Exception as e:
        print('click_count 증가 중 오류 발생 : ', e)
        return False
    finally:
        conn.close()
