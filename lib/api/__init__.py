import json,threading
from lib.log import logger
import lib.util as active
from flask import Flask,request
from flask.ext.cors import CORS


def routing(app):

    @app.route('/api', methods=['GET'])
    def hello_word():

        logger.info("Received %s" %(request.url))
        return

    @app.route('/api/getStatus', methods=['GET'])
    def getStatus():
        logger.info("Received %s" %(request.url))
        return json.dumps(active.getActive())

    @app.route('/api/setStatus', methods=['GET'])
    def setStatus():
        newStatus = request.args.get('status')
        logger.info("Received %s" %(request.url))
        active.setActive(newStatus)
        return json.dumps(active.getActive())


def createApp():
    app = Flask(__name__)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    routing(app)
    app.run('0.0.0.0')


def lunch():
    th = threading.Thread(target=createApp)
    th.setDaemon(False)
    th.start()
    return th.isAlive()