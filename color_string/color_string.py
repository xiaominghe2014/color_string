#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@version: 0.0.0
@author: xiaoming
@license: MIT Licence 
@contact: xiaominghe2014@gmail.com
@site: 
@software: PyCharm
@file: color_string.py
@time: 2018/1/15 下午2:40

"""
import itertools

DEFAULT = 'default'
BLACK = 'black'
RED = 'red'
YELLOW_GREEN = 'yellow_green'
YELLOW = 'yellow'
BLUE = 'blue'
PURPLE = 'purple'
GREEN = 'green'
GRAY = 'gray'

TYPE_DEFAULT = 0
TYPE_HIGH_LIGHT = 1
TYPE_UNDERLINE = 4
TYPE_BLINK = 5
TYPE_REVERSE = 7
TYPE_INVISIBLE = 8

FOREGROUND_INDEX = {
    BLACK: 30,
    RED: 31,
    YELLOW_GREEN: 32,
    YELLOW: 33,
    BLUE: 34,
    PURPLE: 35,
    GREEN: 36,
    GRAY: 37
}

BACKGROUND_INDEX = {
    DEFAULT: 1,
    BLACK: 40,
    RED: 41,
    YELLOW_GREEN: 42,
    YELLOW: 43,
    BLUE: 44,
    PURPLE: 45,
    GREEN: 46,
    GRAY: 47
}


class ColorArgumentsTypeError(Exception):
    def __init__(self, err='color_type Error'):
        Exception.__init__(self, err=err)


def check_show_type(show_type):
    show_list = [0, 1, 4, 5, 7, 8]
    if show_type not in show_list:
        raise ColorArgumentsTypeError(err='color_type Error:valid value is 0, 1, 4, 5, 7, 8')


def check_color(color, arg_name):
    colors_list = [DEFAULT, BLACK, RED, YELLOW_GREEN, YELLOW, BLUE, PURPLE, GREEN, GRAY]
    if color not in colors_list:
        raise ColorArgumentsTypeError(err='{0} Error:valid value is '
                                      'black, red, yellow_green, yellow, blue, purple, green, gray'.format(arg_name))


def get_color(src_string, fore_color=RED, back_color=DEFAULT, show_type=0):
    if not fore_color and not back_color and not show_type:
        return src_string
    check_show_type(show_type)
    check_color(fore_color, 'fore_color')
    check_color(back_color, 'back_color')
    color_string_fmt = '\033[{TYPE};{FORE};{BACK}m{SRC}\033[0m'
    type_string = str(show_type)
    fore_string = '{0}'.format(FOREGROUND_INDEX[fore_color])
    back_string = '{0}'.format(BACKGROUND_INDEX[back_color])
    return color_string_fmt.format(TYPE=type_string, FORE=fore_string, BACK=back_string, SRC=src_string)


if __name__ == '__main__':
    color_list_fore = [BLACK, RED, YELLOW_GREEN, YELLOW, BLUE, PURPLE, GREEN, GRAY]
    color_list_back = [DEFAULT, BLACK, RED, YELLOW_GREEN, YELLOW, BLUE, PURPLE, GREEN, GRAY]
    color_type = [0, 1, 4, 5, 7, 8]
    args_list = list(itertools.product(color_list_fore, color_list_back, color_type))
    color_list = list()
    for i in args_list:
        color_list.append(get_color(
            i[0]+'_'+i[1]+'_'+str(i[2]),
            i[0], i[1], i[2]))
    for color in color_list:
        print(color)

