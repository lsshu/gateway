import requests

token = '???'  # 百度链接推送提供的token
site = 'www.abc.cn'  # 自己的域名

create_link_url = 'http://data.zz.baidu.com/urls?site={}&token={}&type=original'.format(site, token)  # 推送
update_link_url = 'http://data.zz.baidu.com/update?site={}&token={}'.format(site, token)  # 更新
delete_link_url = 'http://data.zz.baidu.com/del?site={}&token={}'.format(site, token)  # 删除


def push_urls(url, urls):
    """
    根据百度站长提供的API推送链接
    :param url: 百度提供的推送、更新、删除接口
    :param urls:
    :return:
    """
    headers = {
        'User-Agent': 'curl/7.12.1',
        'Host': 'data.zz.baidu.com',
        'Content - Type': 'text / plain',
        'Content - Length': '83'
    }

    try:
        r = requests.post(url, headers=headers, data='\n'.join(urls), timeout=5).text
        print('blog signals.py中调用百度链接提交结果：', r)
        return r
    except BaseException as e:
        print('blog signals.py中调用百度链接提交失败：', str(e))
        return str(e)


if __name__ == '__main__':
    # 测试
    urls = [
        'https://blog.starmeow.cn/detail/82161242827b703e6acf9c726942a1e/',
        'https://blog.starmeow.cn/detail/96da2f590cd7246bbde0051047b0d6f/',
    ]
    result = push_urls(create_link_url, urls)
    print(result)  # {"remain":4999988,"success":2}  # 当天剩余的可推送url条数；成功推送的url条数

"""
{
    "remain":4999998,  当天剩余的可推送url条数
    "success":2,  成功推送的url条数
    "not_same_site":[],  由于不是本站url而未处理的url列表
    "not_valid":[]  不合法的url列表
}
"""
