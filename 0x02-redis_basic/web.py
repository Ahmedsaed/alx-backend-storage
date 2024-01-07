#!/usr/bin/env python3
""" Implementing an expiring web cache and tracker
    obtain the HTML content of a particular URL and returns it """
import redis
import requests
r = redis.Redis()


def get_page(url: str) -> str:
    """ track how many times a particular URL was accessed in the key
        "count:{url}"
        and cache the result with an expiration time of 10 seconds """
    cached_result = r.get(f'cache:{url}')
    if cached_result:
        r.incr(f'count:{url}')
        return cached_result.decode('utf-8')

    resp = requests.get(url)

    r.setex(f'cache:{url}', 10, resp.text)

    r.incr(f'count:{url}')

    return resp.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
