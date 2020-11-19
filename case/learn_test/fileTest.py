import csv
# def count_words(filename):
#     try:
#         with open(filename,'r') as file:
#             contents = file.read()
#     except FileNotFoundError:
#         print('sorry!the file ' + filename + ' is not exist!')
#     else:
#         words = contents.split()
#         print('the file ' + filename +  'has about ' + str(len(words)) + ' words!')
#
#
# filenames = ['test_result.txt','11.txt','area_data.txt','pi_digist.txt']
# for filename in filenames:
#     count_words(filename)

# 读取csv某一列（excel风格的）
def openCSV():
    with open('wether.csv','r',encoding='utf-8') as f:
        reader = csv.reader(f)
        print(reader)
        # header_row = next(reader)
        # 定义一个列的空列表
        rows = []
        # 遍历读取数据并添加到rows列表中
        for row in reader:
            rows.append(row[0])
        # 打印整个列的列表
        print(rows)
        # 取列的第一个值
        print(rows[0])

#　读取ＣＳＶ的某一行
def readCSV():
    with open('wether.csv','r',encoding='utf-8') as f:
        csv_read = csv.reader(f)
        rows = []
        # 用枚举的方式给每一行都自动编了一个顺序号，如果i == 0 取第一行
        for i,row in enumerate(csv_read):
            if i == 0:
                rows.append(row)
        print(rows)
        print(rows[0])


def writeCSV():
    with open('wether.csv', 'a+', encoding='utf-8',newline='') as f:
        fwriter = csv.writer(f)
        # 写单行
        fwriter.writerow(['name','jojo'])
        rows = [('banked','amy'),('dog','cat')]
        # 一次写多行
        fwriter.writerows(rows)

#writeCSV()
# openCSV()
readCSV()



