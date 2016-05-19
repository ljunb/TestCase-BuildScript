# -*- coding:utf-8 -*-

'''
---      Author: ljunb
--- Last update: 20150618
---     Purpose: to create the test data of Big Data project(app:011-019)
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
REPEAT_COUNT = 2
NBR_LEN = len(applib.USR_NBR)
NET_TYP_LEN = len(applib.NET_TYP)
DICT_LEN = len(applib.IP_PORT) + 1

#创建存放测试数据的目录
def mkDir():
    # 如果不存在testdatas目录，则创建目录
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
def getTestData(destIp, destPort, stat_time, end_time):
    #采用random.choice(seq)方法来随机获取序列中的元素
    #以list对象返回封装的测试数据
    return [random.choice(applib.USR_NBR), random.choice(applib.USR_IP), destIp, destPort,
            str(applib.getDurTime()), stat_time, end_time, random.choice(applib.APN), 
	    '', '', random.choice(applib.NET_TYP), random.choice(applib.URL_LVL1), 
	    random.choice(applib.URL_LVL2), str(randUP_FLUX), str(randDOWN_FLUX)]
  
#主函数
def main():
    mkDir()  
    #先随机获得测试数据，封装到一个字典，作为参数单一重复场景基础数据
    randMethod()
    repeat_stime, repeat_etime = applib.getRandTime()   
    repeatData = getTestData(applib.IP_PORT[randDictKey][0], applib.IP_PORT[randDictKey][1],
                             repeat_stime, repeat_etime)
        
    #创建新的测试数据文件-IP和PORT没有匹配的数据
    try:
        #使用with自动完成file的关闭
        with open(os.getcwd() + '\\testdatas\APP_011.txt', 'a') as output_011, \
            open(os.getcwd() + '\\testdatas\APP_012.txt', 'a') as output_012, \
            open(os.getcwd() + '\\testdatas\APP_018.txt', 'a') as output_018, \
            open(os.getcwd() + '\\testdatas\APP_019.txt', 'a') as output_019:
            
            #用例011：能够匹配上app规则库
            output_011.write('#用例011：能够匹配上app规则库\n')
            #用例012：IP和端口号匹配不上app规则库
            output_012.write('#用例012：IP和端口号匹配不上app规则库\n')
            #用例018：所有参数重复            
            output_018.write('#用例018：所有参数重复\n')
            #用例019：参数单一重复，匹配APP规则库           
            output_019.write('#用例019：参数单一重复，匹配APP规则库\n')
            
            #生成测试数据
            for i in range(DATA_COUNT):
                #调用随机函数
                randMethod()
                #随机生成收到请求时间和结束时间
                stat_time, end_time = applib.getRandTime()
                
                #用例011：能够匹配上app规则库
                data_011 = getTestData(applib.IP_PORT[randDictKey][0], applib.IP_PORT[randDictKey][1],
                                       stat_time, end_time)
                output_011.write('@#$'.join(data_011) + '@#$\n')
                
                #用例012：IP和端口号匹配不上app规则库
                data_012 = getTestData(applib.getDEST_IP(), applib.getDEST_Port(), stat_time, end_time)
                output_012.write('@#$'.join(data_012) + '@#$\n')
                               
            #用例018：所有参数重复               
            data_018 = getTestData(applib.IP_PORT[randDictKey][0], applib.IP_PORT[randDictKey][1], stat_time, end_time)
            for i in range(DATA_COUNT):
                output_018.write('@#$'.join(data_018) + '@#$\n')

            #用例019：参数单一重复，匹配APP规则库
            '''仍未做到单一参数重复
            '''
            for index, param in enumerate(repeatData):
                for i in range(REPEAT_COUNT):
                    #调用随机函数
                    randMethod()
                    #随机生成收到请求时间和结束时间
                    stime, etime = applib.getRandTime()
                    data_019 = getTestData(applib.IP_PORT[randDictKey][0], applib.IP_PORT[randDictKey][1],
                                           stime, etime)
                    if index == 5:
                        data_019[index] = param
                        data_019[6], data_019[4] = getRandDate(param, 1)
                    elif index == 6:
                        data_019[index] = param
                        data_019[5], data_019[4] = getRandDate(param, 0)                        
                    else:
                        data_019[index] = param
                    output_019.write('@#$'.join(data_019) + '@#$\n')
                     
    #打印错误信息
    except IOError as ioerr:
        print('File error: ' + str(ioerr))

def getRandDate(time, flag):
    #获取日期
    temp_date = time.split()[0]
    temp_time = time.split()[1]
    #获取时间
    hour = temp_time.split(':')[0]
    minute = int(temp_time.split(':')[1])
    secend = int(temp_time.split(':')[2].split('.')[0])
    msecend = temp_time.split(':')[2].split('.')[1]

    durtime = random.randrange(0, 20)
    #返回结束时间
    if flag:
        #间隔秒数
        secend += durtime
        
        if secend >= 60:
            minute += 1
            secend -= 60
    #返回开始时间
    else:
        if secend >= 19:
            secend -= durtime
        else:
            secend = secend - durtime + 60
            minute -= 1
                    
    result_time = [hour, formatMethod(minute), formatMethod(secend)]

    return temp_date + ' ' + ':'.join(result_time) + '.' + msecend, str(durtime)
#格式化函数
def formatMethod(t_param):
        #时间参数小于10的，以‘0X’格式显示
        if t_param < 10:
            return '0' + str(t_param)
        else :
            return str(t_param)  
       
if __name__ == '__main__':
	main()
