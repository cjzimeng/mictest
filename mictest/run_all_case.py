import pytest
import os
if __name__ == '__main__':
    #生成report的报告数据
    pytest.main(['./test_case', '--alluredir', './report/reportdata'])
    #shell = Shell.Shell()
    #print(type(os.system('pip list | findstr allure')))
    #os.system('pip list | findstr allure')

    #将生成的报告数据生成allure报告
    os.system('allure generate ./report/reportdata -o ./report/allure-report --clean')



