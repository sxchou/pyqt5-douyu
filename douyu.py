import json
import datetime
import time
import pandas as pd
import requests
from PyQt5.QtWidgets import QApplication
import config
from pathlib2 import Path
from collections import Counter


class Douyu(object):
    def __init__(self):
        self.url = f'https://www.douyu.com/gapi/rkc/directory/mixList/0_0/'
        self.headers = {
            'User-Agent': f'{config.comboBox_currentText}',

            'referer': "https://www.douyu.com/directory/all"

        }

    @property
    def get_data(self):
        data_list = []
        type_list = []
        i = 0
        for page in range(1, int(config.pages) + 1):
            new_url = self.url + str(page)
            response = requests.get(url=new_url, headers=self.headers)
            js = json.loads(response.text)
            config.ui.textBrowser.append(f'正在爬取第{page}页')
            QApplication.processEvents()
            config.statusBar.showMessage(f'程序正在运行:正在爬取第{page}页')
            jd = int(100 / int(config.pages))
            i += jd
            config.progressBar.setValue(i)
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
                type_list.append(page_text['c2name'])
                data_list.append(dict_temp)
        return data_list, type_list

    @staticmethod
    def save_data(data_list):
        file_dir = Path.cwd().joinpath('douyu_file')
        if not Path.exists(file_dir):
            Path.mkdir(file_dir)
        now_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        a = pd.DataFrame(data_list)
        a.to_excel(f'{file_dir}\\斗鱼主播实时数据{now_time}.xlsx', sheet_name='斗鱼主播实时数据', index=False)

    @staticmethod
    def get_hyper_link(url):
        # 字体、颜色和大小都可以自定义
        # style = "color:#ffb61e;font-size:20px;font-family:Microsoft YaHei"
        return f'<a href="{url}" ><b>{url}</b></a>'

    def parse_data(self, type_list, data_list):
        count_type = Counter(type_list)
        config.ui.textBrowser.append('统计分析：')
        for k, v in count_type.most_common()[:10]:
            data_list1 = []
            for dict_data in data_list:
                if list(dict_data.values())[1] == k:
                    data_list1.append(dict_data)
            data_list1.sort(key=lambda x: x['热度'], reverse=True)
            config.ui.textBrowser.append(f"\n{k}主播共有{v}个:\n{k}主播排名第一的是:{data_list1[0]['主播']}, "
                                         f"热度为：{data_list1[0]['热度']}, 房间号：{data_list1[0]['房间号']}\n"
                                         f"打开斗鱼：{'https://www.douyu.com/'} 输入房间号：{data_list1[0]['房间号']}"
                                         f" 去观看ta,或猛戳下方链接直达👇👇👇👇👇👇")
            config.ui.textBrowser.append(self.get_hyper_link(data_list1[0]['url']))
            config.ui.textBrowser.setOpenExternalLinks(True)
        config.ui.textBrowser.append('这里只展示热门类型和主播，更多请查看生成的excel数据...')

    def run(self):
        data_list, type_list = self.get_data
        self.save_data(data_list)
        config.ui.textBrowser.append(f'爬取完成!共获取{len(data_list)}条主播数据')
        end_time = time.time()
        config.progressBar.setValue(100)
        config.statusBar.showMessage(f'爬取完成!共获取{len(data_list)}条主播数据，文件已保存在douyu_file中。'
                                     + "耗时: {:.2f}秒".format(end_time - config.start_time))
        self.parse_data(type_list, data_list)
