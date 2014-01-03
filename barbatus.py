import tornado.ioloop
import tornado.web

class StaticHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(self.request.uri[1:])

class TemplateHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates"+self.request.uri)

application = tornado.web.Application([
    (r"/static/.*",StaticHandler),
    (r"/.*",TemplateHandler)],debug=True)

application.listen(8888)
tornado.ioloop.IOLoop.instance().start()