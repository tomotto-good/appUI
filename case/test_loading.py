import time
import unittest
import warnings
from page.home.home import PageHome
from page.login.login import PageLogin
from page.task.taskList import PageTaskList
from page.loading.main import PageMain
from page.common.common import Common
from page.loading.shift import PageShift
from page.loading.lps import PageLps
from common.getPath import GetPath


class TestLoading(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("---测试监装任务---")
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
        print('导入common文件..')
        cls.common = Common()

    def tearDown(self) -> None:
        pass

    def test_loading_001(self):
        """导入PL"""
        try:
            print('---test_loading_001---')
            self.pageHome.page_click_task_button()
            self.pageTaskList.page_click_search('uiLoading')  # 搜索任务
            self.common.page_common_click_task_name('监装')  # 点击任务名称进入任务
            self.main.page_click_to_create()  # 点击马上去新建
            self.common.page_common_import_pl_file('清单1', '清单1.xlsx')  # 导入清单
        except Exception as e:
            print(e)

    def test_loading_002(self):
        """装前货况-其他照片"""
        try:
            print('---test_loading_002---')
            self.common.page_common_import_picture(2)
            time.sleep(1)
            self.common.driver.swipe_ext('up', 0.1)  # 添加异常按钮被遮挡，需要上滑
            self.main.page_click_add_abnormal()  # 点击添加异常按钮
            self.main.click_ele(text='生锈')  # 选择异常
            self.main.page_send_photo_remark('装前货况其他照片')
            time.sleep(1)
            self.common.driver.swipe_ext('down', 1)  # 恢复页面
        except Exception as e:
            print(e)

    def test_loading_003(self):
        """装前货况-BL整体照片"""
        print('---test_loading_003---')
        self.main.page_click_bl_front_select('清单1')  #
        self.common.page_common_import_picture(2)
        time.sleep(1)
        self.common.driver.swipe_ext('up', 0.1)  # 添加异常按钮被遮挡，需要上滑
        self.main.page_click_add_abnormal()  # 点击添加异常按钮
        self.main.click_ele(text='变形')  # 选择异常
        self.main.page_send_photo_remark('装前货况BL整体照片')
        time.sleep(1)
        self.common.driver.swipe_ext('down', 1)  # 恢复页面

    def test_loading_004(self):
        """装前货况-明细照片"""
        print('---test_loading_004---')
        self.main.page_click_detail_front_select('鹏1')  # 选择件号
        self.common.page_common_import_picture(2)
        time.sleep(1)
        self.common.driver.swipe_ext('up', 0.1)  # 添加异常按钮被遮挡，需要上滑
        self.main.page_click_add_abnormal()  # 点击添加异常按钮
        self.main.click_ele(text='破损')  # 选择异常
        self.main.page_send_photo_remark('装前货况明细照片')

    def test_loading_005(self):
        """船舶概况-整体照片"""
        print('---test_loading_005---')
        time.sleep(1)
        self.main.driver.drag(0.887, 0.705, 0.088, 0.082)  # 将IM控件拖拽出去
        self.main.click_ele(text='船舶概况')
        self.common.page_common_import_picture(2)  # 从相册导入照片
        self.main.page_click_add_abnormal()  # 点击添加异常按钮
        self.main.page_send_photo_remark('船舶概况整体照片')

    def test_loading_006(self):
        """船舶概况-舱位照片"""
        print('---test_loading_006---')
        self.main.page_click_vessel_select_hatch('No.1')  # 选择舱口
        self.main.page_click_vessel_select_space('舱盖　 No.1')  # 选择舱位
        self.common.page_common_import_picture(2)
        self.main.page_click_add_abnormal()  # 点击添加异常按钮
        self.main.page_send_photo_remark('船舶概况舱位照片')

    def test_loading_007(self):
        """装载过程-舱位整体照片"""
        print('---test_loading_007---')
        self.main.click_ele(text='装载过程')
        self.common.page_common_import_picture(2)  # 从相册导入照片
        time.sleep(1)
        self.common.driver.swipe_ext('up', 1)
        self.main.page_click_add_abnormal()
        self.main.click_ele(text='划痕')
        self.main.page_send_photo_remark('装载过程舱位整体照片')
        time.sleep(1)
        self.common.driver.swipe_ext('down', 1)

    def test_loading_008(self):
        """装载过程-BL整体照片"""
        try:
            print('---test_loading_008---')
            self.main.page_click_bl_front_select('清单1')
            self.common.page_common_import_picture(2)  # 从相册导入照片
            time.sleep(1)
            self.common.driver.swipe_ext('up', 1)
            self.main.page_click_add_abnormal()
            self.main.click_ele(text='油污')
            self.main.page_send_photo_remark('装载过程BL整体照片')
            time.sleep(1)
            self.common.driver.swipe_ext('down', 1)
        except Exception as e:
            print(e)

    def test_loading_009(self):
        """装载过程-明细照片"""
        print('---test_loading_009---')
        self.main.page_click_detail_front_select('龙1')  # 选择件号
        self.common.page_common_import_picture(2)  # 从相册导入照片
        time.sleep(1)
        self.common.driver.swipe_ext('up', 1)
        self.main.page_click_add_abnormal()
        self.main.click_ele(text='油污')
        self.main.page_send_photo_remark('装载过程明细照片')

    def test_loading_010(self):
        """绑扎材料"""
        print('---test_loading_010---')
        self.main.click_ele(text='绑扎材料')
        self.main.click_ele(text='6*8*100CM')  # 选择规格
        self.common.page_common_import_picture(2)  # 从相册导入照片

    def test_loading_011(self):
        """录入工班数据"""
        print('---test_loading_011---')
        self.main.page_click_create_shift()  # 新建工班
        self.shift.page_send_shift_name('工班1')  # 录入工班名称
        self.shift.click_ele(text='确定')
        if self.shift.exists_ele(text='工班积载详情'):
            print('进入工班积载详情页')
            self.shift.click_ele(text='清单1')
            if self.shift.exists_ele(text='新增PL积载数据'):
                self.shift.click_ele(text='新增PL积载数据')
                self.shift.page_send_shift_qty_volume_weight(10, 11, 12)
                self.shift.click_ele(text='添加，并继续下一条')
                self.shift.page_select_hatch_space('No.3', '舱盖　 No.3')
                self.shift.page_send_shift_qty_volume_weight(13, 14, 15)
                self.shift.click_ele(text='添加')
                time.sleep(1)
                self.shift.driver.press('back')
                if self.shift.exists_ele(text='工班积载详情'):
                    print("工班1-清单1件数/体积/重量： ", self.shift.page_get_shift_data())
                    self.shift.driver.press('back')
                    time.sleep(2)
        else:
            print('当前页面不在工班积载详情页')

    def test_loading_012(self):
        """监装-舱口列表-装载数据"""
        print('---test_loading_012---')
        self.main.click_ele(text='装载数据')
        self.assertEqual('23pkgs/25.0m³/27.0t', self.lps.page_get_real_total())
        self.assertEqual('14pkgs/15.53m³/27.77t', self.lps.page_get_pre_total())
