import tornado
from com.handlers.base import BaseHandler
class MainHandler(BaseHandler):
    def get(self):
        c_u = self.get_current_user()
        # print('Current user is >>>>>> ', c_u)
        if not self.current_user:
            # self.redirect('/login')
            self.redirect(self.reverse_url('login'))
            return
        name = tornado.escape.xhtml_escape(self.current_user)
        # print('Index user name is : ', name)
        self.write('Hello '+name+'!!!')
    # @tornado.web.authenticated
    # def get(self):
    #     name = tornado.escape.xhtml_escape(self.current_user)
    #     self.write('Hello {}!!!'.format(name))