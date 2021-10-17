from string import Template

import requests
import yaml


class BaseApi:

    def send_api(self, req: dict):
        return requests.request(**req).json()

    def template(self, path, data, sub=None):
        with open(path, encoding="utf-8") as f:
            if sub is None:
                return yaml.safe_load(Template(f.read()).substitute(data))
            else:
                return yaml.safe_load(Template(yaml.dump(yaml.safe_load(f)[sub])).substitute(data))
