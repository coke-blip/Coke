import requests
import json
import time
from head import head


class Body():
    def __init__(self):
        self.re = head()
        self.base_url = "https://m.douban.com/rexxar/api/v2/subject/recent_hot/movie?start="
        self.session = requests.Session()
        self.session.headers.update(self.re.headeres())

    def get_url(self, sta, end):
        responses = []
        for page in range(sta, end):
            time.sleep(1)
            stare = (sta - 1) * 20
            url = f"{self.base_url}{stare}&limit=20&ck=GmXn"
            print(f"当前正在爬取{page}页的数据...")
            response = self.session.get(url)
            responses.append(response)
            print("---状态🐎200为正常请求！---")
            print(f"请求状态🐎为：{response.status_code}")
        return responses

    def store(self, responses):
        all_items = []
        for response in responses:
            with open("response.json", "w", encoding="utf-8") as fp:
                fp.write(response.text)

            with open("response.json", "r", encoding="utf-8") as f:
                account = json.load(f)
            imp = account.get("items", [])
            all_items.extend(imp)
        return all_items

    def analyze(self, all_items):
        page = 0
        useful_info = []
        for move in all_items:
            rating = move.get("rating", {})
            value = rating.get("value", "0")
            count = rating.get("count", "0")

            title = move.get("title", "无名称")

            pic = move.get("pic", {})
            large = pic.get("large", "暂无网址")
            normal = pic.get("normal", "暂无网址")

            type = move.get("type", "暂无类型")

            card_subtitle = move.get("card_subtitle", "0")
            date = card_subtitle.split("/") if card_subtitle else []
            year = date[0].strip() if len(date) > 0 else "未知年份"
            country = date[1].strip if len(date) > 0 else "未知国家"
            sort = date[2].strip if len(date) > 0 else "未知种类"
            director = date[3].strip if len(date) > 0 else "未知导演"
            cast = date[4].strip if len(date) > 0 else "未知演员"
            page = page + 1

            useful_info.append({
                "当前页数：": page,
                "标题": title,
                "评分": value,
                "大图链接": large,
                "小图链接": normal,
                "种类": type,
            })
        print("数据已存储到该目录下的《最终数据.json》文件中！！！")
        return useful_info

    def final(self, useful_info):
        with open("最终数据.json", "w", encoding="utf-8") as f:
            json.dump(useful_info, f, ensure_ascii=False, indent=4)
