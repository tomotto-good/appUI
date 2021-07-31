from base.base import Base
from page import collection


class DetailList(Base):
    """明细列表页面"""

    """明细详情页面"""

    # 输入场地
    def page_send_address(self, address):
        self.send_key(text=address, ID=collection.addressID)

    # 输入车牌号
    def page_send_plate_number(self, plate):
        self.send_key(text=plate, ID=collection.plateID)

    # 点击保存按钮
    def page_click_save_button(self):
        self.click_ele(ID=collection.saveButtonID)

    # 下载为excel
    def page_click_download_excel(self):
        self.click_ele(xpath=collection.downloadExcelXpath)

    """批量集港页面"""

    # 输入场地
    def page_send_batch_address(self, address):
        self.send_key(text=address, ID=collection.batchAddressID)

    # 输入车牌号
    def page_send_batch_plate(self, plate):
        self.send_key(text=plate, ID=collection.batchPlateID)
