"""
Description
"""

import os
import time
import logging
import threading
from flask import Flask, jsonify, request, make_response

import logic
import utility
from logger import Log


# setup the app
app = Flask(__name__)


# setup the error handlers
@app.errorhandler(400)
def not_found(error):
  return make_response(jsonify( { 'error': 'Bad request' } ), 400)


@app.errorhandler(404)
def not_found(error):
  return make_response(jsonify( { 'error': 'Not found' } ), 404)

# example setting static url
@app.route('/api/quit', methods = ['GET'])
def shutdown():
  Log('shut down event triggered')

  utility.SetQuit(True)

  while utility.GetRunning():
    Log('waiting for process to complete...')

    time.sleep(5.0)

  func = request.environ.get('werkzeug.server.shutdown')
  if func is None:
      raise RuntimeError('Not running with the Werkzeug Server')
  func()

  return make_response(jsonify( { 'result': 'quitting' } ), 200)


# example of processing uri
@app.route('/api/', methods = ['GET'])
def get_command():

  #http://<HOST>:<PORt>/api?command=quit

  command = request.args['command']

  ## do your logic here

  return make_response(jsonify( { "command": command } ), 200)



def StartApp():

  # this surpresses all the flask messages to sdout
  logging.getLogger('werkzeug').disabled = True
  os.environ['WERKZEUG_RUN_MAIN'] = 'true'  

  try:
    # starting the api in it's own thread
    threading.Thread(target=app.run, kwargs={'host': utility.HOST, 'debug': False, 'port': utility.PORT}).start()


    Log("starting API")
  except:
    Log("Exiting main")


if __name__ == '__main__':
    StartApp()


