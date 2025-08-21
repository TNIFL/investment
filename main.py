import secrets
from app.services.community_service import get_post_data_from_db
from flask import Flask, render_template, request, jsonify
from factory import create_app
from app.services.crawling_news import *
from app.services.gpt_services import *


app = create_app()

@app.template_filter('nl2br')
def nl2br(value):
    return value.replace('\n', '<br>\n')


if __name__ == '__main__':
    #crawling_naver_news_by_selenium()
    #translate()
    #crawling_naver_news()
    app.run(host='0.0.0.0', port=80, use_reloader=False, debug=True)
