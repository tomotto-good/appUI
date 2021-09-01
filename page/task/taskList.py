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

    def page_click_search(self, text):
        # 点击莫斯一下-搜索任务
        self.click_ele(task.marsID)
        self.send_key(text=text, ID=task.searchID)
        self.click_ele(ID=task.searchButtonID)

    def page_click_add_task_button(self):
        # 点击任务列表添加任务按钮
        self.click_ele(ID=task.addTaskButtonID)

    def page_send_task_name(self, taskName):
        # 输入任务名称
        self.send_key(text=taskName, ID=task.taskNameInputID)
