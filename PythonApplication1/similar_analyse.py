import jieba
import math


class similar_analyse :
   def analyse(s1,s2):
    stop = open("extra_dict/stop_words.txt",encoding='utf-8')
    stopword = stop.read().split("\n") #停用词
    s1_cut = [i for i in jieba.cut(s1) if i not in stopword and i!=' 'and i!='\n'] #把S1用jieba裁剪并放入到list中，并取消停用词
    s2_cut = [i for i in jieba.cut(s2) if i not in stopword and i!=' 'and i!='\n']

    word_set = set(s1_cut).union(set(s2_cut)) #把list1和list2取并集，放到集合中

    word_dict = dict() #创建空字典
    i = 0
    for word in word_set: #遍历集合
        word_dict[word] = i #把集合中的每个词按顺序放入字典，以1 2 3 4...排序
        i += 1

    s1_cut_code = [word_dict[word]-word_dict[word] for word in word_set] #把s1里的词在上述字典里的映射值，按照s1列表的排序放到一个新列表里，并将它们归0

    for word in s1_cut:
        s1_cut_code[word_dict[word]]+=1 #s1词频

    s2_cut_code = [word_dict[word]-word_dict[word] for word in word_set] #把s2里的词在上述字典里的映射值，按照s1列表的排序放到一个新列表里，并将它们归0

    for word in s2_cut:
        s2_cut_code[word_dict[word]]+=1 #s2词频


    # 计算余弦相似度
    sum = 0
    sq1 = 0
    sq2 = 0

    for i in range(len(s1_cut_code)):
        sum += s1_cut_code[i] * s2_cut_code[i]
        sq1 += pow(s1_cut_code[i], 2)
        sq2 += pow(s2_cut_code[i], 2)

    try:
        result = round(float(sum) / (math.sqrt(sq1) * math.sqrt(sq2)), 2)
    except ZeroDivisionError:
        result = 0.0
    return result

