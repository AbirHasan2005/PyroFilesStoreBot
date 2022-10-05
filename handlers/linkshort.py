from requests import get as sget
from configs import Config
async def Short(url):
    data = {}
    data['api'] = shortner_api
    data['url'] = url
    data['format'] = 'text'
    link = sget(shortner_api_link, params = data).text
    return link
