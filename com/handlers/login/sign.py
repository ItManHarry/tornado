import tornado
from com.handlers.base import BaseHandler
class LoginHandler(BaseHandler):
    def get(self):
        self.write('''
            <html>
                <body>
                    <form action = '/login' method = 'post'>
                    <input type='hidden' name='_xsrf' value='{}'> 
                    Name : <input type = 'text' name='name'><br>
                    <input type='submit' value='Sign In'>
                    </form>
                </body>
            </html>
        '''.format(tornado.escape.xhtml_escape(self.xsrf_token)))
    def post(self):
        user = self.get_argument('name')
        # print(user)
        self.set_signed_cookie('user', user)
        # self.redirect('/')
        self.redirect(self.reverse_url('main'))