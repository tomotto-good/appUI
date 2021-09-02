import time

from base.base import Base
from page import home


class PageHome(Base):
    # 点击任务按钮
    def page_click_task_button(self):
        self.click_ele_ID(ID=home.taskId)

    # 点击消息列表
    def page_click_message_title(self):
        self.click_ele_ID(ID=home.messageTitle)

    # 点击加号
    def page_click_menu(self):
        self.click_ele_ID(ID=home.menuButtonID)

    # 选择文件
    def page_select_file(self):
        self.click_ele_text(text='文件')
        time.sleep(2)
        try:
            result = self.driver.exists(text='1626849874506.jpg')
            if result:
                self.click_ele_text(text='1626849874506.jpg')
            else:
                self.click_ele_description(description="显示根目录")
                self.click_ele_text(text='图片')
                self.click_ele_text(text='Pictures')
                self.click_ele_text(text='1626849874506.jpg')
        except Exception as e:
            print(e)
