import datetime

class answer:
    def answer(self,sm,path):
      try:
        f = open(path,'w')
        print(sm,file=f)
      except Exception:
        print("无法写入"+path)  
