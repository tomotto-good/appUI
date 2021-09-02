from base.base import Base

photoRemarkID = 'com.mj.app.marsreport.test:id/remark'  # 整体照片备注


class TmsPhoto(Base):
    # 输入整体照片备注
    def page_send_photo_remark(self, remark):
        self.send_key_ID(text=remark, ID=photoRemarkID)
