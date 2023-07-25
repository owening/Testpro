#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Testpro 
@File ：calculator
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2023/7/25 14:26 
'''
from typing import Type

import allure


class Calculator:
    @allure.story()
    def add(self, a, b):
        if a > 99 or a < -99 or b > 99 or b < -99:
            print("请输入范围为【-99, 99】的整数或浮点数")
            return "参数大小超出范围"
        return a + b

    def div(self, a, b):
        if a > 99 or a < -99 or b > 99 or b < -99:
            print("请输入范围为【-99, 99】的整数或浮点数")
            return "参数大小超出范围"

        return a / b





