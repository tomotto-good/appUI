from base.base import Base
from page import loading


class PageLps(Base):
    """装船进度"""

    def page_get_real_total(self):
        # 获取全船实际积载数据
        return self.get_text(loading.lpsRealTotalID)

    def page_get_pre_total(self):
        # 获取全船预装货量
        return self.get_text(loading.lpsPreTotalID)
