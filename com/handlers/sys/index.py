import tornado
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html', title='Index Page', items=['Home', 'Python', 'Java', 'C'])
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