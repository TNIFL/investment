from flask import Flask
from routes.calculator import calculator
from routes.community import community
from routes.investment_propensity_analysis import investment_propensity_analysis
from routes.login import login
from routes.mainpage import mainpage
from routes.news import news
from routes.register import register
from routes.logout import logout
from routes.mypage import mypage

from dotenv import load_dotenv
import os


def create_app():
    app = Flask(__name__)

    app.secret_key = os.getenv("SECRET_KEY")

    app.register_blueprint(mainpage)
    app.register_blueprint(calculator)
    app.register_blueprint(community)
    app.register_blueprint(investment_propensity_analysis)
    app.register_blueprint(login)
    app.register_blueprint(news)
    app.register_blueprint(register)
    app.register_blueprint(logout)
    app.register_blueprint(mypage)

    return app