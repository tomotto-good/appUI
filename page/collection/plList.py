from base.base import Base
from page import collection


class PlList(Base):
    # 点击编辑按钮
    def page_pl_click_edit(self):
        self.click_ele(xpath=collection.editXpath)

    """新增/编辑PL页面"""

    # 输入件毛体
    def page_pl_send_data(self, number, volume, weight):
        self.send_key(text=number, ID=collection.numberID)
        self.send_key(text=volume, ID=collection.volumeID)
        self.send_key(text=weight, ID=collection.weightID)
