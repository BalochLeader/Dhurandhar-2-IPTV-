#It Is Program To Generate m3u link 

#program by BalochLeader

import requests

headers = {
    'accept': '*/*',
    'accept-language': 'en-GB',
    'origin': 'https://ekola405gmt.com',
    'priority': 'u=1, i',
    'referer': 'https://ekola405gmt.com/',
    'sec-ch-ua': '"Chromium";v="127", "Not)A;Brand";v="99", "Microsoft Edge Simulate";v="127", "Lemur";v="127"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36',
}

response = requests.get(
    'https://cdn30092.lafix409dos.com/stream2/i-cdn-0/fa3771e985d03f34dc251eab415cce43/MJTMsp1RshGTygnMNRUR2N2MSlnWXZEdMNDZzQWe5MDZzMmdZJTO1R2RWVHZDljekhkSsl1VwYnWtx2cihVT21ERGpmWqpFaZRVSx0EVWhmTHlEeN1WUykVbVVzTXZVaZpGbt1UbK1WT6lUP:1774542583:27.34.69.101:e3d15d11d6e7eeff72b49aa190e3330c3a4de9b7d60188cb43a41eab93364f17:==QTqNWdNpXU15karVXTUFEe/720/index.m3u8',
    headers=headers,
)


print(response.text)
