import tempfile, os
from application import main

ALLOWED_EXTENSIONS = set(['zip'])
PATH = os.path.dirname(os.path.realpath(__file__))

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def execute_overview():
    return os.popen(PATH + '/scripts/overview.sh').read()

def save_zip(file):

    if not allowed_file(file.filename):
        return {'status': 'failed', 'message': 'Improper filename'}, 400

    try:
        
        path = PATH + '/uploads'
        file.save(os.path.join(path, file.filename))
        os.system('unzip -: -o -d' + path + ' ' + os.path.join(path, file.filename))

        return {'status': 'success', 'message': f'Upload success'}, 200 

    except:
        return {'status': 'failed', 'message': 'Something went wrong'}, 500
