import uiautomator2


class Base:

    def __init__(self):
        self.driver = uiautomator2.connect('926QADV7222QM')  # b182d0da,SQRNW17927003213,926QADV7222QM
        self.packageName = 'com.mj.app.marsreport.pre'

    # 获取元素属性ID
    def get_ele(self, ID=None, xpath=None, text=None, description=None, index=0):
        if ID:
            return self.driver(resourceId=ID)[index]
        elif xpath:
            return self.driver.xpath(xpath=xpath)
        elif text:
            return self.driver(text=text)
        elif description:
            return self.driver(description=description)
        elif ID and text:
            return self.driver(ID=ID, text=text)

    # 根据属性ID点击
    def click_ele(self, ID=None, xpath=None, text=None, description=None, index=0):
        if ID:
            print("点击 {}".format(ID))
            self.get_ele(ID=ID, index=index).click()
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
    def exists_ele(self, text):
        print("判断 {}是否存在".format(text))
        return self.driver(text=text).exists(timeout=5)

    # 返回元素文本
    def get_text(self, ID=None, xpath=None):
        print("返回ID={} xpath={}的文本信息".format(ID, xpath))
        return self.get_ele(ID=ID, xpath=xpath).get_text()

    # 重启app
    def restart_app(self):
        self.driver.app_start(self.packageName, stop=True)
        self.click_ele(ID='com.mj.app.marsreport.pre:id/close')

    # 截图
    def get_image(self, filename):
        self.driver.screenshot(filename=filename)
