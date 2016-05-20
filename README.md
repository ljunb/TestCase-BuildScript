## TestCase-BuildScript
这份脚本是本人之前从事测试工作时，协助同事测试公司某大数据项目而编写的，基于Python3.4实现，涉及的技术点主要是文件读写，当时水平也有限，权且实现了功能。
## 脚本内容
脚本分为两部分：
>* 生成测试用例
>* 测试结果校验

## 生成测试用例
用例生成部分，主要是先读取项目部提供的已收集的个别数据，然后再根据业务场景（即用例）进行参数的随机组合，如有特殊场景，再做进一步的代码处理。比如其中一个用例场景：
```
    ...
1 #用例008：分隔符错误（任一分隔符）
2 data_008 = []
3 tempdata_008 = getTestData(applib.IP_PORT[randDictKey][0], applib.IP_PORT[randDictKey][1])
4 rchar = ['@#$' for i in range(15)]
5 rchar[random.randrange(0, 15)] = random.choice(['@#', '@', '#', '$', '#$', '@$', ','])                
6 for param, char in zip(tempdata_008, rchar):
     data_008.append(param + char)
7 output_008.write(''.join(data_008) + '\n')
    ...
```
在该例子中：
>* 第3行中getTestData返回随机组合的参数数组
>* 第4行生成一个拥有多个连接符的数组，并在第5行中，采用random.randrange(0, n)获得随机下标，再将rchar数组中某个值赋值为random.choice()随机选中的连接符，达到生成“任一分隔符错误”的业务场景用例
>* 第6行进行参数与连接符的连接，保存到data_008数组中，在第7行中将数组连接成字符串，再写入到文件中

测试数据的生成，基本都是按照以上思路实现，可在脚本中查看。

## 测试结果校验
每个测试数据的输入，必定有对应的结果输出，而且是唯一的。举例来说，每个测试数据文件对应一个业务场景，每个场景中有多条测试数据；将多个测试数据文件进行分类，分别对应输出结果合法、非法和不匹配这3种结果：
```
    ...
VALID_CASE = ['APP_011.txt', 'APP_003.txt', 'APP_006.txt', 'APP_007.txt']
INVALID_CASE = ['APP_004.txt', 'APP_005.txt', 'APP_008.txt', 'APP_009.txt', 'APP_010.txt', 
'APP_018.txt', 'APP_019.txt']
MISMATCH_CASE = ['APP_001.txt', 'APP_002.txt', 'APP_012.txt']
    ...
```
通过遍历同目录下的这些文件，再判断文件属于哪种类型测试数据，然后跟对应的系统输出结果进一步校验，如果发现测试数据记录刚好存在于输出结果记录中，即可判断用例执行成功，否则将该测试数据写入到另一文件中（执行失败结果收集文件）。代码类似于：
```
    ...
filePath = os.getcwd() + '/testdatas/'
try:
    for root, dirs, files in os.walk(filePath):
        # 遍历文件，根据不同预期匹配不同结果
        for file in files:
            print(file + ' verifying...')
            if file in MISMATCH_CASE:
                verificationResults(file, MISMATCH)
            elif file in VALID_CASE:
                verificationResults(file, VALID)
            else:
                verificationResults(file, INVALID)
    print('All file verified.')
except IOError as err:
    print('File Error: {error}'.format(error = str(err)))
    ...
```
## 最后
转眼离开测试行业已接近1年，该仓库无其他目的，纯粹作为当时工作成果的一个代码托管。其实当时在尝试用脚本将这些数据文件上传到服务器，执行测试后再下载到本地，然后再执行结果校验，实现全程自动化。设想挺好，由于项目服务器问题，未能进一步实现，有点遗憾。这份脚本如能帮到其他测试人员，也算是好事。代码质量不敢保证，大牛勿介意。