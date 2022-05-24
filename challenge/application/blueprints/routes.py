from flask import Blueprint, request, render_template
from application.util import save_zip, execute_overview
import os

web = Blueprint('web', __name__)
api = Blueprint('api', __name__)

@web.route('/')
def index():
    return render_template('index.html')

@web.route('/firmwareupdate')
def firmwareupdate():
    return render_template('firmwareupdate.html')

@web.route('/overview')
def overview():
    res = execute_overview()
    return render_template('overview.html',var=res)

@api.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return {'status': 'failed', 'message': 'No file provided'}, 400

    file = request.files['file']

    if not file or not file.filename:
        return {'status': 'failed', 'message': 'Something went wrong with the file'}, 400

    return save_zip(file)