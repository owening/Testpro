#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Testpro 
@File ：test_calculator
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2023/7/25 16:26 
'''

"""
1．完整的测试流程，包含需求分析、测试计划设计、测试用例编写、测试执行、bug 的提交与管理。 
2．使用思维导图完成需求分分析；提供完整测试计划模板，完成测试计划设计；应用多种测试用例设计方法，包括：等价类、边界值、错误推测法等。 
3．测试执行过程中应用多种测试方法完成计算器的加法、除法运算。 
4．结合项目管理工具完成 bug 的提交与管理，进行测试报告编写与项目总结。 
5．编写自动化测试用例，结合 Allure 技术生成测试报告
--------------------------------------------------------------------------------------------------------------------
执行命令
#通过pytest执行用例、并生成allure对应格式的执行结果文件
pytest .\test_calculator.py -s -q --alluredir ./report/result/ --clean-alluredir

#通过allure源文件启动查看allure报告
allure serve .\report\result\

#生成html格式的allure报告
allure generate .\report\result\ -o .\report\html_repopt\ 

#打开查看html格式的allure报告
allure open.\report\html_repopt\
"""

from hogwarts.calculator import Calculator

class TestCalculator():

    def setup(self):
        self.calculator = Calculator()

    def test_add1(self):
        num1,num2,expected = -98, 98, 0
        res = self.calculator.add(num1, num2)
        assert res == expected

    def test_add2(self):
        num1,num2,expected = -99,37.68, -61.32
        res = self.calculator.add(num1, num2)
        assert res == expected

    def test_add3(self):
        num1,num2,expected = 84.06, 99, 183.06
        res = self.calculator.add(num1, num2)
        assert res == expected

    def test_add4(self):
        num1,num2,expected = -100, 26.05, "参数大小超出范围"
        res = self.calculator.add(num1, num2)
        assert res == expected

    def test_add5(self):
        num1,num2,expected = -8, 100, "参数大小超出范围"
        res = self.calculator.add(num1, num2)
        assert res == expected

    def test_add6(self):
        num1,num2,expected = -68.26, 76.03, 7.77
        res = round(self.calculator.add(num1, num2),2)
        assert res == expected

    # #错误数据类型场景
    # def test_add(self):
    #     num1,num2,expected = "test1", "test2", "test3"
    #     res = self.calculator.add(num1, num2)
    #     assert res != expected



    def test_div1(self):
        num1, num2, expected = -98, 98, -1
        res = self.calculator.div(num1, num2)
        assert res == expected

    def test_div2(self):
        num1, num2, expected = -99, 37.68, -2.63
        res = round(self.calculator.div(num1, num2),2)
        assert res == expected

    def test_div3(self):
        num1, num2, expected = 84.06, 99, 0.85
        res = round(self.calculator.div(num1, num2),2)
        assert res == expected

    def test_div4(self):
        num1, num2, expected = -100, 26.05, "参数大小超出范围"
        res = self.calculator.div(num1, num2)
        assert res == expected

    def test_div5(self):
        num1, num2, expected = -8, 100, "参数大小超出范围"
        res = self.calculator.div(num1, num2)
        assert res == expected

    def test_div6(self):
        num1, num2, expected = -68.26, 76.03, -0.9
        res = round(self.calculator.div(num1, num2), 2)
        assert res == expected

    # #错误数据类型场景
    # def test_add(self):
    #     num1,num2,expected = "test1", "test2", "test3"
    #     res = self.calculator.div(num1, num2)
    #     assert res != expected


