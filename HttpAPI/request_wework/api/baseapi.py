from string import Template

import requests
import yaml


class BaseApi:

    def send(self,data):
       return requests.request(**data).json()

    def template(self,userid,name,mobile):
        with open("../api/member_request.yaml") as f:
            req = {
            "access_token": self.token,
            "userid": userid,
            "name": name,
            "mobile": mobile
            }
            req_result = Template(f.read()).substitute(req)
            return yaml.safe_load(req_result)