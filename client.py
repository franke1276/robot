#!/usr/bin/env python
import tornado.httpclient
import urllib
http_client = tornado.httpclient.HTTPClient()

#d = { 'cmd': "sa", 'data': str([-0.025917028664872863, 0.10879597417855738, -0.57406544281527, -0.29271746183250025, 0.1415089132064551, -0.2933808456289866])}
d = { 'cmd': "sb", 'data': "b"}
response = http_client.fetch(tornado.httpclient.HTTPRequest(url="http://pi:9999/cmd",method="PUT", headers={"Content-Type": "application/x-www-form-urlencoded"},body=urllib.urlencode(d)))
print(str(response.body))
http_client.close()
