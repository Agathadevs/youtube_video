from selectolax.lexbor import LexborSelector
import httpx
from typing import Optional,List
from urllib.parse import (
    quote_plus,
    quote,
    unquote_plus,
    unquote
) 

headers={
    "User-Agent":(
        "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)"
        " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0"
        " Mobile Safari/537.36 Edg/120.0.0.0"
    )
}
class Search:
    def __init__(self,query:str) -> None:

        client=httpx.Client()

        res=client.get(
            "https://www.youtube.com/results?app=desktop&search_query={}".format(
                quote_plus(query)
        ))

        print(res)
    