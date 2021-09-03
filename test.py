import uiautomator2

driver = uiautomator2.connect('926QADV7222QM')
a = driver.exists(text='鲁D 003的装车报告.pdf')
assert a, True
