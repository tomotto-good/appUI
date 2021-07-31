from base.base import Base
from page import login


class PageLogin(Base):
    def page_login(self):
        """密码登录"""
        # 输入用户名
        self.send_key(ID=login.phoneID, text='18217484395')
        # 点击密码登录
        self.click_ele(ID=login.pwdLoginID)
        # 输入密码
        self.send_key(ID=login.pwdInputId, text='123456')
        # 点击登录
        self.click_ele(ID=login.loginId)

    def page_judge_login(self):
        """"判断当前是否在登陆页面"""
        if self.get_ele(ID=login.pwdLoginID).exists(timeout=5):
            self.page_login()
        else:
            print('当前用户已登录，请执行用例')

