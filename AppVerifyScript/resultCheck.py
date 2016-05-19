#-*- coding:utf-8 -*-
import os
import reslib

MISMATCH = 0
OUT = 1
INVALID = 2

OUT_CASE = ['APP_011.txt', 'APP_003.txt', 'APP_006.txt', 'APP_007.txt']
MISMATCH_CASE = ['APP_001.txt', 'APP_002.txt', 'APP_012.txt']
INVALID_CASE = ['APP_004.txt', 'APP_005.txt', 'APP_008.txt', 'APP_009.txt', 'APP_010.txt', 
                'APP_018.txt', 'APP_019.txt']

def createReport():
    '''创建结果报告文件'''
    if os.path.exists(os.getcwd() + '/report.txt'):
        os.remove(os.getcwd() + '/report.txt')

def readLines(file, index):
    '''返回指定行数据'''
    file.seek(0)
    line = ''
    for i in range(index):      
        line = file.readline()
    return line

def verificationResults(sourceData, flag):
    '''
    结果验证函数
    sourceData：测试数据源文件
    flag：数据分类标识位-MISMATCH、OUT、INVALID
    '''
    try:
        with open(os.getcwd()+'/testdatas/' + sourceData, 'r', encoding = 'utf-8') as s_file, \
             open(os.getcwd() + '/report.txt', 'a') as report_file:
                      
            s_lines = s_file.readlines()
            # 不匹配的输出结果
            if MISMATCH == flag:
                resultData = reslib.getResults(flag)         
                for index, s_line in enumerate(s_lines):
                    s_line = s_line.split('@#$')
                    if len(s_line) > 1:
                        # 去掉多余参数
                        s_line.pop(1)
                        # 取前三个参数
                        # 如果源数据在结果文件，则满足预期；否则写入到结果文件
                        if s_line[:3] in resultData:
                            print('Right data - {file_name}\'s Data {line}'.format(file_name = sourceData, line = index))
                        else:
                            if(index == 1):
                                report_file.write('Data case:  --------  {data}'.format(data = readLines(s_file, index))) 
                            report_file.write('Data not in result - {file_name}\'s data {line}: {data}'.format( \
                                file_name = os.path.splitext(sourceData)[0], line = index, data = readLines(s_file, index+1)))
            # 匹配规则库的输出结果
            elif OUT == flag:
                resultData = reslib.getResults(flag)

                for index, s_line in enumerate(s_lines):
                    temp = s_line.split('@#$')
                    if len(temp) > 1:
                        s_list = []
                        s_list.append(temp[0])
                        s_list.append(temp[7])
                        s_list.append(temp[13])
                        s_list.append(temp[14])
                        s_list.append(temp[4])
                        s_list.append(temp[5])
                        s_list.append(temp[6])                  
                        s_list.append(temp[2])
                        s_list.append(temp[3])
            
                        if s_list in resultData:                    
                            print('Right data - {file_name}\'s Data {line}'.format(file_name = sourceData, line = index))
                        else:
                            if(index == 1):
                                report_file.write('Data case:  --------  {data}'.format(data = readLines(s_file, index))) 
                            report_file.write('Data not in result - {file_name}\'s data {line}: {data}'.format( \
                                file_name = os.path.splitext(sourceData)[0], line = index, data = readLines(s_file, index+1)))

            # 非法结果              
            else:
                resultData = reslib.getResults(INVALID)
                for index, s_line in enumerate(s_lines):
                    
                    if s_line in resultData:                        
                        print('Right data - {file_name}\'s Data {line}'.format(file_name = sourceData, line = index))
                    else:
                        if index == 0:
                            report_file.write('Data case:  --------  {data}'.format(data = readLines(s_file, index+1)))
                        else:
                            report_file.write('Data not in result - {file_name}\'s data {line}: {data}'.format( \
                                file_name = os.path.splitext(sourceData)[0], line = index, data = readLines(s_file, index+1)))
            # 日志输出
            print('Verification end.\n')
            report_file.write('\n')
    except IOError as err:
        print('File Error: {error}'.format(error = str(err)))

def main():
    '''将不同场景的输入数据，与对应的预期结果进行对比；
    若不在结果中，则将源数据写入到结果报告文件report.txt中。
    '''
    createReport()
    filePath = os.getcwd() + '/testdatas/'
    try:
        for root, dirs, files in os.walk(filePath):
            # 遍历文件，根据不同预期匹配不同结果
            for file in files:
                print(file + ' verifying...')
                if file in MISMATCH_CASE:
                    verificationResults(file, MISMATCH)
                elif file in OUT_CASE:
                    verificationResults(file, OUT)
                else:
                    verificationResults(file, INVALID)
        print('All file verified.')
    except IOError as err:
        print('File Error: {error}'.format(error = str(err)))
    
if __name__ == '__main__':
    main()


    
