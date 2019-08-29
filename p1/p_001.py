import allure

class Test_001:
    @allure.step('这是测试步骤001')
    def test_001(self):
        print('---test_001')
        allure.attach('用户名','小明同学')
        allure.attach('密码', '123456')
        assert True