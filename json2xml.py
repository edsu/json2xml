#!/usr/bin/env python

"""
Call json2xml from the command line:

    % ./json2xml.py tweet.json tweet | xmllint --format - > tweet.xml

or from a program:

    from json2xml import json2xml
    print json2xml("tweet.json", tag_name="tweet")

"""

import sys
import json
from xml.etree.ElementTree import TreeBuilder, tostring

def json2xml(filename, tag_name="data"):
    """pass in the path to a JSON filename, and an optional tag 
    name for the a root element, and get back some XML for the JSON.
    """
    json_data = json.loads(open(filename).read())
    builder = data2xml(json_data, tag_name=tag_name)
    doc = builder.close()
    return tostring(doc, encoding='utf-8')

def data2xml(data, tag_name="data", builder=None):
    """pass in a python datastructure and get back a etree TreeBuilder
    """
    if builder == None:
        builder = TreeBuilder()
    t = type(data)
    if t in (str, unicode, int, float, bool):
        builder.start(tag_name, {})
        builder.data(unicode(data))
        builder.end(tag_name)
    elif t == list:
        for value in data:
            data2xml(value, tag_name=tag_name, builder=builder)
    elif t == dict:
        builder.start(tag_name, {})
        for key, value in data.items():
            data2xml(value, tag_name=key, builder=builder)
        builder.end(tag_name)
    return builder

if __name__ == "__main__":
    filename = sys.argv[1]
    tag_name = len(sys.argv) > 1 ? sys.argv[2] : "data"
    print json2xml(filename, tag_name=tag_name)
