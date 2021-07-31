from base.base import Base
from page import foot


class DetailList(Base):
    """明细详情页"""

    def page_detail_add_length_width_height(self):
        # 长度加10mm
        self.click_ele(ID=foot.lengthID)

        # 宽度加10mm
        self.click_ele(ID=foot.widthID)

        # 高度加10mm
        self.click_ele(ID=foot.heightID)

    # 输入场地
    def page_detail_input_address(self, address):
        self.send_key(ID=foot.addressID, text=address)

    # 确定按钮
    def page_detail_ok_button(self):
        self.click_ele(text='确定')

    # 下载为excel
    def page_click_download_excel(self):
        self.click_ele(xpath=foot.downLoadingExcelXpath)

    """明细列表页"""

    # 点击批量打尺
    def page_detail_click_batch_foot(self):
        self.click_ele(text='批量打尺')

    # 获取日报名称
    def page_detail_get_report_name(self):
        return self.get_text(ID=foot.reportNameID)
