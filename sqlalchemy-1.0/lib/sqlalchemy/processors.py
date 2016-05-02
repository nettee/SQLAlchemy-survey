# sqlalchemy/processors.py
# Copyright (C) 2010-2016 the SQLAlchemy authors and contributors
# <see AUTHORS file>
# Copyright (C) 2010 Gaetan de Menten gdementen@gmail.com
#
# This module is part of SQLAlchemy and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

"""defines generic type conversion functions, as used in bind and result
processors.

They all share one common characteristic: None is passed through unchanged.

"""

#里面说定义了什么类的类型转换函数，在bind和result处理过程中使用

import codecs
import re
import datetime
from . import util


def str_to_datetime_processor_factory(regexp, type_):
    rmatch = regexp.match #正则表达式？
    # Even on python2.6 datetime.strptime is both slower than this code
    # and it does not support microseconds.
    #甚至python2.6的datetime.strptime都比这个代码慢，并且它不支持微秒
    has_named_groups = bool(regexp.groupindex)

    def process(value): #定义了个函数，返回的就是这个函数传入一个变量
        if value is None: #变量为空，就返回空
            return None
        else:
            try:
                m = rmatch(value) #刚才那个正则表达式在这里match
            except TypeError: #正则表达式匹配这个value，（看来是字符串了？）
                raise ValueError("Couldn't parse %s string '%r' "
                                 "- value is not a string." %
                                 (type_.__name__, value))
            if m is None:
                raise ValueError("Couldn't parse %s string: "
                                 "'%s'" % (type_.__name__, value))
            if has_named_groups: #如果正则表达式模式中有命名的分组
                groups = m.groupdict(0) #取第一个命名组？
                return type_(**dict(list(zip( #type_是传进的参数，估计是一个类型，这是强制转换？
                    iter(groups.keys()),
                    list(map(int, iter(groups.values())))
                ))))
            else:
                return type_(*list(map(int, m.groups(0))))
                #看了下调用，将字符串转换为date.datetime,date.time,date.date类型
    return process


def boolean_to_int(value):
    if value is None:
        return None
    else:
        return int(value)


def py_fallback(): #返回局部变量字典,可通过这个函数访问它里面定义的函数？
    def to_unicode_processor_factory(encoding, errors=None):
        decoder = codecs.getdecoder(encoding)

        def process(value):
            if value is None:
                return None
            else:
                # decoder returns a tuple: (value, len). Simply dropping the
                # len part is safe: it is done that way in the normal
                # 'xx'.decode(encoding) code path.
                return decoder(value, errors)[0]
        return process

    def to_conditional_unicode_processor_factory(encoding, errors=None):
        decoder = codecs.getdecoder(encoding)

        def process(value):
            if value is None:
                return None
            elif isinstance(value, util.text_type):
                return value
            else:
                # decoder returns a tuple: (value, len). Simply dropping the
                # len part is safe: it is done that way in the normal
                # 'xx'.decode(encoding) code path.
                return decoder(value, errors)[0]
        return process

    def to_decimal_processor_factory(target_class, scale):
        fstring = "%%.%df" % scale

        def process(value):
            if value is None:
                return None
            else:
                return target_class(fstring % value)
        return process

    def to_float(value):
        if value is None:
            return None
        else:
            return float(value)

    def to_str(value):
        if value is None:
            return None
        else:
            return str(value)

    def int_to_boolean(value):
        if value is None:
            return None
        else:
            return value and True or False

    DATETIME_RE = re.compile(
        "(\d+)-(\d+)-(\d+) (\d+):(\d+):(\d+)(?:\.(\d+))?")
    TIME_RE = re.compile("(\d+):(\d+):(\d+)(?:\.(\d+))?")
    DATE_RE = re.compile("(\d+)-(\d+)-(\d+)")
    #
    str_to_datetime = str_to_datetime_processor_factory(DATETIME_RE,
                                                        datetime.datetime)
    str_to_time = str_to_datetime_processor_factory(TIME_RE, datetime.time)
    str_to_date = str_to_datetime_processor_factory(DATE_RE, datetime.date)
    return locals()

try:
    from sqlalchemy.cprocessors import UnicodeResultProcessor, \
        DecimalResultProcessor, \
        to_float, to_str, int_to_boolean, \
        str_to_datetime, str_to_time, \
        str_to_date

    def to_unicode_processor_factory(encoding, errors=None):
        if errors is not None:
            return UnicodeResultProcessor(encoding, errors).process
        else:
            return UnicodeResultProcessor(encoding).process

    def to_conditional_unicode_processor_factory(encoding, errors=None):
        if errors is not None:
            return UnicodeResultProcessor(encoding, errors).conditional_process
        else:
            return UnicodeResultProcessor(encoding).conditional_process

    def to_decimal_processor_factory(target_class, scale):
        # Note that the scale argument is not taken into account for integer
        # values in the C implementation while it is in the Python one.
        # For example, the Python implementation might return
        # Decimal('5.00000') whereas the C implementation will
        # return Decimal('5'). These are equivalent of course.
        return DecimalResultProcessor(target_class, "%%.%df" % scale).process

except ImportError:
    globals().update(py_fallback())
