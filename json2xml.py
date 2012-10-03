import sys
import json
from xml.etree.ElementTree import TreeBuilder, tostring

def json2xml(filename, tag_name="data"):
    json_data = json.loads(open(filename).read())
    builder = data2xml(json_data, tag_name=tag_name)
    doc = builder.close()
    return tostring(doc)

def data2xml(data, tag_name="data", builder=None):
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
