from flask import Blueprint, request, render_template, session

calculator = Blueprint('calculator', __name__)

@calculator.route('/calculator', methods=['GET','POST'])
def calculator_page():
    id = session.get('id')
    if request.method == 'GET':
        return render_template('calculator.html')
    return None