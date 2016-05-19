#coding:utf-8

import os
#结果类别标识
MISMATCH = 0
OUT = 1
INVALID = 2

def getResults(flag):
    '''该函数用来遍历结果目录所有文件，并获取所有数据'''
    path = os.getcwd() + '/results/'
    result = []
    results = []
    for root, dirs, files in os.walk(path):
        for f in files:
            try:
                #不匹配的结果数据
                if MISMATCH == flag:
                    with open(path + 'mismatch/' + f, 'r') as mismatch_output:
                        lines = mismatch_output.readlines()
                        temps = []
                        for line in lines:
                            temp = line.strip('\n').split(',')
                            temps.append(temp)
                        result = temps
                #匹配的结果数据
                elif OUT == flag:
                    with open(path + 'out/' + f, 'r', encoding = 'utf-8') as out_output: 
                        lines = out_output.readlines()
                        temps = []
                        for line in lines:
                            temp = line.split('@#$')
                            for i in [2, 2, 2, 2, 2, 2, 7, 9]:
                                temp.pop(i)
                            temps.append(temp)                        
                        result = temps
                #非法的结果数据
                elif INVALID == flag:
                    with open(path + 'invalid/' + f, 'r', encoding = 'utf-8') as invalid_output:
                        result = invalid_output.readlines()
                        result.pop(0)                     
            except IOError as err:
                #print('File Error: ' + str(err))
                pass
            results.extend(result)
    #返回结果数据
    return results
    
if __name__ == '__main__':
    mis = getResults(MISMATCH)
    print(mis)
##    t = getResults(r'C:\Users\yuanwb\Desktop\invalid\\', 2)
##    print(t)
