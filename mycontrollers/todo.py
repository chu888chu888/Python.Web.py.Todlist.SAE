#!/usr/bin/env python
# coding: utf-8
import web

class mytest:
    def GET(self):
            return "<b><h1>我扩展测试一下</h1><b>"
class Upload:
    def GET(self):
        return """<html><head></head><body>
<form method="POST" enctype="multipart/form-data" action="">
<input type="file" name="myfile" />
<br/>
<input type="submit" />
</form>
</body></html>"""

    def POST(self):
        x = web.input(myfile={})
        web.debug(x['myfile'].filename) # 这里是文件名
        web.debug(x['myfile'].value) # 这里是文件内容
        web.debug(x['myfile'].file.read()) # 或者使用一个文件对象
        print x['myfile'].filename
        print x['myfile'].value
        print x['myfile'].file.read()
        raise web.seeother('/todo/upload')

