import tornado.ioloop
import tornado.web

class StaticHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(self.request.uri[1:])

class TemplateHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates"+self.request.uri)

class MoveHandler(tornado.web.RequestHandler):
    def post(self):
        #import ipdb;ipdb.set_trace()
        self.write(str(self.request.arguments))

handlers = [
        (r"/static/.*", StaticHandler),
        (r"/submit/move", MoveHandler),
        (r"/.*", TemplateHandler)
    ]

application = tornado.web.Application(handlers, debug=True)

application.listen(8888)
tornado.ioloop.IOLoop.instance().start()
