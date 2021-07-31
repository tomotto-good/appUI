import time
import unittest
import warnings
from page.home.home import PageHome
from page.login.login import PageLogin
from page.task.taskList import PageTaskList
from page.collection.detailList import DetailList
from page.collection.plList import PlList
from page.common.common import Common
from common.getPath import GetPath


class TestCollection(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        warnings.simplefilter('ignore', Warning)
        cls.login = PageLogin()
        cls.pageHome = PageHome()
        cls.pageTaskList = PageTaskList()
        cls.detailList = DetailList()
        cls.path = GetPath()
        cls.common = Common()
        cls.plList = PlList()
        cls.login.restart_app()
        cls.login.page_judge_login()  # 判断app是否在登陆页面

    def tearDown(self) -> None:
        self.login.restart_app()  # 重启app

    def test_collection_001(self):
        """集港明细"""

        try:
            self.common.page_common_go_detail_list('uiCollection', '清单1')  # 进入明细列表
            self.common.page_common_click_detail_name(detailName='鹏1')  # 进入明细详情
            self.detailList.page_send_address(address='uiAddressTest003')  # 输入场地
            self.detailList.page_send_plate_number(plate='鲁D：3638U')  # 输入车牌号
            self.common.page_common_import_picture(2)  # 从相册导入照片
            time.sleep(1)
            self.detailList.page_click_save_button()
            self.assertEqual('已完成', self.common.page_common_get_detail_status(0))
            self.common.save_picture(self.path.imagePath + r'\collection\coll.jpg')  # 截图
            time.sleep(1)

            """异常集港"""
            self.common.page_common_click_detail_name(detailName='龙1')  # 进入明细详情
            self.detailList.page_send_address(address='uiAddressTest004')  # 输入场地
            self.detailList.page_send_plate_number(plate='鲁D：3639U')  # 输入车牌号
            self.common.page_common_import_picture(2)  # 从相册导入照片
            self.common.page_common_click_detail_abnormal(abnormal='破损')
            self.detailList.driver(text='保存').click()
            time.sleep(1)
            self.common.save_picture(self.path.imagePath + r'\collection\collAbnormal.jpg')  # 截图
            self.assertEqual('异常', self.common.page_common_get_detail_status(1))

            """批量集港"""
            self.detailList.driver.swipe_ext('up', 0.9)
            self.detailList.click_ele(text='批量集港')
            self.common.page_common_detail_select_all(2)  # 选择批量集岗的件数
            self.detailList.click_ele(text='批量集港')
            self.detailList.page_send_batch_address(address='uiAddressTest005')
            self.detailList.page_send_batch_plate(plate='鲁D：3640U')
            self.detailList.click_ele(text='确定')
            self.detailList.click_ele(text='确定')
            time.sleep(1)
            self.common.save_picture(self.path.imagePath + r'\collection\collBatch.jpg')  # 截图
        except Exception as e:
            print(e)

    def test_collection_002(self):
        """筛选明细"""
        try:
            self.common.page_common_go_detail_list('uiCollection', '清单1')
            self.common.page_common_detail_supplier_screen('河南鹤壁')  # 根据厂商筛选任务
            if self.detailList.exists_ele(text='博'):
                self.common.save_picture(self.path.imagePath + r'\collection\supplier.jpg')  # 截图
                print('--测试通过--')
            else:
                return False
        except Exception:
            raise

    def test_collection_003(self):
        """下载为excel"""
        self.common.page_common_go_detail_list('uiCollection', '清单1')
        self.common.page_common_detail_click_right_button()  # 点击右上角功能按钮
        self.detailList.page_click_download_excel()  # 下载为excel
        time.sleep(1)
        self.common.save_picture(self.path.imagePath + r'\collection\excel.jpg')  # 截图

    def test_collection_004(self):
        """验证件毛体功能"""
        self.common.page_common_go_pl_list('uiCollection')  # 进入PL列表
        self.common.page_common_click_create()  # 点击新增
        self.common.page_common_send_pl_number('清单2')  # 输入提单号
        self.plList.page_pl_send_data(11, 12, 13)  # 输入件数/体积/重量
        self.plList.click_ele(text='确定')
        time.sleep(1)
        self.plList.driver.swipe_ext('down', 1)  # 上滑刷新
        time.sleep(1)
        self.common.page_common_click_pl_right_button(1)  # 点击清单2右上角按钮
        self.plList.page_pl_click_edit()  # 点击编辑按钮
        self.common.page_common_import_pl_file('清单1.xlsx')  # 导入文件
        print(self.common.driver.toast.get_message())  # 打印提示信息

    def test_collection_005(self):
        """验证任务小球数据"""
        self.common.page_common_click_task_ball('集港')  # 根据任务备注滑动到指定位置点击任务小球
        time.sleep(2)
        self.common.save_picture(self.path.imagePath + r'\collection\taskBall.jpg')  # 截图

    def test_collection_006(self):
        """验证清单小球数据"""
        self.pageHome.page_click_task_button() # 点击任务按钮
        self.common.page_common_click_task_name('uiCollection')  # 点击任务名称进入任务
        self.common.page_common_click_pl_ball()
        self.common.page_common_click_pl_ball(index=1)  # 点击清单小球
        self.common.save_picture(self.path.imagePath + r'\collection\plBall.jpg')  # 截图
