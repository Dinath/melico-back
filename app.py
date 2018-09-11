from config import Config
from ctrl.infos import Infos
from ctrl.email import Email
from ctrl.generate import Generate

from flask import Flask, request, send_from_directory
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS, cross_origin

import daemon
import sys
import os

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": Config.DOMAIN_AUTH}})
auth = HTTPBasicAuth()


"""
    Password auth
"""
@auth.get_password
def __pwd(username):
    if username in Config.USERS_AUTH:
        return Config.USERS_AUTH.get(username)
    return None

"""
    Used to generate the application
"""
@app.route("/app/post/generate", methods=['POST'])
@auth.login_required
def generate():
    Infos.dbMelicoWanted(Config, request.json)
    if os.path.isfile(Config.GEN_ANDROID_PATH_APK + '/' + Config.GEN_ANDROID_PATH_APK_FILE):
        os.remove(Config.GEN_ANDROID_PATH_APK + '/' + Config.GEN_ANDROID_PATH_APK_FILE)
    Generate.go(Config, request.json)
    return send_from_directory(Config.GEN_ANDROID_PATH_APK, Config.GEN_ANDROID_PATH_APK_FILE, as_attachment=True)

"""
    Send an email from contact
"""
@app.route("/app/post/email", methods=['POST'])
@auth.login_required
def email():
    Email.send(request.json)
    return ''

# """
#     Informations from client's melico
# """
# @app.route("/app/post/infos", methods=['POST'])
# @auth.login_required
# def infos():
#     Infos.dbMelicoWanted(Config, request.json)
#     return ''

"""
    Count the applications being generated
"""
@app.route("/app/get/generate-count", methods=['GET'])
@auth.login_required
def generateCount():
    return str(len(Generate.queue))


if __name__ == "__main__":

    # test
    if Config.DEBUG:
        app.run(debug=True)
        
    # prod
    else:
        with daemon.DaemonContext():
            app.run(threaded=True)

    # app.run(debug=True) if Config.DEBUG else app.run(threaded=True)

