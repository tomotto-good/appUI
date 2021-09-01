import time

import uiautomator2


class Base:

    def __init__(self):
        # self.driver = uiautomator2.connect('926QADV7222QM')  # b182d0da,SQRNW17927003213,926QADV7222QM
        self.driver = uiautomator2.connect_adb_wifi('192.168.1.227')  # viVo：192.168.1.164 华为：192.168.1.227
        self.driver.implicitly_wait(5)

    # 获取元素属性
    def get_ele(self, ID=None, xpath=None, text=None, description=None, index=0):
        while True:
            if ID:
                return self.driver(resourceId=ID)[index]
            elif xpath:
                return self.driver.xpath(xpath=xpath)
            elif description:
                return self.driver(description=description)
            elif ID and text:
                return self.driver(ID=ID, text=text)
            elif self.exists_ele_text(text=text):
                return self.driver(text=text)
            else:
                self.driver.swipe_ext('up', 0.5)

    # 获取元素属性ID
    def get_ele_id(self, ID, index=0):
        try:
            i = 0
            while i < 5:
                i += 1
                if self.exists_ele_resourceId(ID=ID):
                    return self.driver(resourceId=ID)[index]
                else:
                    self.driver.swipe_ext('up', 0.5)
        except Exception as e:
            print(e)

    # 根据属性ID点击
    def click_ele(self, ID=None, xpath=None, text=None, description=None, index=0):
        if ID:
            print("点击 {}".format(ID))
            self.get_ele_id(ID=ID, index=index).click()
        elif xpath:
            print("点击 {}".format(xpath))
            self.get_ele(xpath=xpath).click()
        elif text:
            print("点击 {}".format(text))
            self.get_ele(text=text, index=index).click()
        elif description:
            print("点击 {}".format(description))
            self.get_ele(description=description).click()
        elif ID and text:
            self.get_ele(ID=ID, text=text, index=index).click()

    # 根据坐标点击
    def click_xy(self, x, y):
        print("点击坐标 {} {}".format(x, y))
        self.driver.click(x, y)

    # 输入方法
    def send_key(self, text, ID=None, xpath=None):
        print("点击 ID={} Xpath={} 输入:{}".format(ID, xpath, text))
        self.click_ele(ID=ID, xpath=xpath)
        self.driver.clear_text()
        self.get_ele(ID).send_keys(text=text)

    # 判断元素是否存在 返回bool
    def exists_ele_text(self, text):
        print("判断 {}是否存在".format(text))
        return self.driver(text=text).exists(timeout=3)

    # 判断元素是否存在 返回bool
    def exists_ele_resourceId(self, ID):
        print("判断 {}是否存在".format(ID))
        return self.driver(resourceId=ID).exists(timeout=5)

    # 返回元素文本
    def get_text(self, ID=None, xpath=None, index=0):
        print("返回ID={} xpath={}的文本信息".format(ID, xpath))
        return self.get_ele(ID=ID, xpath=xpath, index=index).get_text()

    # 重启app
    def restart_app(self, packageName):
        time.sleep(1)
        self.driver.app_start(package_name=packageName, stop=True)
        time.sleep(2)

    # 长按某个点
    def long_click(self, x, y):
        time.sleep(1)
        self.driver.long_click(x, y, duration=1)
