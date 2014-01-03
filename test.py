import tornado.ioloop
import tornado.web
import tictactoe as t3
import json
game = t3.TicTacToe()
for player in ["Bob","Bill","Jeb"]:
	game.add_player(player)
game.begin()

class RestHandler(tornado.web.RequestHandler):
    def get(self):
        global game
        self.write(str(self.__dict__))
        print(str(self.get_arguments("move")))
        print(str(self.get_arguments("player")))
        self.write("\n");
        game.execute(self.get_arguments("player")[0],json.loads(self.get_arguments("move")[0]))
        print(game.get_state(None))
        print(game.score())
        #self.write(json.dumps(game.getstate(None))+"\n")
class StaticHandler(tornado.web.RequestHandler):
    def get(self):
        #self.write(str(self.__dict__))
        #print(args)
        self.render(self.request.uri[8:])
application = tornado.web.Application([
    (r"/static/.*",StaticHandler),
    (r"/rest/.*",RestHandler)])

application.listen(8888)
tornado.ioloop.IOLoop.instance().start()
