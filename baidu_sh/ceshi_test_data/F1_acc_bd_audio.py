#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/7/27 10:42
# @Author  : Xzx
# @FileName: F1_acc_bd_audio.py
# @Software: PyCharm
def f1_acc():
    tp, fn, tn, fp = 0, 0, 0, 0
    with open('../ceshi_test_data/result_short_audio.json', mode='r', encoding='utf-8') as f:
        data = f.readlines()
        for dict_data in data:
            for i in eval(dict_data):
                if 'bwg' in i and eval(dict_data).get(i).get('conclusion') == '合规':
                    # tp += 1
                    tn += 1
                elif 'bwg' in i and eval(dict_data).get(i).get('conclusion') != '合规':
                    # fn += 1
                    fp += 1
                elif 'wg' in i and eval(dict_data).get(i).get('conclusion') != '不合规':
                    # fp += 1
                    fn += 1
                elif 'wg' in i and eval(dict_data).get(i).get('conclusion') == '不合规':
                    # tn += 1
                    tp += 1
    P = tp / (tp + fp)
    R = tp / (tp + fn)
    F1 = (2 * P * R) / (P + R)
    acc = (tp + tn) / len(data)
    print(f'tp:{tp}, fn:{fn}, fp:{fp}, tn:{tn}')
    print(f'P:{P}, R:{R}')
    print(f'F1为:{F1},acc为:{acc}')


if __name__ == '__main__':
    f1_acc()
