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

from types import *
from xml.etree.ElementTree import TreeBuilder, tostring

def json2xml(filename, tag_name="data"):
    """pass in the path to a JSON filename, and an optional tag 
    name for the a root element, and get back some XML for the JSON.
    """
    json_data = json.loads(open(filename).read())
    builder = data2builder(json_data, tag_name=tag_name)
    doc = builder.close()
    return tostring(doc, encoding='utf-8')

def data2builder(data, tag_name="data", builder=None):
    """pass in a python datastructure and get back a etree TreeBuilder
    """
    if builder == None:
        builder = TreeBuilder()
    t = type(data)
    if t in (StringType, UnicodeType, IntType, FloatType, BooleanType, LongType):
        builder.start(tag_name, {})
        builder.data(unicode(data))
        builder.end(tag_name)
    elif t == ListType:
        for value in data:
            data2builder(value, tag_name=tag_name, builder=builder)
    elif t == DictionaryType:
        builder.start(tag_name, {})
        for key, value in data.items():
            data2builder(value, tag_name=key, builder=builder)
        builder.end(tag_name)
    elif t == NoneType:
        builder.start(tag_name, {})
        builder.end(tag_name)
    else: 
        raise Exception("uhoh I can't handle type %s" % t)
    return builder

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "usage: ./json2xml.py <json_filename> [tagname]"
        sys.exit(1)
    filename = sys.argv[1]
    tag_name = sys.argv[2] if len(sys.argv) > 2 else "data"
    print json2xml(filename, tag_name=tag_name)
