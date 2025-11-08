class head():
    def headeres(self):
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'origin': 'https://movie.douban.com',
            'priority': 'u=1, i',
            'referer': 'https://movie.douban.com/explore',
            'sec-ch-ua': '"Chromium";v="142", "Microsoft Edge";v="142", "Not_A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0',
            # 'cookie': 'll="108309"; bid=oWTM7PyMZBE; _vwo_uuid_v2=D83C884BAE8C92804AED4814F689C0C1B|b0e0820aa438c7a90d7e04b587053a8f; Hm_lvt_6d4a8cfea88fa457c3127e14fb5fabc2=1761745828; _ga=GA1.2.1099734807.1761745829; _ga_Y4GN1R87RG=GS2.1.s1761745829$o1$g1$t1761747484$j60$l0$h0; __utmc=30149280; __utmz=30149280.1762522240.6.2.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; dbcl2="292175041:boATxzdtF2A"; ck=GmXn; push_noty_num=0; push_doumail_num=0; frodotk_db="0723fd84cbb4a9ab156bf88e631dfd01"; frodotk="7ed89c6da1573e307c89d548e405ba90"; talionusr="eyJpZCI6ICIyOTIxNzUwNDEiLCAibmFtZSI6ICJcdTUzZWZcdTRlNTAifQ=="; __utma=30149280.1740551377.1743561669.1762522240.1762525654.7; __utmb=30149280.0.10.1762525654',
        }
        return headers

    def cookie(self):
        cookies = {
            'll': '"108309"',
            'bid': 'oWTM7PyMZBE',
            '_vwo_uuid_v2': 'D83C884BAE8C92804AED4814F689C0C1B|b0e0820aa438c7a90d7e04b587053a8f',
            'Hm_lvt_6d4a8cfea88fa457c3127e14fb5fabc2': '1761745828',
            '_ga': 'GA1.2.1099734807.1761745829',
            '_ga_Y4GN1R87RG': 'GS2.1.s1761745829$o1$g1$t1761747484$j60$l0$h0',
            '__utmc': '30149280',
            '__utmz': '30149280.1762522240.6.2.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
            'dbcl2': '"292175041:boATxzdtF2A"',
            'ck': 'GmXn',
            'push_noty_num': '0',
            'push_doumail_num': '0',
            'frodotk_db': '"0723fd84cbb4a9ab156bf88e631dfd01"',
            'frodotk': '"7ed89c6da1573e307c89d548e405ba90"',
            'talionusr': '"eyJpZCI6ICIyOTIxNzUwNDEiLCAibmFtZSI6ICJcdTUzZWZcdTRlNTAifQ=="',
            '__utma': '30149280.1740551377.1743561669.1762522240.1762525654.7',
            '__utmb': '30149280.0.10.1762525654',
        }
        return cookies