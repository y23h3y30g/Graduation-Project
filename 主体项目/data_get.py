import requests
import json
import re
import time
#page=1103&num=10

if __name__ == "__main__":
    with open('数据集.txt','w',encoding='utf-8'):
        pass
    url = 'https://pacaio.match.qq.com/virus/trackList'
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15'
    }
    i = 0
    while i < 1103:
        param = {
            'page': str(i),
            'num': '10',
        }
        i += 1
        response = requests.get(url=url,params=param,headers=headers).text


        ex = '"user_name"(.*?)","pub_time"'

        # ex = '"user_name".*?:(\\\\)?"(.*?)(\\\\)?"\}?.*?]","pub_time"'
        url_data_list = re.findall(ex,response,re.S)



        text1 = "".join(url_data_list)



        ex1 = ':\\\\?"(.*?)\\\\?"\}?'

        url_data_list1 = re.findall(ex1, text1, re.S)



        text2 = "".join(url_data_list1)



        a = re.findall(r'[^{\[]', text2, re.S)
        a = "".join(a)
        print(i)
        with open('./数据集.txt','a',encoding='utf-8') as fp:
            fp.write(a)
        time.sleep(3)
        # print(url_data_list1)
        # for url_data in url_data_list1:
        #     print(url_data)

    # list_data = response.json()
    #
    # with open('./test_data.json','w',encoding='utf-8') as fp:
    #     json.dump(list_data,fp=fp,ensure_ascii=False)
