import boto
import uuid
from boto.s3.key import Key
from boto.s3.connection import S3Connection
import sys
import alchemyapi
import hashlib


class article2db:
    def __init__(self):
        s3 = S3Connection('AKIAJSNE54BGVCVJ3RXA','n0bH9+8t1JVmphanLicAtTfWD5Huy6D1tTGWjOm+')
        self.bucket=s3.get_bucket('newslist') 
        self.alchemy = alchemyapi.AlchemyAPI()
            
    def store_key_value(self,key,value):
        possiblekey = self.bucket.get_key(key)
        if possiblekey is None:
            k = Key(self.bucket)
            k.key = key
            k.set_contents_from_string(value)
            return True
        else:
            return False
    
    def exist_url(self,url):
        hashnum = hashlib.md5(url).hexdigest()
        possiblekey = self.bucket.get_key('%s_titl' % hashnum)
        if possiblekey is None:
            return False
        else:
            return True
    
    def exist_hashnum(self,hashnum):
        possiblekey = self.bucket.get_key('%s_titl' % hashnum)
        if (possiblekey) is None:
            return False
        else:
            return True
        
    
    def put_url(self, url):
        keywords = self.alchemy.keywords("url", url)
        text = self.alchemy.text("url",url)
        title = self.alchemy.title("url",url)
        author = self.alchemy.author("url",url)
        if keywords['status'] != 'ERROR':
            hashnum = hashlib.md5(url).hexdigest()
            
            self.store_key_value('%s_titl' % hashnum, title['title'])
            self.store_key_value('%s_text' % hashnum, text['text'])
            self.store_key_value('%s_auth' % hashnum, author['author'])
            self.store_key_value('%s_urll' % hashnum, url)
            
            res = ""
            for item in keywords['keywords']:
                kws = item ['text']
                res = res + kws +" "
            res = res[:-1]
            self.store_key_value('%s_keyw' % hashnum, res)
            return True
        else:
            return False

    def list_all_key(self):
        # self.bucket.list()
        keylist = [] 
        for key in self.bucket.list():
            if key.name[-4:] == 'urll':
                keylist.append(key.name[:-5])
        return keylist
                # keylist.append(key)
    
    def list_all_news(self):
        keylist = self.list_all_key()
        for key in keylist:
            result = self.retrieve_news(key)
            print result['title']+' '+result['author']

    def retrieve_news(self,key): #key is the 128bit code
        url = self.retrieve_key(key+'_urll')
        title = self.retrieve_key(key+'_titl')
        author = self.retrieve_key(key+'_auth')
        text = self.retrieve_key(key+'_text')
        keywords = self.retrieve_key(key+'_keyw')
        
        return {'url':url, 'title':title ,'author':author,'text':text,'keywords':keywords}
        
    def retrieve_key(self,key): #key is the 128bit+4bytes
        k = Key(self.bucket,key)
        # k.key = key
        return k.get_contents_as_string()



def main():
    # parse command line options
    art = article2db()
    art.list_all_news()
    # f=open('cnn_news.txt','r')
    # temp = f.read().splitlines()
    # num = 0
    # while (num<10):
    #     url = temp[num]
    #     num = num +1
    #     print url
    #     art.put_url(url)


if __name__ == "__main__":
    main()




#
# f=open('cnn_news.txt','r')
# temp = f.read().splitlines()
# num=0
# while (num<1):
#     url = temp[num]
#     num = num +1
#     print url
#     # url = "http://cnn.com/2015/04/06/opinions/wang-china-women-detained/index.html"
#     # url = 'http://edition.cnn.com/2015/04/18/africa/south-africa-xenophobia-explainer/index.html'
#     keywords = inst.keywords("url", url)
#     text = inst.text("url",url)
#     title = inst.title("url",url)
#     author = inst.author("url",url)
#     print keywords
#     if keywords['status'] == 'ERROR':
#         continue
#     else:
#         keywords = keywords['keywords']
#         text = text['text']
#         title = title['title']
#         author = author['author']
#     res = ""
#     for item in keywords:
#         kws = item ['text']
#         kws_list = kws.split(" ")
#         for i in kws_list:
#             res = res+i+" "
#     print res
#     item=NewsList(theme=title,text=text,author=author,weblinks=url,keywords=res)
#     item.save()

