from requests import get as sget
from configs import Config
async def Short(url):
    data = {}
    data['api'] = Config.SHORTNER_API
    data['url'] = url
    data['format'] = 'text'
    link = sget(Config.SHORTNER_API_LINK, params = data).text
    return link
