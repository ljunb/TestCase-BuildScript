# -*- coding:utf-8 -*-

'''
-      Author: ljunb                                                   
- Last update: 20150625                                                
-     Purpose: to create the test data of Big Data project(GN:001-011) 
'''

import random
import os
import gnlib

DATA_COUNT = 10
REPEAT_COUNT = 2
NBR_LEN = len(gnlib.USR_NBR)

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
    #定义全局变量(随机数)
    global randURL_LVL2, randURL_LVL1, \
           randCALL_CNT, randUP_FLUX, randDOWN_FLUX, randIndex
    #生成随机数 
    randURL_LVL2 = random.randrange(0, 10000)
    randURL_LVL1 = random.randrange(0, 10000)
    randCALL_CNT = random.randrange(1, 10)
    randUP_FLUX = random.randrange(0, 9999)
    randDOWN_FLUX = random.randrange(0, 999999)       
    
#封装测试数据方法
def getTestData(stat_dts, usr_nbr, randUrl):
    return [stat_dts, usr_nbr, random.choice(gnlib.APN), randUrl, str(randURL_LVL2), str(randURL_LVL1),
            str(randCALL_CNT), str(randUP_FLUX), str(randDOWN_FLUX)]

        
#main函数
def main():
    #创建存放测试数据的目录testdatas
    mkDir()

    randMethod()
    urlMatchData = getTestData(gnlib.getRandTime(), random.choice(gnlib.USR_NBR), random.choice(gnlib.Match_URL))
    websiteData = getTestData(gnlib.getRandTime(), random.choice(gnlib.USR_NBR), random.choice(gnlib.WebSite_URL))
    
    #生成重复数据标识
    repeatFlag = 1
    try:
        with open(os.getcwd() + '\\testdatas\GN_001.txt', 'a') as output_001, \
            open(os.getcwd() + '\\testdatas\GN_002.txt', 'a') as output_002, \
            open(os.getcwd() + '\\testdatas\GN_003.txt', 'a') as output_003, \
            open(os.getcwd() + '\\testdatas\GN_004.txt', 'a') as output_004, \
            open(os.getcwd() + '\\testdatas\GN_005.txt', 'a') as output_005, \
            open(os.getcwd() + '\\testdatas\GN_006.txt', 'a') as output_006, \
            open(os.getcwd() + '\\testdatas\GN_007.txt', 'a') as output_007, \
            open(os.getcwd() + '\\testdatas\GN_008.txt', 'a') as output_008, \
            open(os.getcwd() + '\\testdatas\GN_009.txt', 'a') as output_009, \
            open(os.getcwd() + '\\testdatas\GN_010.txt', 'a') as output_010, \
            open(os.getcwd() + '\\testdatas\GN_011.txt', 'a') as output_011, \
            open(os.getcwd() + '\\testdatas\GN_012.txt', 'a') as output_012, \
            open(os.getcwd() + '\\testdatas\GN_013.txt', 'a') as output_013, \
            open(os.getcwd() + '\\testdatas\GN_019.txt', 'a') as output_019, \
            open(os.getcwd() + '\\testdatas\GN_020.txt', 'a') as output_020:
            #创建新的存放测试数据的文件
            #用例001：统计时间片为空
            output_001.write('#用例001：统计时间片为空\n')
            #用例002：用户号码为空
            output_002.write('#用例002：用户号码为空\n')
            #用例003：URL为空
            output_003.write('#用例003：URL为空\n')
            #用例004：分隔符之间参数为空
            output_004.write('#用例004：分隔符之间参数为空\n')
            #用例005：无数据
            output_005.write('#用例005：无数据\n')
            #用例006：完全重复的数据
            output_006.write('#用例006：完全重复的数据\n')           
            #用例007：URL在过滤库内
            output_007.write('#用例007：URL在过滤库内\n')            
            #用例008：其他参数为空（统计时间片、用户号码、url以外）
            output_008.write('#用例008：其他参数为空（统计时间片、用户号码、url以外）\n')
            #用例009：分隔符错误
            output_009.write('#用例009：任一分隔符错误\n')
            #用例010：分隔符缺少
            output_010.write('#用例010：随机缺少一个分隔符\n')
            #用例011：没有按照格式进行输入内容
            output_011.write('#用例011：没有按照格式进行输入内容（缺少除URL外的任一参数）\n')
            #用例012：URL能够匹配上网站规则库
            output_012.write('#用例012：URL能够匹配上网站规则库\n')
            #用例013：URL匹配不上网站规则库
            output_013.write('#用例013：URL匹配不上网站规则库\n')
            #用例019：参数单一重复，匹配上网站规则库
            output_019.write('#用例019：参数单一重复，匹配上网站规则库\n')
            #用例020：参数单一重复，URL属于过滤库
            output_020.write('#用例020：参数单一重复，URL属于过滤库\n')
            
            #随机生成测试数据
            for i in range(DATA_COUNT): 
                #生成随机数
                randMethod()

                #用例001：统计时间片为空
                data_001 = getTestData('', random.choice(gnlib.USR_NBR), random.choice(gnlib.Match_URL))
                output_001.write(','.join(data_001) + '\n')
                
                #用例002：用户号码为空
                data_002 = getTestData(gnlib.getRandTime(), '', random.choice(gnlib.Match_URL))
                output_002.write(','.join(data_002) + '\n')

                #用例003：URL为空
                data_003 = getTestData(gnlib.getRandTime(), random.choice(gnlib.USR_NBR), '')
                output_003.write(','.join(data_003) + '\n')

                #用例004：分隔符之间参数为空
                data_004 = ['' for i in range(9)]
                output_004.write(','.join(data_004) + '\n')

                #用例005：无数据

                #用例006：完全重复的数据
                while repeatFlag:
                    data_006 = getTestData(gnlib.getRandTime(), random.choice(gnlib.USR_NBR), random.choice(gnlib.Match_URL))
                    for i in range(DATA_COUNT):
                        output_006.write(','.join(data_006) + '\n')
                    repeatFlag -= 1                    
                
                #用例007：URL在过滤库内
                data_007 = getTestData(gnlib.getRandTime(), random.choice(gnlib.USR_NBR), random.choice(gnlib.WebSite_URL))
                output_007.write(','.join(data_007) + '\n')

                #用例008：其他参数为空（统计时间片、用户号码、url以外）
                data_008 = [gnlib.getRandTime(), random.choice(gnlib.USR_NBR), '', random.choice(gnlib.Match_URL)] + \
                                    ['' for i in range(5)]
                output_008.write(','.join(data_008) + '\n')

                #用例009：分隔符错误(任一分隔符错误)
                data_009 = []
                tempdata_009 = getTestData(gnlib.getRandTime(), random.choice(gnlib.USR_NBR), random.choice(gnlib.Match_URL))
                rchar = [',' for i in range(9)]
                rchar[random.randrange(0, 9)] = random.choice(['@#', '@', '#', '$', '#$', '@$', '@#$', '!'])                
                for param, char in zip(tempdata_009, rchar):
                    data_009.append(param + char)
                output_009.write(''.join(data_009).rstrip(',') + '\n')
                

                #用例010：分隔符缺少任意一个
                data_010 = []
                chars = [',' for i in range(9)]
                chars[random.randrange(0, 9)] = ''
                for param, char in zip(data_009, chars):
                    data_010.append(param + char)
                output_010.write(''.join(data_010).rstrip(',') + '\n')
                
                #用例011：没有按照格式进行输入内容（缺少除URL外的其他任一参数）
                data_011 = getTestData(gnlib.getRandTime(), random.choice(gnlib.USR_NBR), random.choice(gnlib.Match_URL))
                del(data_011[random.choice([i for i in range(9) if i != 3])])
                output_011.write(','.join(data_011) + '\n')

                #用例012：URL能够匹配上网站规则库
                data_012 = getTestData(gnlib.getRandTime(), random.choice(gnlib.USR_NBR), random.choice(gnlib.Match_URL))
                output_012.write(','.join(data_012) + '\n')

                #用例013：URL匹配不上网站规则库
                data_013 = getTestData(gnlib.getRandTime(), random.choice(gnlib.USR_NBR), random.choice(gnlib.MisMatch_URL))
                output_013.write(','.join(data_013) + '\n')

            #用例019：参数单一重复，匹配上网站规则库
            getRepeatData(output_019, urlMatchData, 1)
            
            #用例020：参数单一重复，URL属于过滤库
            getRepeatData(output_020, websiteData, 0)
                                                      
    except IOError as err:
        print('File Error: ' + str(err))
        
        
#参数单一重复函数
def getRepeatData(file, p_data, url_flag):
    for index, param in enumerate(p_data):
        for i in range(REPEAT_COUNT):
            randMethod()
            if url_flag:
                url = random.choice(gnlib.Match_URL)
            else:
                url = random.choice(gnlib.WebSite_URL)
            data = getTestData(gnlib.getRandTime(), random.choice(gnlib.USR_NBR), url)
            data[index] = param
            file.write(','.join(data) + '\n')
    
if __name__ == '__main__':
    main()
