import os
import getopt
import sys
import similar_analyse
import open_file
import answer


origin_path=sys.argv[1]
test_path=sys.argv[2]
answer_path=sys.argv[3] #传入三个路径参数
fo = open_file.file_open()
list_=[" "," "]
list_[0]=fo.require_list(origin_path)
list_[1]=fo.require_list(test_path) #打开两个文件
sm =similar_analyse.similar_analyse.analyse(list_[0],list_[1]) #检测两篇文章的字符串相似度
print(test_path +' 相似度：'+ str(sm))

ans=answer.answer()
ans.answer(sm,answer_path) #输出答案文件
print('原文路径：')
print(origin_path)
print('文章相似度：')
print(sm)
print('答案文件：')
print(answer_path)

