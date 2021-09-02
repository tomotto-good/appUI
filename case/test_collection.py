import time
import unittest
import warnings
from page.login.login import PageLogin
from page.task.taskList import PageTaskList
from page.collection.detailList import DetailList
from page.common.pl import PL
from page.common.common import Common
from common.getPath import GetPath
from common.common import unlock_phone


class TestCollection(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("---测试集港任务---")
        warnings.simplefilter('ignore', Warning)
        print('导入login文件..')
        cls.login = PageLogin()
        print('导入task文件..')
        cls.pageTaskList = PageTaskList()
        print('导入detail文件..')
        cls.detailList = DetailList()
        print('导入path文件..')
        cls.path = GetPath()
        print('导入common文件..')
        cls.common = Common()
        print('导入pl文件..')
        cls.pl = PL()

    def tearDown(self) -> None:
        self.common.restart_app()  # 重启app

    def test_collection_001(self):
        """集港明细"""
        print('---test_collection_001---')
        try:
            self.common.page_common_go_pl_list('uiCollection')  # 进入PL列表
            self.pl.page_pl_click_create()
            self.common.page_common_import_pl_file(plNumber='清单1', excelName='清单1.xlsx')
            self.pl.page_pl_click_pl_name('清单1')
            self.common.page_common_click_detail_name(detailName='鹏1')  # 进入明细详情
            self.detailList.page_send_address(address='uiAddressTest003')  # 输入场地
            self.detailList.page_send_plate_number(plate='鲁D：3638U')  # 输入车牌号
            self.common.page_common_import_picture(2)  # 从相册导入照片
            time.sleep(1)
            self.detailList.page_click_save_button()
            self.assertEqual('已完成', self.common.page_common_get_detail_status(0))
            time.sleep(1)

            """异常集港"""
            self.common.page_common_click_detail_name(detailName='龙1')  # 进入明细详情
            self.detailList.page_send_address(address='uiAddressTest004')  # 输入场地
            self.detailList.page_send_plate_number(plate='鲁D：3639U')  # 输入车牌号
            self.common.page_common_import_picture(2)  # 从相册导入照片
            self.common.page_common_click_detail_abnormal(abnormal='破损')
            self.detailList.driver(text='保存').click()
            time.sleep(1)
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

        except Exception as e:
            raise e

    def test_collection_002(self):
        """筛选明细"""
        print('---test_collection_002---')
        try:
            self.common.page_common_go_detail_list('uiCollection', '清单1')
            self.common.page_common_detail_supplier_screen('河南鹤壁')  # 根据厂商筛选任务
            self.assertTrue(self.detailList.exists_ele_text(text='博'))
        except Exception as e:
            raise e

    def test_collection_003(self):
        """下载为excel"""
        print('---test_collection_003---')
        try:
            self.common.page_common_go_detail_list('uiCollection', '清单1')
            self.common.page_common_detail_click_right_button()  # 点击右上角功能按钮
            self.detailList.page_click_download_excel()  # 下载为excel
            time.sleep(3)
            excelName = self.detailList.get_text_ID(ID='com.mj.app.marsreport.pre:id/head_title')  # 获取excel名称
            self.assertIn('xls', excelName)
        except Exception as e:
            raise e

    def test_collection_004(self):
        """验证件毛体功能"""
        print('---test_collection_004---')
        try:
            self.common.page_common_go_pl_list('uiCollection')  # 进入PL列表
            self.pl.page_pl_click_create()  # 点击新增
            self.pl.page_pl_send_pl_number('清单2')  # 输入提单号
            self.pl.page_pl_send_data(11, 12, 13)  # 输入件数/体积/重量
            self.pl.click_ele(text='确定')
            time.sleep(1)
            self.pl.driver.swipe_ext('down', 1)  # 上滑刷新
            time.sleep(1)
            self.pl.page_pl_click_pl_right_button(1)  # 点击清单2右上角按钮
            self.pl.page_pl_click_edit()  # 点击编辑按钮
            self.common.page_common_import_pl_file('清单2', '清单1.xlsx')  # 导入文件
            print(self.common.driver.toast.get_message())  # 打印提示信息
        except Exception as e:
            raise e

    def test_collection_005(self):
        """整体照片"""
        print('---test_collection_005---')
        try:
            self.common.page_common_go_pl_list('uiCollection')  # 进入PL列表
            self.pl.page_pl_click_pl_name('清单2')  # 进入明细列表
            self.pl.click_ele(text='整体照片')
            self.common.page_common_click_camara()  # 点击拍照按钮
            self.common.page_common_take_photo()  # 拍一张
            self.common.page_common_take_video()  # 录像
            time.sleep(2)
            self.common.driver.press('back')
            self.common.driver.press('back')
            time.sleep(2)
        except Exception as e:
            raise e

    def test_collection_006(self):
        """新增明细"""
        print('---test_collection_006---')
        try:
            self.common.page_common_go_pl_list('uiCollection')  # 进入PL列表
            self.pl.page_pl_click_pl_name('清单2')  # 进入明细列表
            self.common.page_common_detail_add_detail('新增明细001', '角钢、紧固件 Angle steel, fasteners', 1000, 1100, 1200,
                                                      1.32, 2,
                                                      '铁箱 IRON CASE')
            self.common.click_ele(text='确定')
            self.common.page_common_import_picture(2)  # 从相册导入照片
            self.common.click_ele(text='保存')
        except Exception as e:
            raise e
