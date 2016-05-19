# -*- coding:utf-8 -*-

'''
---      Author: ljunb
--- Last update: 20150625
---     Purpose: to create the test data of Big Data project(browse:028-040)
'''

import os
import random
import datalib

#基础数据的列表长度
DATA_COUNT = 10
REPEAT_COUNT = 2
NBR_LEN = len(datalib.USR_NBR)
NET_TYP_LEN = len(datalib.NET_TYP)
DICT_LEN = len(datalib.IP_PORT) + 1


#创建存放测试数据的目录
def mkDir():
    if not os.path.exists('testdatas'):
        os.mkdir('testdatas')

    # 删除所有测试数据文件
    for root, dirs, files in os.walk(os.getcwd() + '/testdatas/'):
        for file in files:
            os.remove(root+file)

#生成随机数方法
def randMethod():
	#定义全局变量，作为各list的随机下标
 	global randPROTO_TYP, randUP_FLUX, randDOWN_FLUX, randDictKey
 	
 	#会话协议类型
 	randPROTO_TYP = random.randrange(0, 2)
 	#上、下行流量
 	randUP_FLUX = random.randrange(0, 9999)
 	randDOWN_FLUX = random.randrange(0, 99999)
 	#生成随机字典下标
 	randDictKey = random.randrange(1, DICT_LEN)

#获取不同场景的测试数据
def getTestData(destIp, destPort, url):
    #采用random.choice(seq)方法来随机获取序列中的元素
    #以list对象返回封装的测试数据
    return [random.choice(datalib.USR_NBR), random.choice(datalib.NET_TYP), random.choice(datalib.APN), 
        '', '', destIp, destPort, str(randPROTO_TYP), url, random.choice(datalib.DEVICE), 
        random.choice(datalib.CNTN_TYP),'', random.choice(datalib.URL_LVL2), str(randUP_FLUX), 
        str(randDOWN_FLUX), STAT_TIME, END_TIME]
        
