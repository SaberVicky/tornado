#-*- coding:utf-8 -*-
import tornado.ioloop
import tornado.web
import json
import MySQLdb
import os

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("youjin/index.html")
#    	a = self.get_argument('content', None)
#    	b = self.get_argument('answer', None)
#        
#    	result = {
#            "data" : "data",
#    		"code" : 200,
#    		"msg" : "success",
#    		"a" : a,
#    		"b" : b,
#            "ret" : 1
#    	}
#        
#        db = MySQLdb.connect("127.0.0.1","root","","test")
#        cursor = db.cursor();
#        sql = "INSERT INTO T_Jokes(content, answer) VALUES ('%s', '%s')"  % (a, b)
#        cursor.execute(sql)
#        db.commit()
#
#
#        self.write(json.dumps(result))

class JqueryHanlder(tornado.web.RequestHandler):
    def get(self):
        self.render("youjin/juqery.html")

class TestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("啦啦啦")

class RegisterHandler(tornado.web.RequestHandler):
    def post(self):
        a = self.get_argument('user_account', None)
        b = self.get_argument('user_password', None)

        db = MySQLdb.connect("127.0.0.1","root","","test")
        cursor = db.cursor();
        sql1 = "select count(*) from T_User where user_account = '%s'" % a
        cursor.execute(sql1)
        count = cursor.fetchone()[0]
        if count > 0:
            result = {
            "ret" : 0,
            "count" : count,
            "msg" : "该账号已经被注册"
            }
        else:
            result = {
            "ret" : 1,
            "count" : count,
            "msg" : "注册成功"
            }
            sql = "INSERT INTO T_User(user_account, user_password) VALUES ('%s', '%s')"  % (a, b)
            cursor.execute(sql)

        db.commit()
        db.close()  
        self.write(json.dumps(result))
        

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static")
}

application = tornado.web.Application([
    (r"/register", RegisterHandler),
    (r"/rz", TestHandler),
    (r"/", MainHandler),
    (r"/jquery", JqueryHanlder),
    (r"/(apple-touch-icon\.png)", tornado.web.StaticFileHandler, dict(path=settings['static_path'])),
], **settings)


if __name__ == "__main__":
    application.listen(80)
    print "开启服务器"
    tornado.ioloop.IOLoop.instance().start()
