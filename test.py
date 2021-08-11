import uiautomator2
from base.base import Base

driver = uiautomator2.connect_adb_wifi('192.168.1.162')
print(driver.info)
