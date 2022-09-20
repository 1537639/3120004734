class file_open :
    def require_list(self,str):
      
      text_s = open(str, encoding='utf-8') #打开检测文档
      str_2 = text_s.read() #字符串化
      text_s.close()
      return str_2
     




