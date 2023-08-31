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
        self.xsrf_token
        name = self.get_argument('name')
        print('User name is : ', name)
        self.set_signed_cookie('user', name)
        self.redirect('/')
settings = {
    'cookie_secret': '053d1bd0-6af1-4d81-b195-e72f9a133160',
    'login_url': '/login',
    'xsrf_cookies': True,
}
def make_app():
    return tornado.web.Application([
        (r'/', MainHandler),
        (r'/login', LoginHandler),
    ], **settings)
    '''
    # DNS Rebinding - 限制访问IP地址
    return tornado.web.Application([
        (tornado.routing.HostMatches(r'(localhost|127\.0\.0\.1)'), [
            (r'/', MainHandler),
            (r'/login', LoginHandler),
        ])], **settings)
    '''
async def main():
    app = make_app()
    app.listen(80)
    await asyncio.Event().wait()
if __name__ == '__main__':
    asyncio.run(main())