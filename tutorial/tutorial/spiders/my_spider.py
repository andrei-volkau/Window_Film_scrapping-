import scrapy
import pandas as pd
import json
import random
from ..items import TutorialItem

headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru-BY,ru-RU;q=0.9,ru;q=0.8,en-US;q=0.7,en;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary3nRkyrKMWDP9pvPg',
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
INPUT_FILENAME = "data.csv"


class DusharaSpider(scrapy.Spider):
    name='dushara'

    def start_requests(self):
        df = pd.read_csv(INPUT_FILENAME)
        for index, row in df.iterrows():
            first_zip_value = row["4"].split(" to ")[0]
            second_zip_value = row["4"].split(" to ")[-1]
            url = 'https://iwfa.com/wp-admin/admin-ajax.php'
            codes = list(range(int(first_zip_value), int(second_zip_value)))
            for zip_code in random.sample(codes, 50):
                yield scrapy.FormRequest(
                    url=url,
                    formdata={"lat": "0", "long": "0", "zip": str(zip_code), "nonce": "c47ae0f2e4", "action": "find_dealers"},
                    callback=self.parse
                )

    def parse(self, response):
        json_loaded = json.loads(response.text)
        for item in json_loaded:
            id_value = item["id"]
            country = item["properties"]["country"]
            if country == "United States":
                company_name = item["properties"]["name"]
                phone = item["properties"]["phone"]
                website = item["properties"]["website"]
                state = item["properties"]["state"]
                item = TutorialItem()
                item['id_value'] = id_value
                item['company_name'] = company_name
                item['website'] = website
                item['phone'] =phone
                item['state'] = state
                yield item
