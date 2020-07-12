# -*- coding: utf-8 -*-
import json
import time

import math
import selenium
from selenium import webdriver
from Page_testing import cofing

url = cofing.url
driver = webdriver.Chrome()



def class_name(elements=None, element=None):

    if element:
        elem_name = driver.find_element_by_class_name(element)  # 匹配一个
    else:
        elem_name = driver.find_elements_by_class_name(elements)  # 匹配多个
    return elem_name


def input_data(elemen, data):  # 对话框的输入
    elemen.clear()
    elemen.send_keys(data)

def choice(elems,data):
    for i in elems:
        if i.text == data:
            i.click()
            break
def add_comput():
    class_name(element="console-product-name").click()
    class_name(element="el-button").click()
def sign_in():
    driver.get(url)
    driver.maximize_window()
    class_name(element="login").click()
    elem = class_name(elements="input-text")
    input_data(elem[0], cofing.username)  # 输入用户名
    input_data(elem[1], cofing.password)  # 输入密码
    class_name(element="login-btn").click()
    time.sleep(5)
    driver.find_elements_by_xpath('//li[@class="menu-item"]/a')[2].click()
    time.sleep(12)
    class_name(element="node").click()
    time.sleep(3)
    elems = class_name(elements="node-parentnode-content")
    choice(elems,cofing.province)
    elem = class_name(elements="node-inline")
    choice(elem, cofing.resource)
    time.sleep(4)
    class_name(element="console-product-name").click()
    time.sleep(3)
    # class_name(element="el-button").click()
    with open("jsoncookies.txt","w")as f:
        f.write(json.dumps(driver.get_cookies()))

# 创建机器
def establish_mac():
    driver.get("https://console.ctyun.cn/console/index/#/ecm/ecmCreate")
    driver.delete_all_cookies()
    time.sleep(1)
    with open("jsoncookies.txt","r")as f:
        cookies = json.loads(f.read())
    for i in cookies:
        driver.add_cookie(i)
    driver.get("https://console.ctyun.cn/console/index/#/ecm/ecmCreate")
    driver.maximize_window()
    time.sleep(6)
    elem = class_name(elements=" el-input__inner")
    input_data(elem[0], cofing.mac_name)  # 输入主机名称
    input_data(elem[1], cofing.mac_name1)  # 输入主机名称
    elems = class_name(elements="el-input__suffix-inner")
    elems[0].click()
    elem = class_name(elements="el-select-dropdown__item")
    choice(elem,cofing.vcpu)
    elems[1].click()
    elem = class_name(elements="el-select-dropdown__item")
    choice(elem,cofing.memory)
    time.sleep(2)
    class_name(element="el-radio__inner").click()
    time.sleep(2)
    driver.find_element_by_xpath(
        '//label[@class="el-radio-button el-radio-button--mini"]/span[@class="el-radio-button__inner"]').click()
    elem = driver.find_elements_by_xpath('//div[@class="pwd-input el-input el-input--mini"]/input')
    input_data(elem[0], cofing.mac_password)
    input_data(elem[1], cofing.mac_password)

    # ------------鼠标滑动操作---------
    action=selenium.webdriver.common.action_chains.ActionChains(driver)

    #https://www.ctyun.cn/#/safety/overview/
    elem = class_name(element="el-slider__bar")
    action.click_and_hold(elem)
    action.move_by_offset(0,0)
    action.release() # 第三步：释放鼠标
    action.perform() # 执行动作
    elem.click()
    elem=class_name(element="el-button--primary")
    time.sleep(5)
    elem.click()
    time.sleep(5)
    class_name(element="el-checkbox__inner").click()
    class_name(element="el-button--primary").click()
    time.sleep(15)
    elem = class_name(element="el-button--primary")
    elem.click()
    time.sleep(3)
    data = math.ceil(float(class_name(element="-channel-amount").text))
    elems = class_name(elements="el-input__inner")[1]
    input_data(elems, data)
    class_name(element="el-button--primary").click()