#主函数
def main():
        global STAT_TIME, END_TIME
        randMethod()
        STAT_TIME, END_TIME = datalib.getRandTime()
        #URL匹配规则库
        repeatUrlMatchData = getTestData(datalib.IP_PORT[randDictKey][0], datalib.IP_PORT[randDictKey][1],
                                      random.choice(datalib.Match_URL))

        #APP匹配规则库
        repeatAppMatchData = getTestData(datalib.IP_PORT[randDictKey][0], datalib.IP_PORT[randDictKey][1],
                                       random.choice(datalib.MisMatch_URL))

        #URL属于过滤库
        repeatFilteredData = getTestData(datalib.IP_PORT[randDictKey][0], datalib.IP_PORT[randDictKey][1],
                                      random.choice(datalib.WebSite_URL))
	#创建存放测试数据的文件夹
        mkDir()
        
        try:
            with open(os.getcwd() + '\\testdatas\Browse_028.txt', 'a') as output_028, \
                open(os.getcwd() + '\\testdatas\Browse_029.txt', 'a') as output_029, \
                open(os.getcwd() + '\\testdatas\Browse_030.txt', 'a') as output_030, \
                open(os.getcwd() + '\\testdatas\Browse_031.txt', 'a') as output_031, \
                open(os.getcwd() + '\\testdatas\Browse_032.txt', 'a') as output_032, \
                open(os.getcwd() + '\\testdatas\Browse_033.txt', 'a') as output_033, \
                open(os.getcwd() + '\\testdatas\Browse_034.txt', 'a') as output_034, \
                open(os.getcwd() + '\\testdatas\Browse_035.txt', 'a') as output_035, \
                open(os.getcwd() + '\\testdatas\Browse_036.txt', 'a') as output_036, \
                open(os.getcwd() + '\\testdatas\Browse_037.txt', 'a') as output_037, \
                open(os.getcwd() + '\\testdatas\Browse_038.txt', 'a') as output_038, \
                open(os.getcwd() + '\\testdatas\Browse_039.txt', 'a') as output_039, \
                open(os.getcwd() + '\\testdatas\Browse_040.txt', 'a') as output_040:          
                #用例028：url为空，其他参数正常输入
                output_028.write('#用例028：url为空，其他参数正常输入\n')
                #用例029：IP为空，其他参数正常输入
                output_029.write('#用例029：IP为空，其他参数正常输入\n')
                #用例030：端口号为空，其他参数正常输入
                output_030.write('#用例030：端口号为空，其他参数正常输入\n')
                #用例031：用户号码为空 
                output_031.write('#用例031：用户号码为空 \n')                
                #用例032：网络标识为空
                output_032.write('#用例032：网络标识为空\n')
                #用例033：收到请求时间为空
                output_033.write('#用例033：收到请求时间为空\n')
                #用例034：分隔符错误 
                output_034.write('#用例034：任一分隔符错误\n')
                #用例035：分隔符缺少
                output_035.write('#用例035：随机缺少一个分隔符\n')
                #用例036：没有按照格式进行输入内容（缺少参数）
                output_036.write('#用例036：没有按照格式进行输入内容（缺少参数）\n')
                #用例037：所有参数都重复
                output_037.write('#用例037：所有参数都重复（URL随机为匹配或不匹配）\n')
                #用例038：用户号码重复
                output_038.write('#用例038：参数单一重复，URL匹配上网站规则库\n')
                #用例039：网络标识重复
                output_039.write('#用例039：参数单一重复，匹配上APP规则库\n')
                #用例040：起始时间重复
                output_040.write('#用例040：参数单一重复，URL属于过滤库\n')
                    
                #生成测试数据
                for i in range(DATA_COUNT):
                    #调用生成随机数方法
                    randMethod()
                    #随机生成收到请求时间和结束时间
                    STAT_TIME, END_TIME = datalib.getRandTime()

                    #用例028：url为空，其他参数正常输入
                    data_028 = getTestData(datalib.IP_PORT[randDictKey][0], datalib.IP_PORT[randDictKey][1], '')
                    output_028.write('@#$'.join(data_028) + '@#$\n')

                    #用例029：IP为空，其他参数正常输入
                    data_029 = getTestData('', datalib.IP_PORT[randDictKey][1], random.choice(datalib.Match_URL))
                    output_029.write('@#$'.join(data_029) + '@#$\n')

                    #用例030：端口号为空，其他参数正常输入
                    data_030 = getTestData(datalib.IP_PORT[randDictKey][0], '', random.choice(datalib.Match_URL))
                    output_030.write('@#$'.join(data_030) + '@#$\n')

                    #用例031：用户号码为空
                    data_031 = getTestData(datalib.IP_PORT[randDictKey][0], datalib.IP_PORT[randDictKey][1], \
                                           random.choice(datalib.Match_URL))
                    data_031[0] = ''
                    output_031.write('@#$'.join(data_031) + '@#$\n')

                    #用例032：网络标识为空
                    data_032 = getTestData(datalib.IP_PORT[randDictKey][0], datalib.IP_PORT[randDictKey][1], \
                                           random.choice(datalib.Match_URL))
                    data_032[1] = ''
                    output_032.write('@#$'.join(data_032) + '@#$\n')

                    #用例033：收到请求时间为空
                    data_033 = getTestData(datalib.IP_PORT[randDictKey][0], datalib.IP_PORT[randDictKey][1], \
                                           random.choice(datalib.Match_URL))
                    data_033[15] = ''
                    output_033.write('@#$'.join(data_033) + '@#$\n')

                    #用例034：任一分隔符错误
                    data_034 = []
                    tempdata_034 = getTestData(datalib.IP_PORT[randDictKey][0], datalib.IP_PORT[randDictKey][1], \
                                           random.choice(datalib.Match_URL))
                    rchar = ['@#$' for i in range(17)]
                    rchar[random.randrange(0, 15)] = random.choice(['@#', '@', '#', '$', '#$', '@$', ','])
                    print(rchar)
                    for param, char in zip(tempdata_034, rchar):
                        data_034.append(param + char)
                    output_034.write(''.join(data_034) + '\n')

                    #用例035：分隔符随机缺少一个
                    data_035 = []
                    chars = ['@#$' for i in range(17)]
                    chars[random.randrange(0, 17)] = ''
                    for param, char in zip(data_034, chars):
                        data_035.append(param + char)
                    output_035.write(''.join(data_035) + '\n')

                    #用例036：没有按照格式进行输入内容（缺少除URL、IP&PORT外的任一参数）
                    #del(data_034[random.choice([i for i in range(17) if i not in [5, 6, 8]])])
                    data_034.pop(random.choice([i for i in range(17) if i not in [5, 6, 8]]))
                    output_036.write('@#$'.join(data_034) + '@#$\n')

                #用例037：所有参数都重复（URL随机为匹配或不匹配）                
                data_03701 = getTestData(datalib.IP_PORT[randDictKey][0], datalib.IP_PORT[randDictKey][1], \
                                               random.choice(datalib.Match_URL))
                data_03702 = getTestData(datalib.IP_PORT[randDictKey][0], datalib.IP_PORT[randDictKey][1], \
                                               random.choice(datalib.MisMatch_URL))
                for i in range(DATA_COUNT):
                    temp = random.randrange(0, 2)
                    if temp == 0:
                        output_037.write('@#$'.join(data_03701) + '@#$\n')
                    else:
                        output_037.write('@#$'.join(data_03702) + '@#$\n')
                        

                #用例038：参数单一重复，匹配上网站规则库
                getRepeatData(repeatUrlMatchData, output_038, 0)
                        
                #用例039：参数单一重复，匹配上APP规则库
                getRepeatData(repeatAppMatchData, output_039, 1)

                #用例040：参数单一重复，URL属于过滤库
                getRepeatData(repeatFilteredData, output_040, 2)
                                                           
        #打印出错误信息
        except IOError as err:
            print('File Error: ' + str(err))

