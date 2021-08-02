import time


def unlock_phone(driver):
    if driver.info['screenOn']:
        driver.screen_off()
        time.sleep(2)
    else:
        print('当前设备已解锁')
    print('解锁屏幕..')
    driver.unlock()
    a = 0
    while a < 4:
        driver.click(0.511, 0.728)
        a += 1
