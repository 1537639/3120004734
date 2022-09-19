import os
import similar_analyse
import open_file
import answer

path=os.path .abspath('')
filelist=os.listdir("test_article/") #存放待检测文章的文件
fo = open_file.file_open()
article_dict = dict();
text_origin = open("origin_article\orig.txt",encoding='utf-8') #打开存放原文文档的文件
str_1 =text_origin.read() #字符串化
list_=[" "," "]
list_[0]=str_1

for file in filelist : #遍历test_article文件夹
    list_[1]=fo.require_list(file)
    sm =similar_analyse.similar_analyse.analyse(list_[0],list_[1]) #检测两篇文章的字符串相似度
    if sm >= 0.3: #如果相似度大于0.3加入抄袭文章列表
        article_dict[ path + '\\' +'test_article\\'+ file ] = sm
    print(path + '\\'+ 'test_article\\' + file +' 相似度：'+ str(sm))

ans=answer.answer()
ans.answer(article_dict,path) #输出答案文件
print('原文路径：')
print(path + '\origin_article\orig.txt')
print('抄袭文章：')
print(article_dict)
print('答案文件：')
print(path+'\answer\log.txt')