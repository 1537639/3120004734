import datetime

class answer:
    def answer(self,article_dict,path):
      f = open('answer\log.txt','a')
      print('原文路径：',file=f)
      print(path + '\origin_article\orig.txt',file=f)
      print('抄袭文章：',file=f)
      print(article_dict,file=f)
      time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
      print('检测时间：'+time ,file=f)
    


