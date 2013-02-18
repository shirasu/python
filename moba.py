# coding: UTF-8
import urllib, urllib2, cookielib, re

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))

header = {
    "Accept-Language" : "ja-JP : en-US",
    "Accept" : "application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5",
    "Accept-Charset" : "utf-8 : iso-8859-1 : utf-16 : *;q=0.7",
    "User-Agent" : "Mozilla/5.0 (Linux; U; Android 2.3.3; ja-jp; SonyEricssonIS11S Build/3.0.1.C.1.10) AppleWebKit/533.1 (KHTML : like Gecko) Version/4.0 Mobile Safari/533.1"
}

data = {
    "_CODE" : "あ",
    "_from" : "lg",
    "login_cb" : "/_lg",
    "new" : "",
    "login_id" : "",
    "login_pw" : "",
    "login" : "ログイン"
}

res = opener.open(urllib2.Request("https://ssl.sp.mbga.jp/_lg", urllib.urlencode(data), header))
info = res.info()
readd = res.read()
xloguser = info["x-log-user"]

m = re.match("^m([0-9]+)", xloguser)
if m == None :
    exit("Login failed")

print "ID:" + m.group(1)
print res
print info
#print readd

res = opener.open(urllib2.Request("http://sp.pf.mbga.jp/12008305/?guid=ON&url=http%3A%2F%2F125.6.169.35%2Fidolmaster%2Fmypage", None, header))
info = res.info()
readd = res.read()

nnn = readd.find("ｽﾀﾐﾅ:</span>")
print nnn
print readd[nnn+20:nnn+23]



#print readd
