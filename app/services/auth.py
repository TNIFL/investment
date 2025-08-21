from db import get_connection
from flask import render_template, redirect, url_for


def get_user():

    return None

def login_auth(id, password):
    #TODO::DB연동해서 id, pwd 확인 후 리턴
    #TODO::db에서 id, pwd 가져오고 login.py 에서 login_auth 호출 -> 여기서 값 비교 후 login.py 로 리턴

    conn = get_connection()

    try:
        with conn.cursor() as cursor:
            sql = 'SELECT * FROM user WHERE id=%s'
            cursor.execute(sql, (id))
            userData = cursor.fetchone()

            print("입력한 id => ", id,
                  "입력한 password => ", password)
            if userData:
                if userData['password'] == password:
                    print("--------------로그인 성공--------------")
                    print("패스워드 => ", userData['password'], "user 불러옴")
                    return True
                else:
                    print("--------------로그인 실패--------------")
                    print("user를 찾을 수 없거나 password가 틀렸습니다.")
                    return False
            else:
                print("입력한 id는 존재하지 않음")
                return False

    finally:
        conn.close()

def register_duplicate_check(id, password, email):
    #TODO::회원가입 폼 받아와서 db에 동일한 id 존재하는지 확인
    #TODO::동일한 id 존재하면 x, 없으면 db에 저장
    print('!register_duplicate_check!')
    print('입력받은 값 : ', id, password, email)

    conn = get_connection()

    try:
        with conn.cursor() as cursor:
            sql = 'SELECT id FROM USER WHERE id=%s'
            cursor.execute(sql, (id))
            duplicate_check = cursor.fetchone()
            print(duplicate_check)

            if duplicate_check:
                print('중복 존재, 회원가입 실패')
                return False
            else:
                print('중복 존재하지 않음, 회원가입 가능')

                insert_sql = 'INSERT INTO USER (id, password, email) VALUES (%s, %s, %s)'
                cursor.execute(insert_sql, (id, password, email))
                conn.commit()
                print('회원가입 성공')

                return True

    finally:
        conn.close()
