from base.base import Base
from page import loading


class PageShift(Base):
    # 录入工班名称
    def page_send_shift_name(self, shiftName):
        self.send_key(text=shiftName, ID=loading.shiftNameID)

    # 录入件数/体积/重量
    def page_send_shift_qty_volume_weight(self, qty, volume, weight):
        self.send_key(text=qty, ID=loading.shiftQty)
        self.send_key(text=volume, ID=loading.shiftVolume)
        self.send_key(text=weight, ID=loading.shiftWeight)

    # 选择舱口/舱位
    def page_select_hatch_space(self, hatch, space):
        self.click_ele(ID=loading.selectHatchID)
        self.click_ele(text=hatch)
        self.click_ele(ID=loading.selectSpaceID)
        self.click_ele(text=space)

    # 获取工班装货量
    def page_get_shift_data(self):
        qty = self.get_text_ID(loading.shiftQty)
        volume = self.get_text_ID(loading.shiftVolume)
        weight = self.get_text_ID(loading.shiftWeight)
        return qty, volume, weight
