
import csv

with open('assets.csv', 'a', newline='') as csvfile:

#调用open()函数打开csv文件，传入参数：文件名“assets.csv”，、追加模式“a”、newline=''。

    writer = csv.writer(csvfile, dialect='excel')

    # 用csv.writer()函数创建一个writer对象。

    header = ['小区名称','地址', '建筑时间','楼栋', '单元',  '门牌', '朝向', '面积']

    # 用writerow()函数将表头写进csv文件