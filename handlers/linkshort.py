from requests import get as sget



shortner_api_link = #os.environ.get('SHORTNER_LINK')
shortner_api = #os.environ.get('SHORTNER_API')

async def Short(url):
    data = {}
    data['api'] = shortner_api
    data['url'] = url
    data['format'] = 'text'
    link = sget(shortner_api_link, params = data).text
    return link