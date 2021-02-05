# -*- coding: utf-8 -*-
# @Time : 2021/2/5 9:08 下午
# @Author : Qi Tianyue
# @Github : Orange-66
# @PROJECT : LAPS 
# @File : tool_time.py
# @Remark : 控制时间的工具类
# -----------------------------
import datetime


def current_date():
    result = datetime.datetime.now().strftime('%Y/%m/%d')
    # print(result)
    return result


def current_time_without_second():
    result = datetime.datetime.now().strftime('%H:%M')
    # print(result)
    return result


def current_time_with_second():
    result = datetime.datetime.now().strftime('%H:%M:%S')
    # print(result)
    return result


def current_datetime():
    result = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    # print(result)
    return result


if __name__ == "__main__":
    current_date()
    current_time_with_second()
    current_time_without_second()
    current_datetime()