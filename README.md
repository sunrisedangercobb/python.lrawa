# python_template-lrawa
Long Running App With API

== Python Template: Long Running w/API ==

This is an application template for a long running process with an API.  The 
API is meant to run sidecar to the main program and provide access / control methodology, it is not designed to be an API first.

Flask is a pain in the ass with how it wants to run.  This is a normal use case / pattern that Flask has chosen to make a pain in the ass, so this treats Flask in a 
very hacky work around way to get the functionality that we really want out of it.

This template was designed to be compatible with python 2.xx and 3.xx.  That being
said it was written in python3 so you may encounter issues running 2.xx as it wasn't
comprehensively tested for 2.xx.


Required Libraries:
 - flask

== TODO: ==

TODO(sunrise): add in a route for debug so you can set debug through the API.
TODO(sunrise): fix up the logger to work with this methodology. GetLogLevel SetLogLevel

