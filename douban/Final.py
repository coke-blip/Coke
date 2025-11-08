from body import Home

if __name__ == '__main__':
    sta = int(input("输入起始页..."))
    end = int(input("输入结束页..."))
    home = Home()
    responses = home.get_url(sta=sta, end=end)  # 先获取响应
    all_items = home.store(responses)  # 传入响应处理存储
    useful_info = home.analyze(all_items)  # 传入电影数据解析
    home.final(useful_info)  # 传入解析结果到文件：最终数据.json 中存储
    # home.print_final_data()  # 输出到控制台

