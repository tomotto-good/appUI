import time
import unittest
import warnings
from page.home.home import PageHome
from page.loading.lps import PageLps
from page.loading.shift import PageShift
from page.login.login import PageLogin
from page.task.taskList import PageTaskList
from page.unLoading.main import PageMain
from page.common.common import Common
from page.common.pl import PL
from common.getPath import GetPath


class TestUnLoading(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("---测试监卸任务---")
        warnings.simplefilter('ignore', Warning)
        print('导入login文件..')
        cls.login = PageLogin()
        print('导入home文件..')
        cls.pageHome = PageHome()
        print('导入task文件..')
        cls.pageTaskList = PageTaskList()
        print('导入main文件..')
        cls.main = PageMain()
        print("导入shift文件..")
        cls.shift = PageShift()
        print('导入path文件..')
        cls.path = GetPath()
        print('导入lps文件..')
        cls.lps = PageLps()
        print('导入pl文件..')
        cls.pl = PL()
        print('导入common文件..')
        cls.common = Common()

    def tearDown(self) -> None:
        self.common.restart_app()  # 重启app

    def test_unLoading_001(self):
        """导入PL"""
        try:
            print('---test_unloading_001---')
            self.pageHome.page_click_task_button()
            self.pageTaskList.page_click_search('uiUnloading')  # 搜索任务
            self.common.page_common_click_task_name('监卸')  # 点击任务名称进入任务
            self.main.page_click_to_create()  # 点击马上去新建
            self.common.page_common_import_pl_file('清单1', '清单1.xlsx')  # 导入清单
        except Exception as e:
            print(e)

    def test_unLoading_002(self):
        """船舶概况照片"""
        print('---test_unloading_002---')
        try:
            self.pageHome.page_click_task_button()
            self.pageTaskList.page_click_search('uiUnloading')  # 搜索任务
            self.common.page_common_click_task_name('监卸')  # 点击任务名称进入任务
            self.main.page_click_vessel_select_hatch('整体照片')
            self.common.page_common_import_picture(2)
            self.main.page_send_photo_remark('船舶概况-整体照片')
            self.main.page_click_vessel_select_hatch('No.1')  # 选择舱口
            self.main.page_click_vessel_select_space('舱盖　 No.1')  # 选择舱位
            self.common.page_common_import_picture(2)
            self.main.page_send_photo_remark('船舶概况-舱位照片')

        except Exception as e:
            print(e)

    def test_unLoading_003(self):
        """卸货过程照片"""
        print('---test_unloading_003---')
        self.pageHome.page_click_task_button()
        self.pageTaskList.page_click_search('uiUnloading')  # 搜索任务
        self.common.page_common_click_task_name('监卸')  # 点击任务名称进入任务
        self.common.click_ele(text='卸货过程')
        self.common.page_common_import_picture(2)
        time.sleep(1)
        self.common.driver.swipe_ext('up', 0.1)
        self.main.page_click_add_abnormal()  # 点击添加异常按钮
        self.main.click_ele(text='生锈')
        self.main.page_send_photo_abnormal_remark('卸货过程-舱位整体照片')
        self.main.page_click_bl_front_select('清单1')
        self.common.page_common_import_picture(2)
        self.main.page_click_add_abnormal()  # 点击添加异常按钮
        self.main.click_ele(text='变形')
        self.main.page_send_photo_abnormal_remark('卸货过程-BL整体照片')
        self.main.page_send_detail_select('鹏1')
        self.main.click_ele(text='鹏1')
        self.common.page_common_import_picture(2)
        self.main.page_click_add_abnormal()  # 点击添加异常按钮
        self.main.click_ele(text='划痕')
        self.main.page_send_photo_abnormal_remark('卸货过程-明细照片')

    def test_unLoading_004(self):
        """录入工班数据"""
        print('---test_loading_006---')
        try:
            self.pageHome.page_click_task_button()
            self.pageTaskList.page_click_search('uiUnloading')  # 搜索任务
            self.common.page_common_click_task_name(taskName='监卸')  # 点击任务名称进入任务
            self.main.page_click_create_shift()  # 新建工班
            self.shift.page_send_shift_name('工班1')  # 录入工班名称
            self.shift.click_ele(text='确定')
            if self.shift.exists_ele(text='工班卸载详情'):
                print('进入工班卸载详情页')
                self.shift.click_ele(text='No.2')
                self.shift.click_ele(text='舱盖　 No.2')
                self.shift.page_send_shift_qty_volume_weight(11, 12, 13)
                self.shift.click_ele(text='确定')

            else:
                print('当前页面不在工班卸载详情页')
        except Exception as e:
            print(e)
