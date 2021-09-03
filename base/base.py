import time
import uiautomator2


class Base:

    def __init__(self):
        self.driver = uiautomator2.connect('926QADV7222QM')  # b182d0da,SQRNW17927003213,926QADV7222QM
        # self.driver = uiautomator2.connect_adb_wifi('192.168.1.227')  # viVo：192.168.1.164 华为：192.168.1.227

    # 循环查找ID元素5次，没有找到向下滑动，找到后点击
    def click_ele_ID(self, ID, index=0):
        try:
            i = 0
            while i < 5:
                i += 1
                if self.exists_ele_ID(ID=ID):
                    print('点击{}'.format(ID))
                    self.driver(resourceId=ID)[index].click()
                    break
                else:
                    print('下滑查找')
                    self.driver.swipe_ext('up', 0.5)
        except Exception as e:
            print(e)

    # 循环查找xpath元素5次，没有找到向下滑动，找到后点击
    def click_ele_xpath(self, xpath, index=0):
        try:
            i = 0
            while i < 5:
                i += 1
                if self.exists_ele_xpath(xpath=xpath):
                    print('点击{}'.format(xpath))
                    self.driver(xpath=xpath)[index].click()
                    break
                else:
                    print('下滑查找')
                    self.driver.swipe_ext('up', 0.5)
        except Exception as e:
            print(e)

    # 循环查找text元素5次，没有找到向下滑动，找到后点击
    def click_ele_text(self, text, index=0):
        try:
            i = 0
            while i < 5:
                i += 1
                if self.exists_ele_text(text=text):
                    print('点击{}'.format(text))
                    self.driver(text=text)[index].click()
                    break
                else:
                    print('下滑查找')
                    self.driver.swipe_ext('up', 0.5)
        except Exception as e:
            print(e)

    # 循环查找description元素5次，没有找到向下滑动，找到后点击
    def click_ele_description(self, description, index=0):
        try:
            i = 0
            while i < 5:
                i += 1
                if self.exists_ele_description(description):
                    self.driver(description=description)[index].click()
                    break
                else:
                    print('下滑查找')
                    self.driver.swipe_ext('up', 0.5)
        except Exception as e:
            print(e)

    # 根据坐标点击
    def click_xy(self, x, y):
        print("点击坐标 {} {}".format(x, y))
        self.driver.click(x, y)

    # 根据ID输入方法
    def send_key_ID(self, text, ID, index=0):
        self.click_ele_ID(ID, index)
        self.driver.clear_text()
        print('输入{}'.format(text))
        self.driver(resourceId=ID).send_keys(text=text)

    # 判断text元素是否存在 返回bool
    def exists_ele_text(self, text):
        print("判断 {}是否存在".format(text))
        return self.driver(text=text).exists(timeout=5)

    # 判断ID元素是否存在 返回bool
    def exists_ele_ID(self, ID):
        print("判断 {}是否存在".format(ID))
        return self.driver(resourceId=ID).exists(timeout=5)

    # 判断description元素是否存在 返回bool
    def exists_ele_description(self, description):
        print("判断 {}是否存在".format(description))
        return self.driver(description=description).exists(timeout=5)

    # 判断xpath元素是否存在 返回bool
    def exists_ele_xpath(self, xpath):
        print("判断 {}是否存在".format(xpath))
        return self.driver(xpath=xpath).exists(timeout=5)

    # 返回元素文本
    def get_text_ID(self, ID=None, index=0):
        print("返回ID={}的文本信息".format(ID))
        return self.driver(resourceId=ID)[index].get_text()

    # 重启app
    def restart_app(self, packageName):
        time.sleep(1)
        print('重启app')
        self.driver.app_start(package_name=packageName, stop=True)
        time.sleep(2)

    # 获取toast信息
    def get_toast(self):
        return self.driver.toast.get_message()

    # 长按某个点
    def long_click(self, x, y):
        time.sleep(1)
        self.driver.long_click(x, y, duration=1)

    def click_back(self):
        time.sleep(1)
        self.driver.press('back')
