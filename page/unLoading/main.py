from base.base import Base
from page import unLoading


class PageMain(Base):
    # 点击新建工班
    def page_click_create_shift(self):
        self.click_ele(ID=unLoading.createShiftID)

    # 点击右上角功能按钮
    def page_click_right_function_button(self):
        self.click_ele(ID=unLoading.rightFunctionButtonID)

    # 查看报告
    def page_click_read_report(self):
        self.click_ele(xpath=unLoading.readReportXpath)

    # 马上去新建
    def page_click_to_create(self):
        self.click_ele(ID=unLoading.toCreateID)

    # 添加照片异常按钮
    def page_click_add_abnormal(self):
        self.click_ele(unLoading.addAbnormalID)

    # 输入照片备注
    def page_send_photo_remark(self, remark):
        self.send_key(text=remark, ID=unLoading.addReamrkID)
        self.click_ele(text='确定')

    """船舶概况页面元素"""

    # 选择舱口
    def page_click_vessel_select_hatch(self, hatch):
        self.click_ele(unLoading.hatchSeleteID)
        self.click_ele(text=hatch)

    # 选择舱位
    def page_click_vessel_select_space(self, space):
        self.click_ele(unLoading.spaceSeleteID)
        self.click_ele(text=space)

    # BL选择框
    def page_click_bl_front_select(self, blName):
        self.click_ele(unLoading.blSelectID)
        self.click_ele(text=blName)

    # 件号选择框
    def page_click_detail_front_select(self, detailName):
        self.click_ele(unLoading.detailSelectID)
        self.click_ele(text=detailName)

    def page_send_detail_select(self, detail):
        self.send_key(text=detail, ID=unLoading.detailSelectID)
