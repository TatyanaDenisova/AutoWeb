import requests
import yaml

with open('config.yaml') as f:
    infodata = yaml.safe_load(f)

urlpost = infodata['urlpost']


def check_post_id(token):
    res_get = requests.get(url=urlpost, headers={"X-Auth-Token": token}, params={"owner": "notMe"})
    return [item['id'] for item in res_get.json()['data']]

