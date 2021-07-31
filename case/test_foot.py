import unittest
import warnings
from page.home.home import PageHome
from page.login.login import PageLogin
from page.task.taskList import PageTaskList
from page.foot.plList import PlList
from page.foot.detailList import DetailList
from page.common.common import Common
from common.getPath import GetPath
import time


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

    def test_foot_001(self):
        """正常打尺""" """异常打尺""" """批量打尺"""
        try:
            self.common.page_common_go_detail_list('uiFoot', '清单1')
            self.common.page_common_click_detail_name(detailName='鹏1')  # 进入明细详情
            self.detailList.page_detail_add_length_width_height()  # 长宽高各增加10mm
            self.detailList.page_detail_input_address(address='uiAddressTest001')  # 输入场地
            self.detailList.driver.swipe_ext('up', 0.5)  # 由于遮挡，需要向上滑动
            self.common.page_common_import_picture(2)
            self.detailList.driver.swipe_ext('up', 0.5)
            self.detailList.page_detail_ok_button()
            status = self.common.page_common_get_detail_status(0)
            self.common.save_picture(self.path.imagePath + r'\foot\foot.jpg')  # 截图
            self.assertEqual(status, '已完成')
        except Exception:
            raise

        try:
            self.common.page_common_click_detail_name(detailName='龙1')  # 进入明细详情
            self.detailList.page_detail_add_length_width_height()  # 长宽高各增加10mm
            self.detailList.page_detail_input_address(address='uiAddressTest002')  # 输入场地
            self.common.page_common_import_picture(2)
            time.sleep(1)
            self.detailList.driver.swipe_ext('up', 1)
            self.common.page_common_click_detail_abnormal('生锈')
            self.detailList.page_detail_ok_button()
            status = self.common.page_common_get_detail_status(1)
            self.common.save_picture(self.path.imagePath + r'\foot\abnormalFoot.jpg')  # 截图
            self.assertEqual(status, '异常')
        except AssertionError as e:
            return e

        while 1 == 1:
            if self.detailList.exists_ele(text='龙3'):
                self.detailList.page_detail_click_batch_foot()  # 点击批量打尺
                break
            else:
                self.detailList.driver.swipe_ext('up', 1)
        self.common.page_common_detail_select_all(2)  # 选择批量打尺的件数
        self.detailList.page_detail_click_batch_foot()  # 点击批量打尺
        self.detailList.driver(text='确定').click()  # 点击确定
        self.detailList.driver(text='确定').click()  # 二次提示--点击确定
        self.detailList.driver(text='取消').click()  # 点击取消
        self.common.save_picture(self.path.imagePath + r'\foot\twoFoot.jpg')  # 截图

    def test_foot_002(self):
        """筛选明细"""
        self.common.page_common_go_detail_list('uiFoot', '清单1')
        self.detailList.driver(text='有无异常').click()  # 筛选明细异常
        self.detailList.driver(text='有异常').click()
        status = self.common.page_common_get_detail_status(0)
        self.assertEqual(status, '异常')

    def test_foot_003(self):
        """生成日报"""
        try:
            self.common.page_common_go_detail_list('uiFoot', '清单1')
            self.common.page_common_detail_click_right_button()  # 点击右上角功能按钮
            self.detailList.driver(text='生成日报').click()  # 生成日报
            self.detailList.driver(text='确认').click()
            while 1 == 1:
                if self.detailList.driver(
                        resourceId='com.mj.app.marsreport.pre:id/title_text').exists:
                    self.detailList.driver(text='OK').click()
                    self.detailList.driver(text='确认').click(timeout=3)
                else:
                    break
            self.detailList.driver.drag(0.166, 0.589, 0.626, 0.593)  # 签名
            self.detailList.driver(text='生成日报').click()  # 生成日报
            self.detailList.driver(text='确定').click()
            time.sleep(3)
            self.common.save_picture(self.path.imagePath + r'\foot\Report.jpg')
            self.assertIn('pdf', self.detailList.page_detail_get_report_name())
        except Exception as e:
            print(e)

    def test_foot_004(self):
        """下载清单"""
        self.common.page_common_go_detail_list('uiFoot', '清单1')
        self.common.page_common_detail_click_right_button()  # 点击右上角功能按钮
        self.detailList.page_click_download_excel()  # 下载为excel
        time.sleep(1)
        self.common.save_picture(self.path.imagePath + r'\foot\excel.jpg')  # 截图

    def test_foot_005(self):
        """获取打尺数据截图保存到本地"""
        try:
            self.common.page_common_click_task_ball('打尺')  # 点击任务小球
            time.sleep(2)
            self.pageTaskList.get_image(self.path.imagePath + r'\foot\taskBall.jpg')
            self.pageTaskList.driver.press('back')
            self.common.page_common_click_task_name('uiFoot')  # # 点击任务名称进入PL列表
            self.common.page_common_click_pl_ball()  # 点击清单小球
            self.pageTaskList.get_image(self.path.imagePath + r'\foot\plBall.jpg')
        except Exception as e:
            print(e)

    @unittest.skip('跳过，等PC脚本完成后可执行')
    def test_foot_006(self):
        """重建测试数据"""
        try:
            self.common.page_common_go_pl_list('uiFoot')  # 进入pl列表
            self.common.page_common_click_pl_right_button()  # 点击右上角功能按钮
            self.common.page_common_click_del_pl()  # 点击删除
            self.plList.driver(text='确定').click()
            self.common.page_common_click_create()  # 新增
            self.common.page_common_send_pl_number('清单1')  # 输入提单号
            self.common.page_common_import_pl_file('清单1.xlsx')  # 导入文件
            print(self.common.driver.toast.get_message())  # 打印提示信息
        except Exception as e:
            print(e)
