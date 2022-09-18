class file_open :
    def require_list(self):
      text_origin = open("test_article\orig.txt",encoding='utf-8')
      str_1 =text_origin.read()
      text_s = open("test_article\orig_0.8_add.txt",encoding='utf-8')
      str_2 = text_s.read()
      list_=[str_1,str_2]

      return list_
     




