# -*- coding:utf-8 -*-

'''
---      Author: ljunb
--- Last update: 20150619
---     Purpose: to create the test data of Big Data project(app:006-027)
'''

import os
import random
import datalib


#基础数据的列表长度
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
	#创建存放测试数据的文件夹
        mkDir()    
        try:
            with open(os.getcwd() + '\\testdatas\Browse_006.txt', 'a') as output_006, \
                open(os.getcwd() + '\\testdatas\Browse_008.txt', 'a') as output_008, \
                open(os.getcwd() + '\\testdatas\Browse_009.txt', 'a') as output_009, \
                open(os.getcwd() + '\\testdatas\Browse_011.txt', 'a') as output_011, \
                open(os.getcwd() + '\\testdatas\Browse_012.txt', 'a') as output_012, \
                open(os.getcwd() + '\\testdatas\Browse_014.txt', 'a') as output_014, \
                open(os.getcwd() + '\\testdatas\Browse_015.txt', 'a') as output_015, \
                open(os.getcwd() + '\\testdatas\Browse_026.txt', 'a') as output_026, \
                open(os.getcwd() + '\\testdatas\Browse_027.txt', 'a') as output_027:
                            
                #用例006：URL匹配上过滤库
                output_006.write('#用例006：URL匹配上过滤库\n')
                #用例008：URL、IP和端口号都为空
                output_008.write('#用例008：URL、IP和端口号都为空\n')
                #用例009：URL能够匹配上网站规则库
                output_009.write('#用例009：URL能够匹配上网站规则库\n')
                #用例011：url匹配不上网站规则库，IP和端口号匹配上app规则库 
                output_011.write('#用例011：url匹配不上网站规则库，IP和端口号匹配上app规则库\n')                
                #用例012：数据匹配不上网站规则库和APP规则库
                output_012.write('#用例012：数据匹配不上网站规则库和APP规则库\n')
                #用例014：数据url为空，能够匹配上app规则库
                output_014.write('#用例014：数据url为空，能够匹配上app规则库\n')
                #用例015：数据url为空，能够匹配不上app规则库 
                output_015.write('#用例015：数据url为空，能够匹配不上app规则库\n')
                #用例026：分隔符之间的参数为空
                output_026.write('#用例026：分隔符之间的参数为空\n')
                #用例027：空数据
                output_027.write('#用例027：空数据\n')
                    
                #生成测试数据
                for i in range(5):
                    #调用生成随机数方法
                    randMethod()
                    #随机生成收到请求时间和结束时间
                    STAT_TIME, END_TIME = datalib.getRandTime()

                    #用例006：URL匹配上过滤库
                    data_006 = getTestData(datalib.IP_PORT[randDictKey][0], datalib.IP_PORT[randDictKey][1],
                            random.choice(datalib.WebSite_URL))
                    output_006.write('@#$'.join(data_006) + '@#$\n')

                    #用例008:：URL、IP和端口号都为空
                    data_008 = getTestData('', '', '')
                    output_008.write('@#$'.join(data_008) + '@#$\n')

                    #用例009：URL能够匹配网站规则库，IP和端口号匹配app规则库
                    data_00901 = getTestData(datalib.IP_PORT[randDictKey][0], datalib.IP_PORT[randDictKey][1],
                            random.choice(datalib.Match_URL))
                    output_009.write('@#$'.join(data_00901) + '@#$\n')

                    #用例009：URL能够匹配网站规则库，IP和端口号不匹配app规则库
                    data_00902 = getTestData(datalib.getIP(), datalib.getPort(), random.choice(datalib.Match_URL))
                    output_009.write('@#$'.join(data_00902) + '@#$\n')

                    #用例011：url匹配不上网站规则库，IP和端口号匹配上app规则库
                    data_011 = getTestData(datalib.IP_PORT[randDictKey][0], datalib.IP_PORT[randDictKey][1],
                            random.choice(datalib.MisMatch_URL))
                    output_011.write('@#$'.join(data_011) + '@#$\n')

                    #用例012：数据匹配不上网站规则库和APP规则库
                    data_012 = getTestData(datalib.getIP(), datalib.getPort(), random.choice(datalib.MisMatch_URL))
                    output_012.write('@#$'.join(data_012) + '@#$\n')

                    #用例014：数据url为空，能够匹配上app规则库
                    data_014 = getTestData(datalib.IP_PORT[randDictKey][0], datalib.IP_PORT[randDictKey][1], '')
                    output_014.write('@#$'.join(data_014) + '@#$\n')

                    #用例015：数据url为空，匹配不上app规则库
                    data_015 = getTestData(datalib.getIP(), datalib.getPort(), '')
                    output_015.write('@#$'.join(data_015) + '@#$\n')                    

                    #用例026：分隔符之间的参数为空
                    data_026 = ['' for i in range(17)]
                    output_026.write('@#$'.join(data_026) + '@#$\n')

                    #用例027：空数据
                                                            
        #打印出错误信息
        except IOError as err:
            print('File Error: ' + str(err))

if __name__ == '__main__':
	main()
