from base.base import Base
from page import loading


class PageMain(Base):
    # 点击新建工班
    def page_click_create_shift(self):
        self.click_ele(ID=loading.createShiftID)

    # 点击右上角功能按钮
    def page_click_right_function_button(self):
        self.click_ele(ID=loading.rightFunctionButtonID)

    # 查看报告
    def page_click_read_report(self):
        self.click_ele(xpath=loading.readReportXpath)

    # 马上去新建
    def page_click_to_create(self):
        self.click_ele(ID=loading.toCreateID)
