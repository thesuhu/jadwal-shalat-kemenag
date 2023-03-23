import requests
from requests.cookies import RequestsCookieJar

BASE_URL = 'https://bimasislam.kemenag.go.id'


def getCookies():
    cookie_jar = RequestsCookieJar()

    client = requests.Session()
    client.cookies = cookie_jar

    client.get(BASE_URL + '/jadwalshalat')

    return cookie_jar
