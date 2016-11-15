#-*- coding:utf-8 -*-
import tornado.ioloop
import tornado.web
import json
import os

class MainHandler(tornado.web.RequestHandler):
    def get(self):
    	a = self.get_argument('content', None)
    	b = self.get_argument('answer', None)
        
    	result = {
            "data" : "data",
    		"code" : 200,
    		"msg" : "success",
    		"a" : a,
    		"b" : b,
            "ret" : 1
    	}



#        self.write(json.dumps(result))
self.write("欢迎访问有金水产，该网站正在建设中，请稍后访问。。。")


class TestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("123/main.html") 

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static")
}

application = tornado.web.Application([
    (r"/123", TestHandler),
    (r"/", MainHandler),
    (r"/(apple-touch-icon\.png)", tornado.web.StaticFileHandler, dict(path=settings['static_path'])),
], **settings)


if __name__ == "__main__":
    application.listen(80)
    print "开启服务器"
    tornado.ioloop.IOLoop.instance().start()
