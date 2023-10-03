# Author: Prof. MM Ghassemi <ghassem3@msu.edu>
from flask import current_app as app
from flask import render_template, redirect, request, session, url_for, copy_current_request_context
from pprint import pprint
import json
import random
import os
import functools
import datetime
import cgitb; cgitb.enable()


APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def root():
    return render_template("index.html")


