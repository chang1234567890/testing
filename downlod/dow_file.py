# coding:utf-8
import json
import datetime
import requests
import sys
import hashlib
import shutil
import os
import gzip
import urllib2
import bz2
dowl = "file/new_file/new.txt"
reload(sys)
sys.setdefaultencoding("utf-8")
requests.packages.urllib3.disable_warnings()
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

centos_url = "https://access.redhat.com/labs/securitydataapi/cve.json?after=2010-01-01&per_page=1000&page="
centos_url_18 = "https://access.redhat.com/labs/securitydataapi/cve.json?after=2010-01-01&per_page=1000&page=18"

ubuntu12_url = "https://people.canonical.com/~ubuntu-security/oval/com.ubuntu.precise.cve.oval.xml"
ubuntu14_url = "https://people.canonical.com/~ubuntu-security/oval/com.ubuntu.trusty.cve.oval.xml"
ubuntu16_url = "https://people.canonical.com/~ubuntu-security/oval/com.ubuntu.xenial.cve.oval.xml"
ubuntu18_url = "https://people.canonical.com/~ubuntu-security/oval/com.ubuntu.bionic.cve.oval.xml"

debian7_url = "https://www.debian.org/security/oval/oval-definitions-wheezy.xml"
debian8_url = "https://www.debian.org/security/oval/oval-definitions-jessie.xml"
debian9_url = "https://www.debian.org/security/oval/oval-definitions-stretch.xml"
debian10_url = "https://www.debian.org/security/oval/oval-definitions-buster.xml"

windowsXP_url = "https://oval.cisecurity.org/repository/download/5.11.2/vulnerability/microsoft_windows_xp.xml"
windows7_url = "https://oval.cisecurity.org/repository/download/5.11.2/vulnerability/microsoft_windows_7.xml"
windows8_url = "https://oval.cisecurity.org/repository/download/5.11.2/vulnerability/microsoft_windows_8.xml"
windows8_1_url = "https://oval.cisecurity.org/repository/download/5.11.2/vulnerability/microsoft_windows_81.xml"
windows10_url = "https://oval.cisecurity.org/repository/download/5.11.2/vulnerability/microsoft_windows_10.xml"
windows_server_2008_url = "https://oval.cisecurity.org/repository/download/5.11.2/vulnerability/microsoft_windows_server_2008.xml"
windows_year = "https://nvd.nist.gov/feeds/json/cve/1.0/nvdcve-1.0-%d.json.gz"
dict_url = {
    windows_year: "file/windows/Windows",
    centos_url: "file/centos/CentOS",
    #ubuntu12_url: "file/ubuntu/Ubuntu12.txt",
    ubuntu14_url: "file/ubuntu/Ubuntu14.txt",
    ubuntu16_url: "file/ubuntu/Ubuntu16.txt",
    ubuntu18_url: "file/ubuntu/Ubuntu18.txt",
    debian7_url: "file/debian/Debian7.txt",
    debian8_url: "file/debian/Debian8.txt",
    debian9_url: "file/debian/Debian9.txt",
    debian10_url: "file/debian/Debian10.txt"
    #windowsXP_url: "file/windows/windowsXP.txt",
    #windows7_url: "file/windows/windows7.txt",
    #windows8_url: "file/windows/windows8.txt",
    #windows8_1_url: "file/windows/windows8_1.txt",
    #windows10_url: "file/windows/windows10.txt",
    #windows_server_2008_url: "file/windows/windows_server_2008.txt"
}


# 打印log
def day_time(value):
    now = datetime.datetime.now()
    date = str(now.strftime('%Y-%m-%d %H:%M:%S'))
    print value+"\t"+date
    f = open("log.log", "a+")
    f.write(value+"\t"+date+"\n")
    f.close()


# md5加密
def mad5_ency(valu):
    md5_obj = hashlib.md5()
    md5_obj.update(valu.encode("utf-8"))
    return md5_obj.hexdigest()


# 替换文件
def open_wil(add, values):
    with open(add, "w") as f:
        f.write(values)
        f.close()


# 读取文件
def open_read(add):
    with open(add, 'r') as f:
        yesterday_data = f.read()
        f.close()
    if len(yesterday_data) <= 2:
        return None
    mad5_yesterday = mad5_ency(yesterday_data)
    return mad5_yesterday


# 替换合并后的文件
def replace_file(num):
    lists = []
    for i in range(1, num):
        file_name = "file/centos/CentOS" + str(i) + ".txt"
        f = open(file_name, "r")
        val = f.read()
        f.close()
        data = json.loads(val)
        lists += data
    values = json.dumps(lists)
    open_wil("file/centos/CentOS.txt", values)


def requs(url, file_paths):
    if os.path.exists(file_paths):
        temp_size = os.path.getsize(file_paths)
    else:
        temp_size = 0
    headers = {'Range': 'bytes=%d-' % temp_size}
    r = requests.get(url, stream=True, verify=False, headers=headers, timeout=20)
    return r


