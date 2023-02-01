import requests         # pip install requests
import json
import pandas as pd

# Make GET request to site
appended_data = []
count = 60
anchor = 0
country = 'GB'
country_language = 'en-GB'
query = pd.read_csv(r"C:\Saud\Nike Scrapper\products_list.csv")
df  = query['style']
print(df)
for styles in df:
    url = f'https://api.nike.com/cic/browse/v2?queryid=products&anonymousId=241B0FAA1AC3D3CB734EA4B24C8C910D&country={country}&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace({country})%26filter%3Dlanguage({country_language})%26filter%3DemployeePrice(true)%26searchTerms%3D{styles}%26anchor%3D{anchor}%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D{count}&language={country_language}&localizedRangeStr=%7BlowestPrice%7D%E2%80%94%7BhighestPrice%7D'
    html = requests.get(url=url)
    output = json.loads(html.text)
    # print(output)
    try:
        for item in output['data']['products']['products']:
            name = item['title'],
            subtitle = item['subtitle'],
            currenr_price = item['price']['currentPrice'],
            Final_price = item['price']['fullPrice'],
            image = item['images']['portraitURL']
            # cloud_ID = item['cloudProductId']
            # print(cloud_ID)
            print(name,subtitle,currenr_price,Final_price,image)
            data = {
                'name': name,
                'Subtitle': subtitle,
                'Current Price': currenr_price,
                'Final_price': Final_price,
                'image': image,
                'styles': styles,
                # 'cloud_ID': cloud_ID
            }
            df = pd.DataFrame(data)
            appended_data.append(df)
    except:
        print("No data found")
appended_data = pd.concat(appended_data)
appended_data.to_csv(r"Nike.csv",index=False)
