import tornado
from com.handlers.base import BaseHandler
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