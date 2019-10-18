import time


def format_time():
    return time.strftime('%Y%m%d', time.localtime(time.time()))


def format_time1():
    return time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))


def format_time2():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
