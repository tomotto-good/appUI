"""以下为PL页面元素"""
import time

from base.base import Base

plNameID = 'com.mj.app.marsreport.test:id/bl'  # 清单名称输入框
acceptanceID = 'com.mj.app.marsreport.test:id/acceptance'  # 受理号输入框
quantityID = 'com.mj.app.marsreport.test:id/quantity'  # 件数输入框
volumeID = 'com.mj.app.marsreport.test:id/volume'  # 体积输入框
weightID = 'com.mj.app.marsreport.test:id/weight'  # 重量输入框
contractID = 'com.mj.app.marsreport.test:id/contract'  # 合同号输入框
freightForwarderID = 'com.mj.app.marsreport.test:id/freightForwarder'  # 货运代理输入框
shipperID = 'com.mj.app.marsreport.test:id/shipper'  # 发货人输入框
contactID = 'com.mj.app.marsreport.test:id/contact'  # 联系人输入框
contactPhoneID = 'com.mj.app.marsreport.test:id/contact_phone'  # 联系人电话输入框
podID = 'com.mj.app.marsreport.test:id/pod'  # 卸货港输入框
consigneeID = 'com.mj.app.marsreport.test:id/consignee'  # 收货人输入框
descriptionId = 'com.mj.app.marsreport.test:id/description'  # 描述输入框
selectFileID = 'com.mj.app.marsreport.test:id/select_file'  # 选择文件按钮


class PageTmsPl(Base):

    def page_send_pl_name(self, plName):
        # 输入提单号
        self.send_key_ID(text=plName, ID=plNameID)

    def page_send_acceptance(self, acceptance):
        # 输入受理号
        self.send_key_ID(text=acceptance, ID=acceptanceID)

    def page_send_pl_size(self, quantity, volume, weight):
        # 输入清单尺寸
        self.send_key_ID(text=quantity, ID=quantityID)
        self.send_key_ID(text=volume, ID=volumeID)
        self.send_key_ID(text=weight, ID=weightID)

    # 输入PL相关信息
    def page_send_more_info(self, contract, freightForwarder, shipper, contact, contact_phone, pod, description,
                            consignee):
        self.send_key_ID(text=contract, ID=contractID)
        self.send_key_ID(text=freightForwarder, ID=freightForwarderID)
        self.send_key_ID(text=shipper, ID=shipperID)
        self.send_key_ID(text=contact, ID=contactID)
        self.send_key_ID(text=contact_phone, ID=contactPhoneID)
        time.sleep(1)
        self.send_key_ID(text=pod, ID=podID)
        self.send_key_ID(text=description, ID=descriptionId)
        self.send_key_ID(text=consignee, ID=consigneeID)

    # 导入PL清单文件
    def page_click_import_file(self):
        self.click_ele_ID(ID=selectFileID)
        if self.exists_ele_text(text='清单1.xlsx'):
            self.click_ele_text(text='清单1.xlsx')
            self.click_ele_text(text='OK')
        else:
            self.click_ele_description(description='显示根目录')
            self.click_ele_text(text='文件管理(QQ浏览器)')
            self.click_ele_text(text='手机存储')
            self.click_ele_text(text='1')
            self.click_ele_text(text='清单1.xlsx')
            self.click_ele_text(text='OK')
