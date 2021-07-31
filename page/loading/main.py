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

    # 添加照片异常按钮
    def page_click_add_abnormal(self):
        self.click_ele(loading.addAbnormalID)

    # 输入照片备注
    def page_send_photo_remark(self, remark):
        self.send_key(text=remark, ID=loading.addReamrkID)
        self.click_ele(text='确定')

    """装前货况页面元素"""

    # 装前货况-BL选择框
    def page_click_bl_front_select(self, blName):
        self.click_ele(loading.blSelectID)
        self.click_ele(text=blName)

    # 装前货况-件号选择框
    def page_click_detail_front_select(self, detailName):
        self.click_ele(loading.detailSelectID)
        self.click_ele(text=detailName)

    """船舶概况页面元素"""

    # 选择舱口
    def page_click_vessel_select_hatch(self, hatch):
        self.click_ele(loading.hatchSeleteID)
        self.click_ele(text=hatch)

    # 选择舱位
    def page_click_vessel_select_space(self, space):
        self.click_ele(loading.spaceSeleteID)
        self.click_ele(text=space)
