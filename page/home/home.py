from base.base import Base
from page import home


class PageHome(Base):
    # 点击任务按钮
    def page_click_task_button(self):
        self.click_ele(ID=home.taskId)
