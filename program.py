#!/usr/bin/env python

"""
This is your main program and you should name it according to that. This
project is meant to serve as a template to help create consistency in the 
creation of long running python3 programs.
"""

__authors__ = ['Sunrise Cobb', 'Geoff Howland']



import os
import sys
import time
import logging
import traceback

from logger import Log, SetupLogger

import logic
import utility


# this captures the path for the following includes
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )


def RunForever():


  utility.SetRunning(True)

  try:
    while not utility.GetQuit():

      logic.DoEverything()

      Log('sleeping: %s' % utility.SCAN_PERIOD)
      time.sleep(utility.SCAN_PERIOD)


  except Exception as e:
    (exc_type, exc_value, exc_traceback) = sys.exc_info()
    traceback_output = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    Log('Exception while executing: %s\n\n%s' % (e, traceback_output), logging.ERROR)

    raise

  finally:
    #INFO: all your clean up logic has to go here
    logic.FileProgramManager('pid', 'delete', '%s' % utility.PID)
    logic.FileProgramManager('port', 'delete', '%s' % utility.PORT)

    utility.SetRunning(False)


def Main():
  """
  Args: None
  Returns: None
  """

  SetupLogger('%s/%s.log' % (utility.LOG_PATH, utility.PROGRAM_NAME))

  try:
    # setup the api
    import api
    api.StartApp()

    # write pid and port data to disk
    logic.FileProgramManager('pid', 'create', '%s' % utility.PID)
    logic.FileProgramManager('port', 'create', '%s' % utility.PORT)

    # start our long running process
    RunForever()

  except Exception as e:
    (exc_type, exc_value, exc_traceback) = sys.exc_info()
    traceback_output = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    Log('Exception while executing: %s\n\n%s' % (e, traceback_output), logging.ERROR)

    raise


if __name__ == '__main__':
  Main()


