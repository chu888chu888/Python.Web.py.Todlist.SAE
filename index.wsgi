#!/usr/bin/env python
# coding: utf-8
import os
import sae
from config.url import urls
import web

app = web.application(urls, globals()).wsgifunc()
application = sae.create_wsgi_app(app)
