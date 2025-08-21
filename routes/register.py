from flask import Blueprint, request, render_template
from app.services.auth import register_duplicate_check
from app.services.news_service import get_all_news_data

register = Blueprint('signup', __name__)

@register.route('/register', methods=['GET','POST'])
def register_page():
    if request.method == 'GET':
        return render_template('register.html')

    if request.method == 'POST':
        id = request.form.get('id')
        password = request.form.get('password')
        email = request.form.get('email')

        register_result = register_duplicate_check(id, password, email)

        if register_result: #True
            return render_template('mainpage.html', message='회원가입 성공', latest_news=get_all_news_data())
        else:
            return render_template('register.html', message='회원가입 실패')

        return render_template('register.html')
