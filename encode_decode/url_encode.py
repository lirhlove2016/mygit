
from urllib import parse
from urllib import request

url = 'http://www.baidu.com/s?'
dict1 ={'wd': '百度翻译'}
url_data = parse.urlencode(dict1) #unlencode()将字典{k1:v1,k2:v2}转化为k1=v1&k2=v2
print('编码url  ',url_data)             #url_data：wd=%E7%99%BE%E5%BA%A6%E7%BF%BB%E8%AF%91
data = request.urlopen((url+url_data)).read() #读取url响应结果
data = data.decode('utf-8') #将响应结果用utf8编码
print('响应结果用utf8编码 ',data)
url_org = parse.unquote(url_data) #解码url
print('解码url----',url_org)              #url_org：wd=百度翻译



#quote( ) 和 unquote( )
str1 = 'http://wwww.baidu.com/asg/北京&%上海&token'
str2 = parse.quote(str1)   #quote()将字符串进行编码
print('字符串进行编码 ',str2)                #str2=haha%E5%93%88%E5%93%88
str3 = parse.unquote(str2) #解码字符串
print('字符串进行编码 ',str3)                #str3=haha哈哈
