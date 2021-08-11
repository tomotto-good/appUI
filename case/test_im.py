import time
import unittest
from page.home.home import PageHome


class TestIM(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('导入home文件..')
        cls.home = PageHome()

    def tearDown(self) -> None:
        self.home.restart_app()

    def test_im_001(self):
        """验证图片格式的文件正常打开"""
        try:
            print("1.进入消息列表")
            self.home.page_click_message_title()
            print("2.下拉刷新")
            time.sleep(1)
            self.home.driver.swipe_ext('down', 1)
            print("3.进入uiCollection任务")
            self.home.click_ele(text='uiCollection')
            print('4.点击加号')
            self.home.page_click_menu()
            print("5.选择文件")
            self.home.page_select_file()
            print("6.打开文件")
            self.home.click_ele(text='1626849874506.jpg', ID='com.mj.app.marsreport.pre:id/file_name_right')
            print('---断言')
            time.sleep(2)
            self.assertTrue(self.home.exists_ele_resourceId(ID='com.mj.app.marsreport.pre:id/imageView'))
        except Exception as e:
            raise e

    def test_im_002(self):
        """验证点击推送到IM的系统通知可以正常跳转到H5"""
        try:
            print("1.进入消息列表")
            self.home.page_click_message_title()
            print("2.下拉刷新")
            time.sleep(1)
            self.home.driver.swipe_ext('down', 1)
            print("3.进入uiCollection任务")
            self.home.click_ele(text='uiCollection')
            print("4.点击显示更多信息进入H5")
            while True:
                if self.home.exists_ele_text(text='显示更多信息'):
                    self.home.click_ele(text='显示更多信息')
                    break
                else:
                    self.home.driver.swipe_ext('down', 0.5)
            print("---断言")
            self.assertTrue(self.home.exists_ele_resourceId(ID='com.mj.app.marsreport.pre:id/webView'))
        except Exception as e:
            raise e
