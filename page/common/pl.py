from base.base import Base
from page import common


class PL(Base):
    """新增/编辑PL页面"""

    # 输入件毛体
    def page_pl_send_data(self, number, volume, weight):
        self.send_key(text=number, ID=common.numberID)
        self.send_key(text=volume, ID=common.volumeID)
        self.send_key(text=weight, ID=common.weightID)

    # 点击PL名称进入明细列表
    def page_pl_click_pl_name(self, plName):
        self.click_ele(text=plName)

    # 点击清单小球
    def page_pl_click_pl_ball(self, index=0):
        self.click_ele(ID=common.plBallID, index=index)

    # pl右上角功能按钮
    def page_pl_click_pl_right_button(self, index=0):
        self.click_ele(ID=common.plRightButtonID, index=index)

    # 删除模板按钮
    def page_pl_click_del_pl(self):
        self.click_ele(xpath=common.plDelXpath)

    # 新增模板按钮
    def page_pl_click_create(self):
        self.click_ele(ID=common.plCreateID)

    # 输入提单号
    def page_pl_send_pl_number(self, plNumber):
        self.send_key(text=plNumber, ID=common.plNumberID)

    # 点击“选择文件”
    def page_pl_click_select_file(self):
        self.click_ele(ID=common.plSelectFileID)

    # 点击编辑按钮
    def page_pl_click_edit(self):
        self.click_ele(xpath=common.editXpath)


