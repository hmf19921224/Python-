
import urllib.request


html = urllib.request.urlopen('http://www.baidu.com').read().decode('utf-8')
# print(html)
'''
这一行我们使用了urllib.request模块中的urlopen方法，相当于发送了一个Request给服务器，
它会返回一个Response对象，然后我们使用了read方法将内容读出来，可惜它是bytes类型的数据，
于是我们给它解码，即decode，就变成了编码后的字符串。
'''

html1 = urllib.request.urlopen('http://httpbin.org/headers').read().decode('utf-8')

# print(html1)


from urllib.request import ProxyHandler, build_opener

proxy_handler = ProxyHandler({
    'http': '61.135.217.7:80',
})
opener = build_opener(proxy_handler)
response = opener.open('http://www.baidu.com')
# print(response.read().decode('utf-8'))


#正则表达式
import  re
str = '我不是123快乐'

pattern = re.compile('123')

matchs =  pattern.match(str)

print(matchs)
import urllib.request


html = urllib.request.urlopen('http://www.baidu.com').read().decode('utf-8')
# print(html)
'''
这一行我们使用了urllib.request模块中的urlopen方法，相当于发送了一个Request给服务器，
它会返回一个Response对象，然后我们使用了read方法将内容读出来，可惜它是bytes类型的数据，
于是我们给它解码，即decode，就变成了编码后的字符串。
'''

html1 = urllib.request.urlopen('http://httpbin.org/headers').read().decode('utf-8')

# print(html1)


from urllib.request import ProxyHandler, build_opener

proxy_handler = ProxyHandler({
    'http': '61.135.217.7:80',
})
opener = build_opener(proxy_handler)
response = opener.open('http://www.baidu.com')
# print(response.read().decode('utf-8'))


#正则表达式
import  re

str = '我125不是快乐'
# patterns = re.compile('123')
# matchs = patterns.search(patterns,str,re.M)

matchObj = re.search( r'125', str, re.M|re.I)
print(matchObj)
print(matchObj.group())


# print(re_telephone)
print(matchs)
if matchs:
    # 使用Match获得分组信息
    print(matchs.group())


pattern = re.compile(r'hello')

# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
match = pattern.match('hello world!')

if match:
    # 使用Match获得分组信息
    print(match.group())

