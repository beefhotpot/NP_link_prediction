# encoding: utf-8
import numpy as np
import networkx as net
import pandas as pd
import matplotlib.pyplot as plot

filePath1='/Users/gunannan/Downloads/机器学习/data/train.txt'
filePath2='/Users/gunannan/Downloads/机器学习/data/train_2.txt'
filePath3='/Users/gunannan/Downloads/机器学习/data/train_3.txt'
filePath4='/Users/gunannan/Downloads/机器学习/data/train_4.txt'
filePath5='/Users/gunannan/Downloads/机器学习/data/train_5.txt'


# #transfer the original data set to the format as the test set
# trian_2 doesn't have same source and sink while train_3 has

# file1=open(filePath1)
# file2=open(filePath2, 'w')
# file2.write('Source'+','+'Sink'+ '\n')
# # file3=open(filePath3, 'w')
# # file3.write('Source'+','+'Sink'+ '\n')
# num=0;
# for line in file1.readlines():
#     lineArr = line.strip().split()
#     for node in lineArr:
#         if node!=lineArr[0]:
#             file2.write(lineArr[0]+","+node+'\n')
#             num=num+1
# file1.close()
# file2.close()
# # for line in file1.readlines():
# #     lineArr = line.strip().split()
# #     for i in range(len(lineArr)):
# #         if i!=0:
# #             file3.write(lineArr[0]+","+lineArr[i]+'\n')
# #             num=num+1
# print(num)



# count the followee and follower for every user, and create train_4
# the format is: Source,Sourec_Followee,Source_Follower,Sink,Sink_Followee,Sink_Follower
# and cerate train_5, which is similar to train_4, but the format is node,followee,follower, the node is unique here,maybe useful?

# file2=open(filePath2)
# # file4=open(filePath4, 'w')
# # file4.write('Source'+','+'Source_Followee'+','+'Source_Follower'+','+'Sink'+','+'Sink_Followee'+ ',' + 'Sink_Follower'+ '\n')
# file5=open(filePath5, 'w')
# file5.write('Node'+','+'Followee'+','+'Follower'+ '\n')
# num=0
# followee={}
# follower={}
# file2.readline()
# for line in file2.readlines():
#     lineArr = line.strip().split(",")
#     if lineArr[0] not in followee:
#         followee[lineArr[0]] = 1
#     else:
#         followee[lineArr[0]] += 1
#     if lineArr[0] not in follower:
#         follower[lineArr[0]]=0
#
#     if lineArr[1] not in follower:
#         follower[lineArr[1]] = 1
#     else:
#         follower[lineArr[1]] += 1
#     if lineArr[1] not in followee:
#         followee[lineArr[1]]=0
#
# # file2.seek(0)
# # file2.readline()
# # for line in file2.readlines():
# #     lineArr = line.strip().split(",")
# #     file4.write(lineArr[0]+','+str(followee[lineArr[0]])+','+str(follower[lineArr[0]])+','
# #                 +lineArr[1]+','+str(followee[lineArr[1]])+','+str(follower[lineArr[1]]) + '\n')
#
# for key in followee.keys():
#     file5.write(key+','+str(followee[key])+','+str(follower[key])+ '\n')
#     num+=1
#
# file2.close()
# # file4.close()
# file5.close()
# print(num)
