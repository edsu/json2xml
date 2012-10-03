json2xml
========

A simplistic JSON to XML converter, created mainly as a way to kill time
one evening after a tweet from @pbinkley.

Example
-------

From the command line:

    % ./json2xml.py tweet.json | xmllint --format - > tweet.xml

Or from your program:

```python

from json2xml import json2xml

print json2xml("tweet.json", tag_name="tweet")
``` 

