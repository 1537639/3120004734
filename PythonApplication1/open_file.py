class file_open :
    def require_list(self,str):
      try:
        text_s = open(str, encoding='utf-8') #打开文档
      except FileNotFoundError:
        print("无法打开"+str)
        str_=''
      str_= text_s.read() #字符串化
      text_s.close()
      return str_
     




