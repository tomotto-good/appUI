from base.base import Base

detailSelectID = 'com.mj.app.marsreport.test:id/isSelect'  # 明细选择框
detailStatusID = 'com.mj.app.marsreport.test:id/item_label'  # 明细状态


class TmsDetailList(Base):
    # 明细选择框
    def page_select_detail(self, number):
        for index in range(number):
            self.click_ele(ID=detailSelectID, index=index)

    # 返回第Index条明细状态，默认第一条
    def page_get_detail_status(self, index=0):
        return self.get_text(detailStatusID, index=index)