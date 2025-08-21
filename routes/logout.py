from flask import redirect, session, url_for, Blueprint

logout = Blueprint('logout', __name__)

@logout.route('/logout')
def logout_page():
    if session.pop('id', None):
        print("session pop 완료")

    return redirect(url_for('mainpage.index', id=None))