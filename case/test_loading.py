import unittest
import warnings
from page.home.home import PageHome
from page.login.login import PageLogin
from page.task.taskList import PageTaskList
from page.foot.plList import PlList
from page.foot.detailList import DetailList
from page.common.common import Common
from common.getPath import GetPath


class TestFoot(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        warnings.simplefilter('ignore', Warning)
        cls.login = PageLogin()
        cls.pageHome = PageHome()
        cls.pageTaskList = PageTaskList()
        cls.plList = PlList()
        cls.detailList = DetailList()
        cls.path = GetPath()
        cls.common = Common()
        cls.login.page_judge_login()  # 判断app是否在登陆页面

    def tearDown(self) -> None:
        self.detailList.restart_app()  # 重启app

    def test_loading_001(self):
        """导入PL"""
        self.pageTaskList.page_send_search('uiLoading')  # 搜索任务
        self.common.page_common_click_task_name('uiLoading')  # 点击任务名称进入任务
        # 创建PL（不导入清单）
