"""
This is designed to hold all the logic for your program.
"""

import os
import sys

import utility
from logger import Log, SetupLogger


def FileProgramManager(file_extension, action, process_or_port=None):
  """
  This creates or removes the PID or PORT files.
  """

  filepath = utility.LOG_PATH + '/' + utility.PROGRAM_NAME + '.%s' % file_extension


  if (action == "create"):
    if os.path.isfile(filepath):
      Log("%s already exists, exiting" % filepath)
      return False
    else:
      try:
        my_file = open(filepath, 'w')
        my_file.write(process_or_port)
        Log("writing: %s" % filepath)
        my_file.close()
        return True
      except:
        raise

  else:
    Log("removing: %s" % filepath)
    os.unlink(filepath)



def DoEverything():
  """
  This is where all your work goes.
  """
  Log("doing everything!!")




