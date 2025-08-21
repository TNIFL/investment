from flask import Blueprint, request, render_template, redirect, url_for, session
from app.services.auth import login_auth

login = Blueprint('login', __name__)

@login.route('/login', methods=['GET','POST'])
def login_page():
    if request.method == 'POST':
        id = request.form['id']
        password = request.form['password']

        #auth에 id, pwd 보내주고 login_auth에서 값 확인 후 리턴
        login_result = login_auth(id, password)

        if login_result == True:
            session_result = session['id'] = id
            if session_result:
                print("session in")
                print(session)
            return redirect(url_for('mainpage.index'))
        elif login_result == False:
            return render_template('login.html', alert_message="로그인 실패")


    return render_template('login.html')