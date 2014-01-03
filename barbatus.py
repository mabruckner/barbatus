import tornado.ioloop
import tornado.web
import User

games = []
users = []


class StaticHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(self.request.uri[1:])

class TemplateHandler(tornado.web.RequestHandler):
    def get(self):
        global users
        user = None
        if not self.get_secure_cookie("user"):
            user = User.User()
            self.set_secure_cookie("user",user.identifier)
            users.append(user)
        else:
            identifier = self.get_secure_cookie("user")
            for u in users:
                if u.identifier == identifier:
                    user=u
                    break
            if user == None:
                user = User.User()
                self.set_secure_cookie("user",user.identifier)
                users.append(user)
        print(users)
        self.render("templates"+self.request.uri)

application = tornado.web.Application([
    (r"/static/.*",StaticHandler),
    (r"/.*",TemplateHandler)],debug=True,cookie_secret = "WE NEED A COOKIE SECRET KEY FOR THIS TO WORK")

application.listen(8888)
tornado.ioloop.IOLoop.instance().start()