from base.base import Base
from page import task
from page.home.home import PageHome


class PageTaskList(Base):
    def __init__(self):
        super().__init__()
        self.pageHome = PageHome()

    def page_click_task_name(self, taskName):
        # 点击任务名称进入任务
        while 1 == 1:
            if self.driver(text=taskName).exists:
                self.click_ele(text=taskName)
                break
            else:
                self.driver.swipe_ext('up', 0.5)

    def page_swipe_remark(self, remark):
        # 根据任务列表备注滑动
        while 1 == 1:
            x = self.get_ele(ID=task.remarkID).get_text()
            if x.split("：")[-1] == remark:
                break
            else:
                self.driver.swipe_ext('up', 0.3)

    def page_click_task_ball(self):
        # 点击任务小球
        self.click_ele(ID=task.taskBall)

    # 点击任务列表-点击搜索框-输入搜索内容-点击搜索
    def page_send_search(self, search):
        self.pageHome.page_click_task_button()  # 点击任务按钮
        self.click_ele(ID=task.marsID)  # 点击莫斯一下
        self.send_key(text=search, ID=task.searchID)  # 输入搜索内容
        self.click_ele(ID=task.searchButtonID)  # 点击搜索按钮
