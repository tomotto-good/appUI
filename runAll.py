import unittest
import time
from BeautifulReport import BeautifulReport as bf
from common import getPath

g = getPath.GetPath()


def _runALL():
    # 组装测试套件
    suite = unittest.defaultTestLoader.discover(g.casePath, pattern="test*")
    # 运行测试套件并生成测试报告
    reportPath = g.reportPath + r'\莫斯APP测试报告{}.html'.format(time.strftime("%Y_%m_%d"))
    with open(reportPath, "wb") as f:
        runner = bf(suite)
        runner.report(filename=r'report\莫斯APP测试报告{}.html'.format(time.strftime("%Y_%m_%d")), description='莫斯APP测试')
        f.close()


if __name__ == '__main__':
    _runALL()
