import json
import os
import requests

token = ""  # 写你钉钉机器人token

headers_info = {
    # 添加了正常的UA
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

headers = {"Content-Type": "application/json"}

# 获取当前IP和用户名
login_info = "root     pts/7        2024-03-07 16:37 (27.38.129.203)" # os.popen("who am i").read()
# 解析IP地址
ssh_ip = login_info.split()[-1].strip("()")
ssh_name = login_info.split()[0].strip("()")
# 获取IP信息
info_url = f"https://whois.pconline.com.cn/ipJson.jsp?ip={ssh_ip}&json=true"
info_urls = requests.get(info_url, headers=headers_info)
info_json = json.loads(info_urls.text.strip())

test = f"""

**您的香港云主机登录提示！!  **

**登录用户: {ssh_name}**

**IP: {info_json['pro']}**

**登录地址: {info_json['pro']}{info_json['city']}**

**运营商: {info_json['addr']}**

**请注意查收哦 ~**
"""

json_text = {
    "at": {
        "isAtAll": True
    },
    "text": {
        "content": test,
    },
    "msgtype": "text"
}
# 调用钉钉机器人API
data = json.dumps(json_text).encode(encoding="utf-8")
url_dingding = "https://oapi.dingtalk.com/robot/send?access_token=" + token
url_post = requests.post(url_dingding, headers=headers, data=data)
