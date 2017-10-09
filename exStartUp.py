#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Program name: 深度学习开学任务
    Author: Yuanzizi
    Github: https://github.com/Yuanzizi/
    Edition：v 0.1
    Edit date: 2017.10.09
    Descrition:
        ------------------------------------------------
        统计这篇 happiness_seg.txt 出现频率最高的前 10 个「二元词组」，
        并输出它们的频率
        -------------------------------------------------
    Log:
        V0.1 2017-10-09
        + 安装numpy ok
        + 确定词组数据结构 ok
        + 编写文件读取函数 ok
        + 编写词组频率统计函数 ok

"""
import numpy as np
from collections import Counter
# print(np.version.version)

def initial_list(input_file_path='', str_split=''):
    """从文件中读取词组 到 list 列表中，并且去重和排序，并返回

    Args:
        input_file_path: 文件的路径，词组按照空格分隔
        str_split: key:values  的分割字符，缺省是空格.

        Returns:
        返回一个list 类型

        Raises:
        FileNotFoundError: 文件没找到，给出提示
        """
    puntuation_list = ['，','。','！','“','”','；','？','、','《','》','【','】',
    '（','）','/r','/r/n','/n',',','.','?',';','．', '／', '：', '＞', '＠', '［', '＿', '｛', '}','～','＄', '％', '－','\'','-','·','—','―','‘','’','…']
    wordlist = [] #词组列表
    list2word = [] #二元词组列表
    wordFrequency = {} # 词频字典
    try:
        with open('text_initial.txt','w',encoding='utf-8') as w:
            with open(input_file_path, encoding='utf-8') as f1:
                for line in f1:
                    for word in line.split():
                        if word not in puntuation_list:
                            wordlist.append(word)
                            w.write(word+" ")
            # w.flush()
            # w.seek(0,0)
        wordlist.reverse()
        while len(wordlist) > 1:
            k1 = wordlist.pop()
            k2 = wordlist.pop()
            list2word.append(k1+" "+k2)
            wordlist.append(k2)
        # print(list2word)

        # for w in list2word:
        #     if list2word.count(w) > 1:
        #         wordFrequency[w] = list2word.count(w)
        #         print(w,list2word)
        wordFrequency = Counter(list2word)
        with open("result.txt", 'w', encoding='utf-8') as r:
            for k,v in wordFrequency.items():
                line = str(k) + ":" + str(v)
                r.writelines(line)
        wordFrequency = sorted(wordFrequency.items(),key=lambda item:item[1],reverse=True)
        for i in range(10):
            print(wordFrequency[i])
    except FileNotFoundError:
        print("文件无法找到，请确认路径和文件名正确.......")

    # return db
if __name__ == '__main__':

    initial_list("happiness_seg.txt")
