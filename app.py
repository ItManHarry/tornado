import asyncio
import tornado
from settings import settings
from urls import urls
def make_app():
    return tornado.web.Application(urls, **settings)
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