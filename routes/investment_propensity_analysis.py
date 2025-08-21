from flask import Blueprint, request, render_template, session

investment_propensity_analysis = Blueprint('investment_propensity_analysis', __name__)

@investment_propensity_analysis.route('/investment_propensity_analysis', methods=['GET','POST'])
def investment_propensity_analysis_page():
    id = session.get('id')
    if request.method == 'GET':
        return render_template('investment_propensity_analysis.html')

    if request.method == 'POST':
        return render_template('investment_propensity_analysis.html')
    return None