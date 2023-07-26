#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Testpro 
@File ：test_calculator
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2023/7/25 16:26 
'''
import sys

import pytest

"""
    1.完整的测试流程，包含需求分析、测试计划设计、测试用例编写、测试执行、bug 的提交与管理。
    2.使用思维导图完成需求分分析；提供完整测试计划模板，完成测试计划设计；应用多种测试用例设计方法，包括：等价类、边界值、错误推测法等。
    3.测试执行过程中应用多种测试方法完成计算器的加法、除法运算。
    4.结合项目管理工具完成 bug 的提交与管理，进行测试报告编写与项目总结。
    5.编写自动化测试用例，结合 Allure 细化测试报告，比如添加用例标题与用例步骤。
    6.使用参数化减少代码量，提高代码的可维护性。
    7.使用 mark 标签为测试用例分类
    8.设置跳过、预期失败用例
    9.对异常用例进行处理
    --------------------------------------------------------------------------------------------------------------------
    执行命令
    #通过pytest执行用例、并生成allure对应格式的执行结果文件
    pytest .\test_calculator.py -vs --alluredir ./report/result/ --clean-alluredir
    
    #通过allure源文件启动查看allure报告
    allure serve .\report\result\
    
    #生成html格式的allure报告
    allure generate .\report\result\ -o .\report\html_repopt\ 
    
    #打开查看html格式的allure报告
    allure open.\report\html_repopt\
"""

from hogwarts.calculator import Calculator

test_add_data = [(-98, 98, 0), (-99, 37.68, -61.32), (84.06, 99, 183.06),
                 (-100, 26.05, "参数大小超出范围"), (-8, 100, "参数大小超出范围"), (-68.26, 76.03, 7.77), (-98.51, -68.06, -166.57)]

test_div_data = [(-98, 98, -1), (-99, 37.68, -2.63), (84.06, 99, 0.85),
                 (-100, 26.05, "参数大小超出范围"), (-8, 100, "参数大小超出范围"), (-68.26, 76.03, -0.9), (-98.51, -68.06, 1.45)]


class TestCalculator():

    def setup_class(self):
        self.calculator = Calculator()

    @pytest.mark.skipif(sys.platform != "win32", reason="在win32上跳过，不执行")  #带条件，满足条件时跳过用例
    @pytest.mark.addtest   #自定义测试用例分类标签， pytest.mark.自定义标签名
    @pytest.mark.parametrize("num1,num2,expected", test_add_data,
                             ids=["-98+98=0", "-99+37.68=61.32", "84.06+99=183.06", "-100+26.05=参数超出范围",
                                  "-8+100=参数超出范围",
                                  "-68.26+76.03=7.77", "-99.51+(-68.06)=-167.57"])
    def test_add1(self, num1, num2, expected):
        res = self.calculator.add(num1, num2)
        if type(res) == float:
            res = round(res, 2)
        assert res == expected

    # #错误数据类型场景
    @pytest.mark.xfail(raises=TypeError,reason="这是预期失败原因描述")  #标记为预期失败用例
    @pytest.mark.testfail
    @pytest.mark.parametrize("num1,num2,expected", [["test1", "test2", "test3"]])
    def test_exc_add(self, num1, num2, expected):
        #预期指定异常时进行捕获后继续执行后续代码
        with pytest.raises(TypeError):
            res = self.calculator.add(num1, num2)
            print("打印：", res)
            assert res != expected



    @pytest.mark.skip(reason="无条件直接跳过该用例，这是跳过原因描述")  #无条件，直接跳过用例
    @pytest.mark.divtest
    @pytest.mark.parametrize("num1,num2,expected", test_div_data,
                             ids=["-98/98=-1", "-99/37.68=-2.63", "84.06/99=0.85", "-100/26.05=参数超出范围", "-8/100=参数超出范围",
                                  "-68.26/76.03=-0.9", "-99.51/(-68.06)=1.45"])
    def test_div1(self, num1, num2, expected):
        res = self.calculator.div(num1, num2)
        if type(res) == float:
            res = round(res, 2)
        assert res == expected

# #错误数据类型场景
# def test_add(self):
#     num1,num2,expected = "test1", "test2", "test3"
#     res = self.calculator.div(num1, num2)
#     assert res != expected
