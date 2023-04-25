import requests
import json


class Douyu(object):
    def __init__(self):
        self.url = f'https://www.douyu.com/gapi/rkc/directory/mixList/0_0/1'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'
                          ' (KHTML, like Gecko) Chrome/108.0.5359.95 Safari/537.36',

            'referer': "https://www.douyu.com/directory/all"

        }

    def gate_data(self):
        response = requests.get(url=self.url, headers=self.headers)
        js = json.loads(response.text)
        # print(js['data']['rl']['rt'])
        for page_text in js['data']['rl']:
            dict_temp = {
                '标题': page_text['rn'],
                '类型': page_text['c2name'],
                '主播': page_text['nn'],
                '热度': page_text['ol'],
                'od': page_text['od'],
                '房间号': page_text['rid'],
                'url': 'https://www.douyu.com/' + page_text['url']
            }
            print(dict_temp)

    def run(self):
        self.gate_data()


if __name__ == '__main__':
    Douyu().run()
