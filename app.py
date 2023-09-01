import asyncio
import tornado

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_signed_cookie('user')
class MainHandler(BaseHandler):
    # def get(self):
    #     c_u = self.get_current_user()
    #     print('Current user is >>>>>> ', c_u)
    #     if not self.current_user:
    #         self.redirect('/login')
    #         return
    #     name = tornado.escape.xhtml_escape(self.current_user)
    #     print('Index user name is : ', name)
    #     self.write('Hello '+name+'!!!')
    @tornado.web.authenticated
    def get(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        self.write('Hello {}!!!'.format(name))
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
        name = self.get_argument('name')
        print('User name is : ', name, 'OK')
        self.set_signed_cookie('user', name)
        self.redirect('/')
class JsonHandler(BaseHandler):
    def initialize(self, email):
        print('Execute the initialize method ...')
        self.email = email

    def prepare(self):
        print('Execute the prepare method ...')
    def get(self):
        print('Execute the get method ...')
        params = self.request.body
        if params:
            print('Parameters : ', params)
        else:
            print('Empty parameters!')
        self.write({'name': 'Harry', 'age': 40, 'email': self.email})
        self.set_header('Content-Type', 'application/json')
    def on_finish(self):
        print('Execute the finish method ...')
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html', title='Index Page', items=['Home', 'Python', 'Java', 'C'])
class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render_string('home.html', title='Home Page', items=['Home', 'Python', 'Java', 'C'])
from settings import settings
def make_app():
    return tornado.web.Application([
        (r'/', MainHandler),
        (r'/index', IndexHandler),
        (r'/home', HomeHandler),
        (r'/login', LoginHandler),
        (r'/json', JsonHandler, dict(email='guoqian.cheng@hyundai-di.com')),
        (r'/(images/bg/1\.jpg)', tornado.web.StaticFileHandler, dict(path=settings['static_path'])),
    ], **settings)
    '''
    # DNS Rebinding - 限制访问IP地址
    return tornado.web.Application([
        (tornado.routing.HostMatches(r'(localhost|127\.0\.0\.1)'), [
            (r'/', MainHandler),
            (r'/login', LoginHandler),
        ])], **settings)
    '''
'''
页面导入静态文件
<html>
   <head>
      <title>FriendFeed - {{ _("Home") }}</title>
   </head>
   <body>
     <div><img src="{{ static_url("images/logo.png") }}"/></div>
   </body>
 </html>
'''

async def main():
    app = make_app()
    app.listen(80)
    await asyncio.Event().wait()
if __name__ == '__main__':
    asyncio.run(main())