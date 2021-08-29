import requests
import yaml


class EnvApi:
    #读取yaml配置文件中env数据
    env = yaml.safe_load(open("env.yaml"))

    def send(self, data):
        #将请求url中的域名替换成默认配置环境对应的IP
        data["url"] = str(data["url"]).replace("www.testing.fision", self.env["test-env"][self.env["default"]])
        res = requests.request(**data)
        print(res.text)
        return res
