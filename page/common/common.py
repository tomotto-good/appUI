from base.base import Base
from page import common
from page import foot
from page.home.home import PageHome
from page.task.taskList import PageTaskList


class Common(Base):
    def __init__(self):
        super().__init__()
        self.pageHome = PageHome()
        self.pageTaskList = PageTaskList()

    # 截图
    def save_picture(self, filename):
        self.driver.screenshot(filename=filename)
        print('截图成功保存至：', filename)

    """相册页面"""

    # 从相册导入照片
    def page_common_import_picture(self, photoNum):
        self.click_ele(text='从相册导入')  # 点击“从相册导入”
        for i in range(photoNum):
            self.get_ele(ID=common.photoID)[i].click()
        self.click_ele(ID=common.useButtonID)

    """任务列表页面"""

    # 滑动到制定位置点击任务小球
    def page_common_click_task_ball(self, remark):
        self.pageHome.page_click_task_button()  # 进入任务列表
        self.pageTaskList.page_swipe_remark(remark)  # 滑动到指定位置
        self.pageTaskList.page_click_task_ball()  # 点击任务小球

    # 点击任务名称进入任务
    def page_common_click_task_name(self, taskName):
        # 点击任务名称进入任务
        while 1 == 1:
            if self.exists_ele(text=taskName):
                self.click_ele(text=taskName)
                break
            else:
                self.driver.swipe_ext('up', 0.5)

    """PL列表页面"""

    # 点击PL名称进入明细列表
    def page_common_click_pl_name(self, plName):
        self.click_ele(text=plName)

    # 点击清单小球
    def page_common_click_pl_ball(self, index=0):
        self.click_ele(ID=foot.plBallID, index=index)

    # pl右上角功能按钮
    def page_common_click_pl_right_button(self, index=0):
        self.click_ele(ID=foot.plRightButtonID, index=index)

    # 删除模板按钮
    def page_common_click_del_pl(self):
        self.click_ele(xpath=foot.plDelXpath)

    # 新增模板按钮
    def page_common_click_create(self):
        self.click_ele(ID=foot.plCreateID)

    # 输入提单号
    def page_common_send_pl_number(self, plNumber):
        self.send_key(text=plNumber, ID=foot.plNumberID)

    # 点击“选择文件”
    def page_common_click_select_file(self):
        self.click_ele(ID=foot.plSelectFileID)

    """明细列表页面"""

    # 获取明细状态
    def page_common_get_detail_status(self, statusIndex):
        return self.get_ele(ID=common.detailStatusID)[statusIndex].get_text()

    # 点击明细名称进入明细详情
    def page_common_click_detail_name(self, detailName):
        self.click_ele(text=detailName)

    # 右上角功能按钮
    def page_common_detail_click_right_button(self):
        self.click_ele(ID=foot.rightButtonID)

    """明细详情页面"""

    # 点击明细异常
    def page_common_click_detail_abnormal(self, abnormal):
        if self.get_ele(text='变形').exists:
            self.click_ele(text=abnormal)
        else:
            while 1 == 1:
                self.driver.swipe_ext('up', 1)
                if self.get_ele(text='变形').exists:
                    self.click_ele(text=abnormal)
                    break

    # 批量选择明细
    def page_common_detail_select_all(self, footNum):
        for i in range(footNum):
            self.get_ele(ID=common.detailSelectID)[i].click()

    # 根据厂商名称筛选明细
    def page_common_detail_supplier_screen(self, supplier):
        self.click_ele(text='厂商')
        self.click_ele(text=supplier)

    """业务组装"""

    # 进入任务列表-进入PL列表
    def page_common_go_pl_list(self, taskName):
        self.pageHome.page_click_task_button()  # 进入任务列表
        self.pageTaskList.page_click_task_name(taskName)  # 进入任务

    # 进入任务列表-进入PL列表-进入明细列表
    def page_common_go_detail_list(self, taskName, plName):
        self.pageHome.page_click_task_button()  # 进入任务列表
        self.pageTaskList.page_click_task_name(taskName)  # 进入任务
        self.page_common_click_pl_name(plName)  # 进入明细列表

    # 点击选择文件-点击excel-ok
    def page_common_import_pl_file(self, excelName):
        # 导入清单
        self.page_common_click_select_file()
        self.click_ele(text=excelName)
        self.click_ele(text='OK')
        self.click_ele(text='确定')

    # 输入提单号-输入件毛体-点击确定
    def page_common_create_pl(self, plNumber):
        self.page_common_send_pl_number(plNumber)
        pass
