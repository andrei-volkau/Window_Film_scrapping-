import requests

cookies = {
    '_gid': 'GA1.2.2058559134.1673960702',
    '_gat_UA-128306984-1': '1',
    '_ga_6CTHZLKJPL': 'GS1.1.1673965075.2.1.1673965075.0.0.0',
    '_ga': 'GA1.1.1966458327.1673960702',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru-BY,ru-RU;q=0.9,ru;q=0.8,en-US;q=0.7,en;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryBVzbJfnb56pQWUMq',
    # 'Cookie': '_gid=GA1.2.2058559134.1673960702; _gat_UA-128306984-1=1; _ga_6CTHZLKJPL=GS1.1.1673965075.2.1.1673965075.0.0.0; _ga=GA1.1.1966458327.1673960702',
    'Origin': 'https://iwfa.com',
    'Referer': 'https://iwfa.com/dealer-locator/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

data = '------WebKitFormBoundaryBVzbJfnb56pQWUMq\r\nContent-Disposition: form-data; name="lat"\r\n\r\n0\r\n------WebKitFormBoundaryBVzbJfnb56pQWUMq\r\nContent-Disposition: form-data; name="long"\r\n\r\n0\r\n------WebKitFormBoundaryBVzbJfnb56pQWUMq\r\nContent-Disposition: form-data; name="zip"\r\n\r\n10001\r\n------WebKitFormBoundaryBVzbJfnb56pQWUMq\r\nContent-Disposition: form-data; name="nonce"\r\n\r\nc47ae0f2e4\r\n------WebKitFormBoundaryBVzbJfnb56pQWUMq\r\nContent-Disposition: form-data; name="action"\r\n\r\nfind_dealers\r\n------WebKitFormBoundaryBVzbJfnb56pQWUMq--\r\n'

response = requests.post('https://iwfa.com/wp-admin/admin-ajax.php', headers=headers, data=data)
print(response)
print(response.text)