def centos_data(urls, file_name):
    num = 0
    replaces = False
    while True:
        with open(dowl, "a+") as fd:
            fd.truncate()
            fd.close()
        num += 1
        url = urls + str(num)
        file_names = file_name + str(num) + ".txt"
        day_time(url)
        while True:
            try:
                data = requs(url, dowl)
                with open(dowl, "a+") as fd:
                    for chunk in data.iter_content(chunk_size=500):
                        fd.write(chunk)
                break
            except:
                f = open(dowl, "w")
                f.truncate()
                f.close()
                pass
        md5_data = open_read(dowl)
        if md5_data:
            try:  # 读数据，报错没这个文件，侧从新写入文件
                md5_yesterdays = open_read(file_names)
                if md5_yesterdays != md5_data:
                    replaces = True
                    shutil.move(dowl, file_names)
                    day_time(file_names+u" 与之前MD5加密后不等-已替换 ")
                else:
                    os.remove(dowl)
                    day_time(file_names+u" 与之前MD5加密后相等-未替换 ")
            except:
                replaces = True
                shutil.move(dowl, file_names)
                day_time(file_names+u" 没有此文件已写入 ")
        else:
            day_time(u"此页面无数据未写入")
            break
    # 如果有文件被更改，从新替换合并的文件
    if replaces:
        replace_file(num)
        day_time(u" CentOS.txt文件-已替换 ") 
    else:
        day_time(u" CentOS.txt文件-未替换 ")


def obtain_data(url, file_name):
    with open(dowl, "a+") as fd:
        fd.truncate()
        fd.close()
    day_time(url)
    start = True
    while start:
        try:
            requ = requs(url, dowl)
            with open(dowl, "a+") as fd:
                for chunk in requ.iter_content(chunk_size=100):
                    if chunk:
                        fd.write(chunk)
                fd.close()
            data = open_read(dowl)
            # md5_data = mad5_ency(data)
            if data:
                try:
                    md5_yesterdays = open_read(file_name)
                    if md5_yesterdays != data:
                        shutil.move(dowl, file_name)
                        day_time(file_name+u" 与之前MD5加密后不等-已替换 ")

                    else:
                        os.remove(dowl)
                        day_time(file_name+u" 与之前MD5加密后相等-未替换 ")

                except:
                    shutil.move(dowl, file_name)
                    day_time(u" 没有%s文件已从新写入 " % file_name)

            else:
                day_time(u" 网址没有数据 ")
            start = False
        except:
            with open(dowl, "a+") as fd:
                fd.truncate()
                fd.close()
            pass
def ubuntuss(urls, file_name):
    with open(dowl, "a+") as fd:
        fd.truncate()
        fd.close()
    day_time(urls)
    start = True
    while start:
        try:
            data = urllib2.urlopen(urls,timeout=180)
            with open(dowl, "a+") as fd:
                fd.write(bz2.decompress(data.read()))
                fd.close()
            data = open_read(dowl)
            if data:
                try:
                    md5_yesterdays = open_read(file_name)
                    if md5_yesterdays != data:
                        shutil.move(dowl, file_name)
                        day_time(file_name + u" 与之前MD5加密后不等-已替换 ")

                    else:
                        os.remove(dowl)
                        day_time(file_name + u" 与之前MD5加密后不等-未替换 ")

                except:
                    shutil.move(dowl, file_name)
                    day_time(u" 没有%s文件已从新写入 " % file_name)

            else:
                day_time(u" 网址没有数据 ")
            start = False
        except:
            with open(dowl, "a+") as fd:
                fd.truncate()
                fd.close()
        pass
def windowsyear(urls, file_name):
    num = 2009
    starts = 1
    while starts:
        num += 1
        url = urls % num
        file_names = file_name + str(num) + ".json.gz"
        day_time(url)
        while True:
            try:
                data = urllib2.urlopen(url)
                with open(file_names, "wb") as code:
                    code.write(data.read())
                f_name=file_names.replace(".json.gz", ".txt")
                g_file=gzip.GzipFile(file_names)
                # # 创建gzip对象
                open(f_name, "w").write(g_file.read())
                # gzip对象用read()打开后，写入open()建立的文件里。
                g_file.close()
                os.remove(file_names)
                break
            except:
                years = datetime.datetime.now().year
                if years < num:
                    starts = 0
                    break
                pass



# 启动程序
def start_program():

    for i in dict_url:
        if dict_url[i] == "file/centos/CentOS":
            centos_data(i, dict_url[i])
        elif dict_url[i] == "file/windows/Windows":
            windowsyear(i, dict_url[i])
        elif "file/ubuntu/" in dict_url[i]:
            ubuntuss(i,dict_url[i])
        else:
            obtain_data(i, dict_url[i])

    day_time(u"爬取比较完毕")


if __name__ == "__main__":
    start_program()
