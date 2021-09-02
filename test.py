import uiautomator2

driver = uiautomator2.connect('SQRNW17927003213')
while True:
    print(driver.toast.get_message())
