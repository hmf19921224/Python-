from  urllib import request
import ssl

context = ssl._create_unverified_context()

with request.urlopen('https://api.douban.com/v2/book/2129650',context=context) as f:

    data = f.read()

    print('status:', f.status, f.reason)

    for k,v in f.getheaders():

        print('key %s values %s' %(k,v))

    print('data:',data.decode('utf-8'))
