# -*- coding:utf-8 -*-

'''
---      Author: ljunb
--- Last update: 20150618
---     Purpose: to create the test data of Big Data project(app:001-010)
'''

import os
import random
import applib
#基础数据模块，以下皆为list对象：
#   用户号码-USR_NBR
#   终端IP-USR_IP
#   APN类型-APN;
#   网络标识-NET_TYP
#   一级分类-URL_LVL1
#   二级分类-URL_LVL2
#   IP&PORT匹配字典-IP_PORT
#   在线服务器IP地址-getDEST_IP()
#   目的端口-getDEST_Port()
#   随机时间-getRandTime()

#IP/PORT相匹配的字典长度
DATA_COUNT = 10
NBR_LEN = len(applib.USR_NBR)
NET_TYP_LEN = len(applib.NET_TYP)
DICT_LEN = len(applib.IP_PORT) + 1

#创建存放测试数据的目录
def mkDir():
    #如果不存在testdatas目录，则创建目录
    if not os.path.exists('testdatas'):
        os.mkdir('testdatas')
    # 删除所有测试数据文件
    for root, dirs, files in os.walk(os.getcwd() + '/testdatas/'):
        for file in files:
            os.remove(root+file)    

#生成随机数方法
def randMethod():
    #定义全局变量
    global randUP_FLUX, randDOWN_FLUX, randDictKey
 	
    #上、下行流量
    randUP_FLUX = random.randrange(0, 9999)
    randDOWN_FLUX = random.randrange(0, 99999)
    #生成随机字典下标
    randDictKey = random.randrange(1, DICT_LEN)

#获取不同场景的测试数据
def getTestData(destIp, destPort):
    #采用random.choice(seq)方法来随机获取序列中的元素
    #以list对象返回封装的测试数据
    return [random.choice(applib.USR_NBR), random.choice(applib.USR_IP), destIp, destPort,
            str(applib.getDurTime()), STAT_TIME, END_TIME, random.choice(applib.APN), 
	    '', '', random.choice(applib.NET_TYP), random.choice(applib.URL_LVL1), 
	    random.choice(applib.URL_LVL2), str(randUP_FLUX), str(randDOWN_FLUX)]
        
#主函数
def main():
    global STAT_TIME, END_TIME
    mkDir()
    #生成重复数据需要的下标
    repeatFlag = 1
    repeatNBR = random.randrange(0, NBR_LEN)
    repeatTYP = random.randrange(0, NET_TYP_LEN)
    repeatIndex = random.randrange(0, DICT_LEN)
    repeatStat_Time, temp = applib.getRandTime()
    
    #创建新的测试数据文件-IP和PORT没有匹配的数据
    try:
        #使用with自动完成file的关闭
        with open(os.getcwd() + '\\testdatas\APP_001.txt', 'a') as output_001, \
            open(os.getcwd() + '\\testdatas\APP_002.txt', 'a') as output_002, \
            open(os.getcwd() + '\\testdatas\APP_003.txt', 'a') as output_003, \
            open(os.getcwd() + '\\testdatas\APP_004.txt', 'a') as output_004, \
            open(os.getcwd() + '\\testdatas\APP_005.txt', 'a') as output_005, \
            open(os.getcwd() + '\\testdatas\APP_006.txt', 'a') as output_006, \
            open(os.getcwd() + '\\testdatas\APP_007.txt', 'a') as output_007, \
            open(os.getcwd() + '\\testdatas\APP_008.txt', 'a') as output_008, \
            open(os.getcwd() + '\\testdatas\APP_009.txt', 'a') as output_009, \
            open(os.getcwd() + '\\testdatas\APP_010.txt', 'a') as output_010:
            
            #用例001：IP为空
            output_001.write('#用例001：IP为空\n')
            #用例002：PORT为空
            output_002.write('#用例002：PORT为空\n')
            #用例003：用户号码为空
            output_003.write('#用例003：用户号码为空\n')
            #用例004：起始时间为空
            output_004.write('#用例004：起始时间为空\n')
            #用例005：网络标识为空
            output_005.write('#用例005：网络标识为空\n')            
            #用例006：分隔符之间的参数为空
            output_006.write('#用例006：分隔符之间的参数为空\n')
            #用例007：空数据
            output_007.write('#用例007：空数据\n')
            #用例008：分隔符错误
            output_008.write('#用例008：分隔符错误\n')
            #用例009：分隔符随机缺少一个
            output_009.write('#用例009：分隔符随机缺少一个\n')
            #用例010：没有按照格式进行输入内容
            output_010.write('#用例010：没有按照格式进行输入内容（缺少除IP&PORT外的任一参数）\n')
            
            #生成测试数据
            for i in range(DATA_COUNT):
                #调用随机函数
                randMethod()
                #随机生成收到请求时间和结束时间
                STAT_TIME, END_TIME = applib.getRandTime()
                
                #用例001：IP为空
                data_001 = getTestData('', applib.IP_PORT[randDictKey][1])
                output_001.write('@#$'.join(data_001) + '@#$\n')

                #用例002：PORT为空
                data_002 = getTestData(applib.IP_PORT[randDictKey][0], '')
                output_002.write('@#$'.join(data_002) + '@#$\n')

                #用例003：用户号码为空
                data_003 = getTestData(applib.IP_PORT[randDictKey][0], applib.IP_PORT[randDictKey][1])
                data_003[0] = ''
                output_003.write('@#$'.join(data_003) + '@#$\n')

                #用例004：起始时间为空
                data_004 = getTestData(applib.IP_PORT[randDictKey][0], applib.IP_PORT[randDictKey][1])
                data_004[5] = ''
                output_004.write('@#$'.join(data_004) + '@#$\n')

                #用例005：网络标识为空
                data_005 = getTestData(applib.IP_PORT[randDictKey][0], applib.IP_PORT[randDictKey][1])
                data_005[10] = ''
                output_005.write('@#$'.join(data_005) + '@#$\n')
                
                #用例006：分隔符之间的参数为空
                data_006 = ['' for i in range(15)]
                output_006.write('@#$'.join(data_006) + '@#$\n')
                
                #用例007：空数据

                #用例008：分隔符错误（任一分隔符）
                data_008 = []
                tempdata_008 = getTestData(applib.IP_PORT[randDictKey][0], applib.IP_PORT[randDictKey][1])
                rchar = ['@#$' for i in range(15)]
                rchar[random.randrange(0, 15)] = random.choice(['@#', '@', '#', '$', '#$', '@$', ','])                
                for param, char in zip(tempdata_008, rchar):
                    data_008.append(param + char)
                output_008.write(''.join(data_008) + '\n')
                
                #用例009：分隔符随机缺少一个
                data_009 = []
                tempdata_009 = getTestData(applib.IP_PORT[randDictKey][0], applib.IP_PORT[randDictKey][1])
                chars = ['@#$' for i in range(15)]
                chars[random.randrange(0, 15)] = ''
                for param, char in zip(tempdata_009, chars):
                    data_009.append(param + char)
                output_009.write(''.join(data_009) + '\n')
                
                #用例010：没有按照格式进行输入内容（缺少除IP&PORT外的任一参数）
                #data_008.pop(random.choice([i for i in range(15) if i not in [2, 3]]))
                del(data_008[random.choice([i for i in range(15) if i not in [2, 3]])])        
                output_010.write('@#$'.join(data_008) + '@#$\n')

                       
    #打印错误信息
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
    
if __name__ == '__main__':
	main()
