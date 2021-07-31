# coding: utf-8
import uiautomator2 as u2
from page.foot.detailList import DetailList
import time


def take_photos():
    """无限拍照"""
    try:
        d = u2.connect("926QADV7222QM")

        while 1 < 2:
            d(text="拍照").click()
            index = 0
            while index < 20:
                index += 1
                d(resourceId="com.mj.app.marsreport.test:id/whiteBottom").click()
                print("剩余次数：{}".format(20 - index))
                time.sleep(1.5)
    except Exception as e:
        print(e)


take_photos()
