import tornado
class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render_string('home.html', title='Home Page', items=['Home', 'Python', 'Java', 'C'])
