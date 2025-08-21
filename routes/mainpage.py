from flask import Flask, render_template, redirect, Blueprint, request, session
from dotenv import load_dotenv
from app.services.news_service import *
import os

load_dotenv()

mainpage = Blueprint('mainpage', __name__)

@mainpage.route('/', methods=['GET', 'POST'])
def index():
    id = session.get('id')
    if request.method == 'GET':
        print("------------mainpage------------")
        if id:
            print("현재 id => {id}")
            return render_template('mainpage.html', id=id, latest_news=get_all_news_data())
        else:
            print("로그인 안됨")
            return render_template('mainpage.html', id=None, latest_news=get_all_news_data())