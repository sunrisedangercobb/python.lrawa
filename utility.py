"""
Description
"""

import os
import logging

from logger import Log, SetupLogger



PROGRAM_NAME = 'program'
LOG_PATH = 'logs'


# Time in seconds to wait between scanning
SCAN_PERIOD = 10.0

PID = str(os.getpid())


# Api vars
PORT = '7000'
HOST = '127.0.0.1'

# Set to true when you want to close the long running job
QUITTING = False
RUNNING = False


def SetQuit(value):

  global QUITTING
  QUITTING = value
  Log('quitting: %s' % QUITTING, logging.DEBUG)

  GetQuit()


def GetQuit():

  global QUITTING
  Log('is quitting: %s' % QUITTING, logging.DEBUG)
  return QUITTING

def GetRunning():

  global RUNNING
  Log('is RUNNING: %s' % RUNNING, logging.DEBUG)
  return RUNNING


def SetRunning(value):
  global RUNNING
  RUNNING = value


