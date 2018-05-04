#!/usr/bin/python
# -*- coding: UTF-8 -*-

#datemining guide chapter2

users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bill":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Jordyn":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
        }

def manhattan(rating1,rating2): #计算两个
    # 计算曼哈顿距离
    distance = 0
    for key in rating1:
        if key in rating2:
            distance +=abs(rating1[key]-rating2[key])
    return distance


print manhattan(users['Bill'],users['Sam'])


def computeNearestNeighbor(username,users):  #计算某一个人和其他所有用户的距离
    distances = []
    for user in users:
        if user!=username:
            distance = manhattan(users[user],users[username])
            distances.append((distance,user))
    distances.sort()#default asc
    return distances#返回的为一二维数组


print computeNearestNeighbor('Hailey',users)

print computeNearestNeighbor('Hailey',users)[0][1]

print users[computeNearestNeighbor('Hailey',users)[0][1]] #拿到的是Veronica


def recommend(username,users):#为某一个人进行推荐
    nearest = computeNearestNeighbor(username,users)[0][1]#得到这个人最近的其他用户,拿到的是用户名字
    recommendations = []#进行排序
    #找出距离最近的用户评价过的 但是username没有评价过的乐队
    neighborRatings = users[nearest]
    userRatings = users[username]
    for artist in neighborRatings:
        if not artist in userRatings:
            recommendations.append((artist,neighborRatings[artist]))
    return sorted(recommendations,key =lambda  artistTuple:artistTuple[1],reverse=True)

print recommend('Hailey',users)
print recommend('Bill',users)
print recommend('Chan',users)



def minkowski(ratings1,ratings2,n):#ratinfs是一个用户对某个电影的评分列
    distance = 0
    for key in ratings1:
        if key in ratings2:
            distance+= pow(abs(ratings1[key]-ratings2[key]),n)
    return pow(distance,1.0/n)

print minkowski(users['Bill'],users['Chan'],1)


from math import sqrt

def pearson(ratings1,ratings2): #计算距离的一种，能够去除用户个人的评分习惯
    sum_xy = 0
    sum_x = 0
    sum_y = 0
    sum_x2 = 0
    sum_y2 = 0
    n = 0
    for key in ratings1:
        if key in ratings2:
            n +=1
            x = ratings1[key] #拿到对某乐队的评分
            y = ratings2[key]
            sum_xy +=x*y
            sum_x +=x
            sum_y +=y
            sum_x2 += pow(x,2)
            sum_y2 += pow(y,2)
    denominator = sqrt(sum_x2-pow(sum_x,2)/n)*sqrt(sum_y2-pow(sum_y,2)/n)
    if denominator == 0:
        return 0
    else:
        return (sum_xy-(sum_x*sum_y)/n)/denominator

print pearson(users['Dan'],users['Chan'])


def cosin(ratings1,ratings2):
    sum_xy = 0
    sum_x2 = 0
    sum_y2 = 0
    for key in ratings1:
        if key in ratings2:
            x=ratings1[key]
            y=ratings2[key]
            sum_xy+=x*y
            sum_x2 +=pow(x,2)
            sum_y2 += pow(y,2)
    cosDistance = sum_xy/(sqrt(sum_x2)*sqrt(sum_y2))
    return  cosDistance

print cosin(users['Angelica'],users['Veronica'])


"""
k近邻法 python代码
参数值：
data - 数据集
k - 选取几个邻居 : 保存这几个邻居的
n - 推荐几个乐队
metrics - 采用何种计算距离的方式
"""

import codecs
class recommender:
    def __init__(self,data,k=1,metric = 'pearson',n=5):
        self.k = k
        self.n = n
        self
