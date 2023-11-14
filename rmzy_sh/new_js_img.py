#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/8/7 15:25
# @Author  : Xzx
# @FileName: new_js_img.py
# @Software: PyCharm
from datetime import datetime


def get_repeat_res(old_file_path, new_file_path):
    cw_num = 0
    count = 0
    old_dataId_list = []
    with open('./'+old_file_path, mode='r', encoding='utf-8') as f1:
        data1 = f1.readlines()
        for i in data1:
            for key in eval(i):
                odl_dataId = eval(i).get(key).get('data').get('contentCheckTask').get('dataId')
                # print(ys_url)
                old_dataId_list.append(odl_dataId)
        print(old_dataId_list)
    review_time_total = 0
    new_dataId_list = []
    with open('./'+new_file_path, mode='r', encoding='utf-8') as f:
        data = f.read()
        # print(type(eval(data)))
        print(len(eval(data)))
        for j in eval(data):
            dataId = j.get('data_id')
            new_dataId_list.append(dataId)
        for k in old_dataId_list:
            if k in new_dataId_list:
                start_time = datetime.strptime(eval(data)[new_dataId_list.index(k)].get('start_time'),"%d/%m/%Y "
                                                                                                      "%H:%M:%S")
                end_time = datetime.strptime(eval(data)[new_dataId_list.index(k)].get('end_time'), "%d/%m/%Y %H:%M:%S")
                diff_time = (end_time - start_time).seconds
                review_time_total += diff_time
                count += 1
                if diff_time > 5:
                    print(old_dataId_list.index(k))
                    print(f'review_time,{diff_time}')
                    cw_num += 1
        print(f'avg_dealy, {review_time_total / count}')
        print(f'cw_num, {cw_num}')
        print(f'count, {count}')


if __name__ == '__main__':
    get_repeat_res(old_file_path='res_img_new.json', new_file_path='res_img_time.json')  # 5s



