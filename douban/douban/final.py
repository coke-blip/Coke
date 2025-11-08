from body import Body

if __name__ == '__main__':
    home = Body()
    sta = int(input("输入起始页:..."))
    end = int(input("输入结束页:..."))
    responses = home.get_url(sta=sta,end=end)
    all_items = home.store(responses)
    useful_info = home.analyze(all_items)
    final = home.final(useful_info)
