from flask import Blueprint, request, render_template, session
from app.services.news_service import *


news = Blueprint('news', __name__)

@news.route('/news', methods=['GET','POST'])
def news_page():
    id = session.get('id')

    news_data = get_all_news_data()

    if request.method == 'GET':
        return render_template('news.html',id=id,
                                           news_data=news_data)



