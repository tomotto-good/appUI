import time
import unittest
import random
from page.task.taskList import PageTaskList
from page.tms.tmsPl import PageTmsPl
from page.tms.tmsTrainList import TmsTrainList
from page.tms.tmsDetailList import TmsDetailList
from page.common.common import Common
from page.tms.tmsPhoto import TmsPhoto


class TestTms(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.taskList = PageTaskList()
        cls.pl = PageTmsPl()
        cls.trainList = TmsTrainList()
        cls.detailList = TmsDetailList()
        cls.common = Common()
        cls.photo = TmsPhoto()

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_tms_001(self):
        """创建装卸车任务 """
        try:
            global taskName
            self.taskList.page_click_add_task_button()
            taskName = "tms{}".format(random.randint(10, 100))
            self.taskList.page_send_task_name(taskName)
            self.taskList.click_ele(text='确定')
            self.assertTrue(self.taskList.exists_ele_text('模板下载'), '任务创建失败')
        except Exception as e:
            raise e

    def test_tms_002(self):
        """新增PL"""
        try:
            self.pl.page_send_pl_name('清单1')
            self.pl.page_send_acceptance('受理号')
            self.pl.page_send_pl_size(100, 110, 120)  # 输入长宽高
            self.pl.click_ele(text='显示更多信息')
            time.sleep(1)
            self.pl.driver.swipe_ext('up', 1)
            self.pl.page_send_more_info('合同号', '货运代理', '发货人', '联系人', '18217486666', '卸货港', '任务描述', '收货人')
            self.pl.page_click_import_file()  # 导入PL文件
            self.pl.click_ele(text='确定')
        except Exception as e:
            raise e

    def test_tms_003(self):
        """创建车次"""
        try:
            for i in range(6):
                self.pl.click_ele(text='车次列表')
                self.trainList.page_add_train('鲁D 00{}'.format(i),
                                              '司机：{}'.format(i),
                                              '182{}'.format(random.randint(10000000, 99999999)))
                self.trainList.click_ele(text='确定')
                self.assertEqual(self.trainList.page_get_train_status(), '待装车')
        except Exception as e:
            raise e

    def test_tms_004(self):
        """编辑车次"""
        try:
            self.trainList.click_ele(text='编辑')
            self.trainList.page_send_address_info('薛城', '浦东')
        except Exception as e:
            raise e

    def test_tms_005(self):
        """车次状态-预装车"""
        try:

            self.common.page_common_restart_app_go_task('com.mj.app.marsreport.test', taskName)  # 重启app并进入任务
            self.common.click_ele(text='确认并开始任务')
            time.sleep(1)
            self.trainList.click_ele(text='鲁D 005')
            self.detailList.click_ele(text='批量装车')
            self.detailList.page_select_detail(1)  # 选择明细
            self.detailList.click_ele(text='批量预装车')
            self.detailList.click_ele(text='预装车')
            self.assertEqual(self.detailList.page_get_detail_status(), '预装车')  # 断言明细状态
            time.sleep(1)
            self.detailList.driver.press('back')
            self.detailList.driver.press('back')
            i = 0
            while i < 5:
                i += 1
                status = self.trainList.page_get_train_status()
                if status == '预装车':
                    break
                else:
                    self.trainList.driver.swipe_ext('down', 1)
        except Exception as e:
            raise e

    def test_tms_006(self):
        """车次状态-装车中"""
        try:
            self.trainList.click_ele(text='鲁D 004')  # 进入明细列表
            self.detailList.click_ele(text='龙1')  # 进入明细详情
            self.common.page_common_import_picture(9)
            self.common.click_ele(text='装载过程')
            self.common.page_common_import_picture(9)
            self.common.click_ele(text='水湿')
            self.common.click_ele(text='保存')
            self.assertEqual(self.common.page_common_get_detail_status(0), '已装车')
        except Exception as e:
            raise e

    def test_tms_006_01(self):
        """车次状态-装车中-整体照片"""
        try:
            self.common.click_ele(text='整体照片')
            self.common.page_common_import_picture(2)
            self.common.long_click(0.177, 0.261)  # 长按编辑
            self.photo.page_send_photo_remark('装前车次整体-货物')
            self.photo.click_ele(text='确定')
            self.common.long_click(0.492, 0.26)  # 长按编辑
            self.photo.page_send_photo_remark('装前车次整体-签收单')
            self.photo.click_ele(text='签收单')
            self.photo.click_ele(text='确定')
        except Exception as e:
            raise e

    def test_tms_007(self):
        """车次状态-已发车"""
        self.common.page_common_restart_app_go_task('com.mj.app.marsreport.test', 'tms34')
        self.common.click_ele(text='鲁D 003')
        self.common.click_ele(text='阿sir')
        self.common.page_common_import_picture(9)
        self.common.click_ele(text='装载过程')
        self.common.page_common_import_picture(9)
        self.common.click_ele(text='水湿')
        self.common.click_ele(text='保存')
        self.assertEqual(self.common.page_common_get_detail_status(0), '已装车')
        self.common.click_ele(text='兵')
        self.common.page_common_import_picture(9)
        self.common.click_ele(text='装载过程')
        self.common.page_common_import_picture(9)
        self.common.click_ele(text='水湿')
        self.common.click_ele(text='保存')
        self.assertEqual(self.common.page_common_get_detail_status(1), '已装车')
        self.common.click_ele(text='GP-1')
        self.common.page_common_import_picture(9)
        self.common.click_ele(text='装载过程')
        self.common.page_common_import_picture(9)
        self.common.click_ele(text='水湿')
        self.common.click_ele(text='保存')
        self.assertEqual(self.common.page_common_get_detail_status(2), '已装车')
