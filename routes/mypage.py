from flask import Flask, Blueprint, request, session, render_template
from app.services.community_service import get_post_data_from_db
from app.services.news_service import get_all_news_data

mypage = Blueprint('mypage', __name__)

@mypage.route('/mypage', methods=['GET', 'POST'])
def my_page():
    id = session.get('id')

    posts = get_post_data_from_db()
    news_data = get_all_news_data()

    if request.method == 'GET':
        return render_template('mypage.html', id=id,
                                              posts=posts,
                                              news_data = news_data)
