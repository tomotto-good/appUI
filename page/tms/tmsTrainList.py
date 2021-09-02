import time

from base.base import Base

addTrainButtonID = 'com.mj.app.marsreport.test:id/create'  # 新建车次按钮
trainNumberID = 'com.mj.app.marsreport.test:id/licensePlateNumber'  # 车牌号输入框
driverID = 'com.mj.app.marsreport.test:id/driver'  # 司机输入框
phoneID = 'com.mj.app.marsreport.test:id/mobile'  # 手机号输入框
originID = 'com.mj.app.marsreport.test:id/origin_address_name'  # 起运地
destinationID = 'com.mj.app.marsreport.test:id/destination_name'  # 目的地
trainStatusID = 'com.mj.app.marsreport.test:id/tag'  # 车次状态
addressSearchID = 'com.mj.app.marsreport.test:id/search'  # 地址搜索框


class TmsTrainList(Base):
    # 添加车次
    def page_add_train(self, trainNumber, driver, phone):
        self.click_ele_ID(addTrainButtonID)
        self.send_key_ID(text=trainNumber, ID=trainNumberID)
        self.send_key_ID(text=driver, ID=driverID)
        self.send_key_ID(text=phone, ID=phoneID)

    # 返回第index条明细状态，默认第一条
    def page_get_train_status(self, index=0):
        return self.get_text_ID(trainStatusID, index=index)

    # 录入起运地/目的地
    def page_send_address_info(self, origin, destination):
        self.click_ele_ID(originID)  #
        self.send_key_ID(text=origin, ID=addressSearchID)
        self.click_ele_ID(ID='com.mj.app.marsreport.test:id/item_des', index=1)
        time.sleep(1)
        self.click_ele_text(text='确定')
        time.sleep(1)
        self.click_ele_ID(destinationID)  #
        self.send_key_ID(text=destination, ID=addressSearchID)
        self.click_ele_ID(ID='com.mj.app.marsreport.test:id/item_des', index=1)
        time.sleep(1)
        self.click_ele_text(text='确定')
        time.sleep(1)
        self.click_ele_text(text='确定')
