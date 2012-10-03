json2xml
========

A simplistic JSON to XML converter, created mainly as a way to kill time
one evening after a
[tweet](https://twitter.com/pabinkley/status/253279453738835969)
from @pbinkley. Yes, you are entitled to ask why I would ever want to 
convert JSON to XML. No, I'm not going to provide an answer :-)

Example
-------

From the command line:

    % ./json2xml.py tweet.json | xmllint --format - > tweet.xml

Or from your program:

```python

from json2xml import json2xml

print json2xml("tweet.json", tag_name="tweet")
``` 

Or if you have a python data structure created by something like json.loads
and you would like xml for it, get a TreeBuilder for it:

```python

from json2xml import data2builder
from xml.etree.ElementTree import tostring

data = {"foo": "bar", "baz": [1, 2, 3]}
builder = data2builder(data, tag_name="data")
doc = builder.close()
print tostring(doc)
```
