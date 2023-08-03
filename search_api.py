"""Queries RTD search API and parses the result to be used by the bot."""

import requests
from config import URL, PROJECT

def query(search_query:str, page:int=-1, page_size:int=-1) -> requests.Response:
    """
    Queries the ReadTheDocs search V3 API with given search query.
     
    Searches for given PROJECT, see
    https://docs.readthedocs.io/en/stable/server-side-search/api.html 
    for more info. Returns the JSON response.
    """
    params = {
        'q' : f"project:{PROJECT} {search_query}",
    }
    if page != -1:
        params['page'] = page
    if page_size != -1:
        params['page_size'] = page_size
    return requests.get(URL, params=params)

def parse_query(query_response:requests.Response) -> list:
    """Returns a list of parsed result dicts."""
    query_response.raise_for_status()
    return [parse_result(result) for result in query_response.json()['results']]

def parse_result(result:dict) -> dict:
    """Returns a parsed and simplified dict with keys `url` and `title`."""
    return {
        'url' : result['domain']+result['path'],
        'title' : result['title']
    }