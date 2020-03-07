#!/usr/bin/python
import re
import json
from flask import Flask, request, escape

app = Flask(__name__)

@app.route("/parse/<filename>")
def parse1Name(filename):
    patt = re.compile("(?P<filename>(?P<vendor>[a-zA-Z0-9]+)_?"+
        "(?P<assay>A\d{3})?_?(?P<year>\d{4})?(?P<month>\d{2})"+
        "(?P<day>\d{2})?.*.(?P<filetype>\w{3}))")
    parsed = re.search(patt, filename).groupdict()
    return json.dumps(parsed)

@app.route("/")
def root():
    return "Welcome!"
