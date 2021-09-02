from base.base import Base

detailSelectID = 'com.mj.app.marsreport.test:id/isSelect'  # 明细选择框
detailStatusID = 'com.mj.app.marsreport.test:id/item_label'  # 明细状态
freightID = 'com.mj.app.marsreport.test:id/freight'  # 运费输入框
prePayID = 'com.mj.app.marsreport.test:id/pre_pay'  # 预付
toPayID = 'com.mj.app.marsreport.test:id/to_pay'  # 到付
receiptPayID = 'com.mj.app.marsreport.test:id/receipt_pay'  # 回单付
saveID = 'com.mj.app.marsreport.test:id/save'  # 签名页面保存按钮


class TmsDetailList(Base):
    # 明细选择框
    def page_select_detail(self, number):
        for index in range(number):
            self.click_ele_ID(ID=detailSelectID, index=index)

    # 返回第Index条明细状态，默认第一条
    def page_get_detail_status(self, index=0):
        return self.get_text_ID(detailStatusID, index=index)

    # 输入运费并点击付款方式
    def page_send_freight(self, freight, payType):
        self.send_key_ID(text=freight, ID=freightID)
        if payType == 1:
            self.click_ele_ID(prePayID)
        elif payType == 2:
            self.click_ele_ID(toPayID)
        elif payType == 3:
            self.click_ele_ID(receiptPayID)

    # 签名页面保存按钮
    def page_sign_save(self):
        self.click_ele_ID(saveID)
