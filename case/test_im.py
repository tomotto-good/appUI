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
        """验证图片格式的文件是否正常打开"""
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
            if self.home.driver.exists(resourceId='com.mj.app.marsreport.pre:id/imageView'):
                print('---pass---')
            else:
                print("---fail---")
        except Exception as e:
            print(e)

    def test_im_002(self):
        """验证点击推送到IM的系统通知可以正常跳转到H5"""

    def test_im_003(self):
        """"""
