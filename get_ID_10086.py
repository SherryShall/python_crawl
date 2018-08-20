# -*- coding: utf-8 -*
import sys
import xlrd
import urllib
import requests
import os
import ssl
import base64
import matplotlib.pyplot as plt
from PIL import Image

headers = {
     "method": "POST",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"

}

# sichuan

url="http://resources.geetest.com/nerualpic/inspires/5a82c8bc83057c12776876e83277908c.jpg?challenge=053713d71a24b62bfaa49351b51168cc" # sichuan
# url ="https://hb.ac.10086.cn/SSO/img?codeType=0&rand=1525938990975"


for i in range(10000):
    if len(str(url)) != 0:
        path = 'D:/2018.8.13/sample/'
        filename = '%s.png' % (int(i))
        img_file = path + filename
        print i

        session = requests.Session()
        # response = session.get(url,verify=False)
        response = session.get(url, headers=headers)
        lens = len(response.content)
        # # lenx = lens - (lens % 4 if lens % 4 else 4)
        # result_start = response.content[117]
        # result_end = response.content[-33:-30]
        # print result_start
        # print result_end

        import json
        with open(img_file, 'wb') as f:
            if response.content:
                print("success")
                print(response.content)
                f.write(response.content)

                # image = Image.open(response.content)
                # image.show()
                # f.write(response.content.decode(encoding="UTF-8"))
                # f.write(base64.decodestring(response.content[22:lens])) #tianjin
                # response_dict = json.loads(response.content)
                # response_str = response_dict.get("resultObj")
                #
                # f.write(base64.decodestring(response.content[117:-30])) #sichuan
                # f.write(base64.decodestring(response_str)) #sichuan
                f.flush()
                f.close()


# url="http://tj.ac.10086.cn/captcha.htm?token=3AMFUflys2OJx5tPtipmKQ8V3JmY5dWeU&_=0.010553174081280314"


# for i in range(1):
#     if len(str(url)) != 0:
#         path = 'D:\PyCharm Files\Conda\image_download\\10086tianjin_new\c'
#         filename = '%s.png' % (int(i))
#         img_file = path + filename
#         print i
#
#         session = requests.Session()
#         # response = session.get(url,verify=False)
#         response = session.get(url, headers=headers)
#         lens = len(response.content)
#         # a = base64.decodestring(response.content[40:lens])
#         # # lenx = lens - (lens % 4 if lens % 4 else 4)
#         # result_start = response.content[21]
#         # # result_end = response.content[-31]
#         # print result_start
#
#
#         with open(img_file, 'wb') as f:
#             if response.content:
#                 f.write(response.content) #normal
#                 f.write(base64.decodestring(response.content[22:lens])) #tianjin
#                 # f.write(base64.decodestring(response.content[40:lens])) #anhui
#                 f.flush()
#                 f.close()
#             #res2 = urllib.urlretrieve(str(url), path)
