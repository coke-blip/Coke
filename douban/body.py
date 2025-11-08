# 导入所需模块：
# requests：用于发送HTTP网络请求
# Request（自定义模块head）：用于构造请求头
# json：处理JSON数据的解析与序列化
# time：添加请求延时，规避反爬机制
import requests
from head import Request
import json
import time


# 核心思想:
# 1、获取封装的请求头，请求数据
# 2、将获取返回的数据存储到json文件，筛选出需要的文件数据
# 3、将数据进行解析
# 4、存储/输出最终数据

class Home():
    def __init__(self):
        # 实例化Request类，用于获取豆瓣接口所需的请求头（如User-Agent、Cookie等）
        self.re = Request()
        # 豆瓣“近期热门电影”API的基础URL，`start=`用于分页控制
        self.base_url = "https://m.douban.com/rexxar/api/v2/subject/recent_hot/movie?start="
        # 创建Session对象，用于保持会话（自动管理Cookie）并统一设置请求头
        self.session = requests.Session()
        self.session.headers.update(self.re.headers())  # 加载自定义请求头

    def get_url(self, sta, end):
        responses = []
        print("---状态🐎200为正常请求！---")
        # 循环请求分页数据（此处仅请求第1页，range(1,2)表示page取1）
        for page in range(sta, end + 1):
            # 休眠1秒，模拟人类操作频率，降低被反爬拦截的风险
            time.sleep(1)
            # 计算当前页的start参数（每页20条数据，第1页start=0）
            stare = (page - 1) * 20
            print(f"正在获取第{page}页数据...")
            # 拼接完整请求URL，包含分页、数量限制、鉴权参数（ck需确保有效）
            url = f"{self.base_url}{stare}&limit=20&ck=GmXn"
            # 发送GET请求
            response = self.session.get(url)
            responses.append(response)
            # 打印响应状态码，确认请求是否成功（200为正常）
            print("响应状态🐎为：", response.status_code)
        return responses

    def store(self, responses):
        all_items = []
        for response in responses:
            # 将原始响应内容写入JSON文件，用于备份或调试
            with open("原始响应数据.json", "w", encoding="utf-8") as fp:
                fp.write(response.text)

            # 读取原始JSON数据，解析为Python字典
            with open("原始响应数据.json", "r", encoding="utf-8") as fp:
                original_data = json.load(fp)
            # 提取JSON中“items”字段（电影条目列表），若不存在则返回空列表
            items_only = original_data.get("items", [])
            all_items.extend(items_only)  # 合并当前页电影数据到总列表
        # 将所有页的电影数据保存为JSON文件，供参考
        with open("all_items数据.json", "w", encoding="utf-8") as f:
            json.dump(all_items, f, ensure_ascii=False, indent=4)
        return all_items  # 返回所有筛选好的items数据

    def analyze(self, all_items):
        # 用于存储最终提取的有用信息
        useful_info = []
        page = 0
        # 遍历每部电影的字典，逐个提取信息
        for movie in all_items:  # 调用封装的store()函数
            # 提取评分信息：包含评分值、评价数等
            rating = movie.get("rating", {})  # 若rating字段不存在，返回空字典
            score = rating.get("value", "无评分")  # 评分值，默认“无评分”
            vote_count = rating.get("count", 0)  # 评价数，默认0

            # 提取电影标题，默认“未知标题”
            title = movie.get("title", "未知标题")

            # 提取海报图片链接：大图和小图
            pic = movie.get("pic", {})  # 若pic字段不存在，返回空字典
            large_pic = pic.get("large", "无大图链接")  # 大图链接，默认“无大图链接”
            normal_pic = pic.get("normal", "无小图链接")  # 小图链接，默认“无小图链接”

            # 解析影片详情（年份、国家、类型、导演、演员）
            card_subtitle = movie.get("card_subtitle", "")  # 原始详情字符串，如“2025 / 韩国 / 喜剧 惊悚 犯罪 / 卞成贤 / 薛景求 红炅”
            details = card_subtitle.split(" / ") if card_subtitle else []  # 按“/”拆分字符串为列表
            # 逐个提取详情字段，若不存在则设为“未知XXX”
            year = details[0].strip() if len(details) > 0 else "未知年份"
            country = details[1].strip() if len(details) > 1 else "未知国家"
            genre = details[2].strip() if len(details) > 2 else "未知类型"
            director = details[3].strip() if len(details) > 3 else "未知导演"
            cast = details[4].strip() if len(details) > 4 else "未知演员"

            # 提取电影类型标识（如“movie”）和唯一ID
            movie_type = movie.get("type", "未知类型")
            movie_id = movie.get("id", "未知ID")
            page = page + 1

            # 将提取的信息整理为字典，加入结果列表
            useful_info.append({
                f"--------------------当前条数为{page}:": "-------------------",
                "标题": title,
                "评分": score,
                "评价数": vote_count,
                "大图链接": large_pic,
                "小图链接": normal_pic,
                "年份": year,
                "国家": country,
                "类型": genre,
                "导演": director,
                "演员": cast,
                "类型标识": movie_type,
                "电影ID": movie_id,
            })
        print("数据已存储到该目录下的《最终数据.json》文件中！！！")
        return useful_info

    def final(self, useful_info):
        # 将提取的有用信息保存为新的JSON文件，便于后续分析（如可视化、入库等）
        with open("最终数据.json", "w", encoding="utf-8") as f:
            json.dump(useful_info, f, ensure_ascii=False, indent=4)

    def print_final_data(self):
        # 将提取的有用信息输出到控制台，直接查看
        with open("最终数据.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            print(data)
            # 格式化输出，indent控制缩进和换行
            print(json.dumps(data, ensure_ascii=False, indent=4))