# 服务器操作
def the_server(elems1):
    elems1[1].click()  # 服务器
    time.sleep(5)
    # elem =class_name(element="el-input__inner")
    # input_data(elem, cofing.mac_name1)  # 输入机器名字进行查找
    # class_name(element="el-input-group__append").find_element_by_class_name("el-button").click() #查询按钮
    # time.sleep(3)
    # class_name(elements="el-checkbox__inner")[1].click() # 选取机器
    # # 安装agent
    # driver.find_element_by_xpath('//button[@class="el-button changeColor el-button--default"]').click()
    class_name(element="has-gutter").find_elements_by_class_name("is-leaf")[4].click()
    # driver.find_element_by_xpath('//th[@class=el-table_1_column_9     is-leaf]').click()
    time.sleep(1)
    protect=class_name(elements="el-table-filter__list-item")  # 防护状态
    # print(protect[1].text)
    protect[1].click()
    time.sleep(2)
    class_name(element="has-gutter").find_elements_by_class_name("is-leaf")[4].click()
    time.sleep(1)
    protect[2].click()

# 入侵检测
def intrusion_detection(elems1):
    elems1[4].click()
    time.sleep(2)
    class_name(element="p_l_20").click()
    time.sleep(2)
    driver.find_element_by_xpath('//button[@class="el-button createButton el-button--primary"]').click()
    time.sleep(2)
    elem = driver.find_elements_by_xpath('//button[@class="el-button createButton el-button--default"]')
    time.sleep(1)
    for i in elem:
        i.click()
        time.sleep(2)
        # dialog_box=driver.switch_to_alert.accept()
        # dialog_box = driver.switch_to_active_element()
        time.sleep(2)
        # class_name(element="dialogloginArea1").find_elements_by_class_name("el-select")[1].click()
        time.sleep(6)
        # ele = driver.find_elements_by_xpath('//div[@class="el-scrollbar"]/div[@class="el-scrollbar"]/div[@class="el-select-dropdown__wrap el-scrollbar__wrap"]/ul[@class="el-scrollbar__view el-select-dropdown__list"]//li[@class="el-select-dropdown__item"]/span')
        # for j in ele:
        #     if j.text==u"黑龙江省":
        #         j.click()
        time.sleep(4)
        driver.find_element_by_class_name('//div[@class="el-input el-input--suffix"]/span[@class="el-input__suffix"]/span[@class="el-input__suffix-inner"]').click()
        # driver.quit()
        a = driver.find_elements_by_xpath('//ul[@class="el-scrollbar__view el-select-dropdown__list"]/li[@class="el-select-dropdown__item"]/span')
        for j in a:
            print(j.text)
        f = driver.find_elements_by_xpath('//button[@class="el-button f_btn f_btn_r el-button--default"]/span')
        print(f[1].text)
        break

# 服务器安全卫士
def cloud_security():
    driver.get("https://console.ctyun.cn/console/index/#/console")
    driver.maximize_window()
    driver.delete_all_cookies()
    time.sleep(1)
    with open("jsoncookies.txt", "r")as f:
        cookies=json.loads(f.read())
    for i in cookies:
        driver.add_cookie(i)
    driver.get("https://console.ctyun.cn/console/index/#/console")
    driver.maximize_window()
    time.sleep(8)
    elem = class_name(elements="console-product-productsList")[1].find_element_by_class_name("console-product-subtitle").click()
    time.sleep(40)
    windows=driver.window_handles  # 获取当前的所有窗口
    driver.switch_to.window(windows[-1])   # 切换到最新打开的窗口
    time.sleep(2)
    elems1 = driver.find_elements_by_xpath('//ul[@class="sub-menu"]/ul')  # 左侧列表
    intrusion_detection(elems1) # 入侵检测
    # the_server(elems1)  # 服务器器操作

if __name__=="__main__":
    # sign_in()  # 登录保存cookie
    # establish_mac()  # 添加机器
    cloud_security()   # 服务器安全卫士