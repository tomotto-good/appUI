import os


class GetPath:
    def __init__(self):
        # 当前文件绝对路径
        curPath = os.path.realpath(__file__)
        # 当前文件夹绝对路径
        self.dirPath = os.path.dirname(curPath)
        # 获取case目录路径
        self.appUIPath = os.path.dirname(self.dirPath)
        self.casePath = os.path.join(self.appUIPath, 'case')
        # 获取report目录路径
        self.reportPath = os.path.join(self.appUIPath, 'report')
        # 获取image目录路径
        self.imagePath = os.path.join(self.appUIPath, 'image')
        # 获取page的目录路径
        self.pagePath = os.path.join(self.appUIPath, 'page')

    # 打尺用例路径
    def get_case_foot_path(self):
        return os.path.join(self.casePath, 'foot')

    # 集港用例路径
    def get_case_collection_path(self):
        return os.path.join(self.casePath, 'collection')
