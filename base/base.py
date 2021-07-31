import time
import uiautomator2


class Base:

    def __init__(self):
        self.driver = uiautomator2.connect('926QADV7222QM')  # b182d0da,SQRNW17927003213,926QADV7222QM
        self.driver.debug = False
        self.packageName = 'com.mj.app.marsreport.pre'
    # 获取元素属性ID
    def get_ele(self, ID=None, xpath=None, text=None, index=0):
        if ID:
            return self.driver(resourceId=ID)[index]
        elif xpath:
            return self.driver.xpath(xpath=xpath)
        elif text:
            return self.driver(text=text)
        elif ID and text:
            return self.driver(ID=ID, text=text)

    # 根据属性ID点击
    def click_ele(self, ID=None, xpath=None, text=None, index=0):
        if ID:
            self.get_ele(ID=ID, index=index).click()
        elif xpath:
            self.get_ele(xpath=xpath).click()
        elif text:
            self.get_ele(text=text, index=index).click()
        elif ID and text:
            self.get_ele(ID=ID, text=text, index=index).click()

    # 根据坐标点击
    def click_xy(self, x, y):
        self.driver.click(x, y)

    # 输入方法
    def send_key(self, text, ID=None, xpath=None):
        self.click_ele(ID=ID, xpath=xpath)
        self.driver.clear_text()
        self.get_ele(ID).send_keys(text)

    # 判断元素是否存在 返回bool
    def exists_ele(self, ID=None, xpath=None, text=None):
        return self.get_ele(ID=ID, xpath=xpath, text=text).exists(timeout=5)

    # 返回元素文本
    def get_text(self, ID=None, xpath=None):
        return self.get_ele(ID=ID, xpath=xpath).get_text()

    # 重启app
    def restart_app(self):
        self.driver.app_stop(self.packageName)
        time.sleep(1)
        self.driver.app_start(self.packageName)
        self.click_ele(ID='com.mj.app.marsreport.pre:id/close')

    # 截图
    def get_image(self, filename):
        self.driver.screenshot(filename=filename)
