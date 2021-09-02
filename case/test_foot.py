import unittest
import warnings
from page.task.taskList import PageTaskList
from page.foot.detailList import DetailList
from page.common.pl import PL
from page.common.common import Common
from common.getPath import GetPath
import time


class TestFoot(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("---测试打尺任务---")
        warnings.simplefilter('ignore', Warning)
        print('导入task文件..')
        cls.pageTaskList = PageTaskList()
        print('导入detail文件..')
        cls.detailList = DetailList()
        print('导入pl文件..')
        cls.pl = PL()
        print('导入path文件..')
        cls.path = GetPath()
        print('导入common文件..')
        cls.common = Common()

    def tearDown(self) -> None:
        self.common.restart_app()  # 重启app

    def test_foot_001(self):
        """正常/异常/批量打尺"""
        print('---test_foot_001---')
        try:
            self.common.page_common_go_pl_list('uiFoot')  # 进入PL列表
            self.pl.page_pl_click_create()
            self.common.page_common_import_pl_file('清单1', '清单1.xlsx')
            self.pl.page_pl_click_pl_name('清单1')
            self.common.page_common_click_detail_name(detailName='鹏1')  # 进入明细详情
            self.detailList.page_detail_add_length_width_height()  # 长宽高各增加10mm
            self.detailList.page_detail_input_address(address='uiAddressTest001')  # 输入场地
            self.detailList.driver.swipe_ext('up', 0.5)  # 由于遮挡，需要向上滑动
            self.common.page_common_import_picture(2)
            self.detailList.driver.swipe_ext('up', 0.5)
            self.detailList.page_detail_ok_button()
            status = self.common.page_common_get_detail_status(0)
            self.assertEqual(status, '已完成')

            self.common.page_common_click_detail_name(detailName='龙1')  # 进入明细详情
            self.detailList.page_detail_add_length_width_height()  # 长宽高各增加10mm
            self.detailList.page_detail_input_address(address='uiAddressTest002')  # 输入场地
            self.common.page_common_import_picture(2)
            time.sleep(1)
            self.detailList.driver.swipe_ext('up', 1)
            self.common.page_common_click_detail_abnormal('生锈')
            self.detailList.page_detail_ok_button()
            status = self.common.page_common_get_detail_status(1)
            self.assertEqual(status, '异常')
            while 1 == 1:
                if self.detailList.exists_ele_text(text='龙3'):
                    self.detailList.page_detail_click_batch_foot()  # 点击批量打尺
                    break
                else:
                    self.detailList.driver.swipe_ext('up', 1)
            self.common.page_common_detail_select_all(2)  # 选择批量打尺的件数
            self.detailList.page_detail_click_batch_foot()  # 点击批量打尺
            self.detailList.driver(text='确定').click()  # 点击确定
            self.detailList.driver(text='确定').click()  # 二次提示--点击确定
            self.detailList.driver(text='取消').click()  # 点击取消
        except Exception as e:
            raise e

    def test_foot_002(self):
        """筛选明细"""
        print('---test_foot_002---')
        try:
            self.common.page_common_go_detail_list('uiFoot', '清单1')
            self.detailList.driver(text='有无异常').click()  # 筛选明细异常
            self.detailList.driver(text='有异常').click()
            status = self.common.page_common_get_detail_status(0)
            self.assertEqual(status, '异常')
        except Exception as e:
            raise e

    def test_foot_003(self):
        """生成日报"""
        print('---test_foot_003---')
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
            self.assertIn('pdf', self.detailList.page_detail_get_report_name())
        except Exception as e:
            raise e

    def test_foot_004(self):
        """下载清单"""
        print('---test_foot_004---')
        try:
            self.common.page_common_go_detail_list('uiFoot', '清单1')
            self.common.page_common_detail_click_right_button()  # 点击右上角功能按钮
            self.detailList.page_click_download_excel()  # 下载为excel
            time.sleep(1)
            excelName = self.detailList.get_text_ID(ID='com.mj.app.marsreport.pre:id/head_title')  # 获取excel名称
            self.assertIn('xls', excelName)
        except Exception as e:
            raise e

    def test_foot_005(self):
        """整体照片"""
        print('---test_foot_005---')
        pass

    @unittest.skip('跳过，等PC脚本完成后可执行')
    def test_foot_006(self):
        """重建测试数据"""
        try:
            self.common.page_common_go_pl_list('uiFoot')  # 进入pl列表
            self.pl.page_pl_click_pl_right_button()  # 点击右上角功能按钮
            self.pl.page_pl_click_del_pl()  # 点击删除
            self.pl.driver(text='确定').click()
            self.pl.page_pl_click_create()  # 新增
            self.pl.page_pl_send_pl_number('清单1')  # 输入提单号
            self.common.page_common_import_pl_file('清单1', '清单1.xlsx')  # 导入文件
            print(self.common.driver.toast.get_message())  # 打印提示信息
        except Exception as e:
            raise e
