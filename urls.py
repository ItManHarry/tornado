import tornado
from settings import settings
from com.handlers.login.sign import LoginHandler
from com.handlers.sys.main import MainHandler
from com.handlers.test.json import JsonHandler
from com.handlers.sys.index import IndexHandler
from com.handlers.sys.home import HomeHandler
urls = [
    tornado.web.URLSpec(r'/', MainHandler, name='main'),
    (r'/index/', IndexHandler),
    (r'/home', HomeHandler),
    tornado.web.URLSpec(r'/login', LoginHandler, name='login'),
    (r'/json', JsonHandler, dict(email='guoqian.cheng@hyundai-di.com')),
    (r'/(images/bg/1\.jpg)', tornado.web.StaticFileHandler, dict(path=settings['static_path'])),
]