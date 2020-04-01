from flask import Blueprint, jsonify, request, render_template

homeBP = Blueprint('homeBP', __name__)


@homeBP.route('/', methods=['GET'])
def progressive_optimal():
    return render_template('index.html', title='Home')