def getRepeatData(p_data, file, flag):
    for index, param in enumerate(p_data):
        for i in range(REPEAT_COUNT):
            #调用随机函数
            randMethod()
            #随机生成收到请求时间和结束时间
            stime, etime = datalib.getRandTime()
            if flag == 0:
                url = random.choice(datalib.Match_URL)
            elif flag == 1:
                url = random.choice(datalib.MisMatch_URL)
            else:
                url = random.choice(datalib.WebSite_URL)
                
            ip = datalib.IP_PORT[randDictKey][0]
            port = datalib.IP_PORT[randDictKey][1]
            data = getTestData(ip, port, url)
        
            if index == 15:
                data[index] = param
                data[16] = getRandDate(param, 1)
            elif index == 16:
                data[index] = param
                data[15] = getRandDate(param, 0)
            else:
                data[index] = param
                data[15] = stime
                data[16] = etime

            file.write('@#$'.join(data) + '@#$\n')
        
def getRandDate(time, flag):
    #获取日期
    temp_date = time.split()[0]
    temp_time = time.split()[1]
    #获取时间
    hour = temp_time.split(':')[0]
    minute = int(temp_time.split(':')[1])
    secend = int(temp_time.split(':')[2].split('.')[0])
    msecend = temp_time.split(':')[2].split('.')[1]

    durtime = random.randrange(0, 5)
    #返回结束时间
    if flag:
        #间隔秒数
        secend += durtime
        
        if secend >= 60:
            minute += 1
            secend -= 60
    #返回开始时间
    else:
        if secend >= 5:
            secend -= durtime
        else:
            secend = secend - durtime + 60
            minute -= 1
                    
    result_time = [hour, datalib.formatMethod(minute), datalib.formatMethod(secend)]

    return temp_date + ' ' + ':'.join(result_time) + '.' + msecend


if __name__ == '__main__':
	main()
