# -*- coding: UTF-8 -*-

# import os
# os.system('"/usr/bin/firefox" https://www.louisvuitton.cn/zhs-cn/products/pochette-accessoires-monogram-005656')



from selenium.webdriver.common.keys import Keys
# import selenium.options as options
from selenium import webdriver
import time

option = webdriver.ChromeOptions()
option.add_experimental_option('useAutomationExtension', False)
option.add_experimental_option("excludeSwitches", ['enable-automation'])
option.add_argument("ignore-certificate-errors")
option.add_argument("--ignore-ssl-errors")

browser = webdriver.Chrome(options=option)

# browser = webdriver.Chrome()
# browser.get("https://www.louisvuitton.cn/zhs-cn/products/pochette-accessoires-monogram-005656")

# options.addArguments("--user-data-dir="+System.getenv("USERPROFILE")+"/AppData/Local/Google/Chrome/User Data/Default");

browser.set_page_load_timeout(10)
browser.set_script_timeout(10)
#try去get
try:
  browser.get("https://secure.louisvuitton.cn/zhs-cn/cart")
except:
  print("加载页面太慢，停止加载，继续下一步操作")
  browser.execute_script("window.stop()")

# browser.get("https://www.louisvuitton.cn/zhs-cn/products/short-sleeved-asymmetric-dress-with-frills-nvprod1800016v")


# time.sleep(10)
print("HI")
# browser.find_element_by_id('searchHeaderInput').send_keys('hi')
# browser.find_element_by_id('autocompletionResultPageTop').click()
# browser.find_element_by_id('addToCartSubmit').click()


print("HI")
# browser.find_element_by_class('shareButton btnShare js-tracking shareBinded').click()
# browser.find_element_by_id('clientService_1').click()
browser.find_element_by_id('continueShoppingTop').click()



print("HI")


# browser.find_element_by_id('addToCartSubmit').click()



# browser.close()



# driver = webdriver.Chrome()
# driver.get('http://www.baidu.com')
# time.sleep(3)
# # 找到输入框 并且输入指定内容
# print(30)
# driver.find_element_by_id('kw').send_keys('selenium')
# print(3)
# time.sleep(3)
# # ctrl+a 全选输入框的全部内容
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
# time.sleep(3)
# # 清除输入框内容
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')
 
# time.sleep(3)
# driver.find_element_by_id('kw').send_keys(u'曹羽')
# time.sleep(3)
# driver.find_element_by_id('su').click()
 
# time.sleep(3)
# 退出浏览器
# driver.quit()
