#!/usr/bin/python
# -*- coding: UTF-8 -*-

#datemining guide chapter3

# 修正的余弦相似度(删除用户主观评分的影响)
from math import sqrt
users3 = {"David": {"Imagine Dragons": 3, "Daft Punk": 5,
"Lorde": 4, "Fall Out Boy": 1},
"Matt": {"Imagine Dragons": 3, "Daft Punk": 4,
"Lorde": 4, "Fall Out Boy": 1},
"Ben": {"Kacey Musgraves": 4, "Imagine Dragons": 3,
"Lorde": 3, "Fall Out Boy": 1},
"Chris": {"Kacey Musgraves": 4, "Imagine Dragons": 4,
"Daft Punk": 4, "Lorde": 3, "Fall Out Boy": 1},
"Tori": {"Kacey Musgraves": 5, "Imagine Dragons": 4,
"Daft Punk": 5, "Fall Out Boy": 3}}


def computeSimilarity(band1,band2,userRatings):#用来得到物品与物品之间的相似度
    averages = {}
    for (key,ratings) in userRatings.items(): #求用户对所有物品评分的平均分
        averages[key] = (float(sum(ratings.values()))/len(ratings.values())) #key为用户名

    print userRatings.items()

    num = 0 # 分子
    dem1 = 0 #分母的第一部分
    dem2 = 0
    for (user,ratings) in userRatings.items():
        if band1 in ratings and band2 in ratings: #代表某一个用户评价了这边两个物品
            avg = averages[user]#得到这一用户的平均分
            num+=(ratings[band1]-avg)*(ratings[band2]-avg) #得到x*y
            dem1+=pow(ratings[band1]-avg,2)
            dem2+=pow(ratings[band2]-avg,2)
    return num/(sqrt(dem1)*sqrt(dem2))

print computeSimilarity('Kacey Musgraves','Fall Out Boy',users3)

print users3['David']
print type(users3['David'])
'''
预测某一用户对某一物品的打分
'''

# 1. 修正用户对物品的评分，使之落到[-1,1]这个区间内
def normalize(userRatings):
   min = 1
   max = 5
   user_nor_score = {}
   for user in userRatings:
      band_nor_score = {}
      print user+ '原始评分：'+str(userRatings[user])
      for band in userRatings[user]:
             nor_score = float((2*userRatings[user][band]-(max+min)))/(max-min) #标准化后的分数
             band_nor_score[band] = nor_score
      print user + '评分正则化后: '+ str(band_nor_score)
      user_nor_score[user] = band_nor_score
   return user_nor_score

print normalize(users3)
'''
def restoreStar(userRatings): #将正则化后的分数还原
    min = 1
    max = 5
    user_ini_score = {}
    for user in userRatings:
        band_ini_score = {}
        print user + '原始评分：' + str(userRatings[user])
        for band in userRatings[user]:
            ini_score = float((2 * userRatings[user][band] - (max + min))) / (max - min)  # 标准化后的分数
            band_ini_score[band] = nor_score
        print user + '评分正则化后: ' + str(band_ini_score)
        user_ini_score[user] = band_ini_score
    return user_ini_score
'''

'''
基于修正后的余弦相似度的用户预测分数
'''
# band这个乐队从来没有出现在user的评分列表中
def predictScore(user,band,userRatings): #基于某一组用户对乐队的评分来预测某一用户对目标乐队的评分
   pre_score = 0.0 #定义为float类型
   num = 0.0 #分子
   dem = 0.0 #分母
   max = 5
   min = 1
   user_nor_score = normalize(userRatings) # 得到每一用户对乐队正则化的评分
   if not band in userRatings[user]: #代表此用户从来没有给这个乐队评过分
      for  band1 in userRatings[user]:#如果没有评价过此乐队
          num += user_nor_score[user][band1]*computeSimilarity(band,band1,userRatings)
          dem += abs(computeSimilarity(band,band1,userRatings))
      pre_score = 0.5*(num/dem+1)*(max-min)+min
   else:
       pre_score = userRatings[user][band]
   return pre_score

print predictScore('David','Kacey Musgraves',users3)
print predictScore('David','Daft Punk',users3)


'''
1. 计算
'''
def simpleSlopeOne(user,band,userRatings):#返回的还是用户对某一乐队的评分
    card = 0 #用来计算评价过band1和band2的用户数 

