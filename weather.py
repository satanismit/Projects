# https://www.google.com/search?q=weather+amreli
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36

# span id: wob_tm
# vk_bk wob-unit
from requests_html import HTMLSession
import speech_to_text

def weather():
        
    s=HTMLSession() # create a session
    query="amreli"
    url=f'https://www.google.com/search?q=weather+{query}'
    # get the page
    r=s.get(url, headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"})

    temp=r.html.find("span#wob_tm", first=True).text
    print(temp)
    unit=r.html.find("div.vk_bk.wob-unit span.wob_t", first=True).text
    print(unit)
    desc = r.html.find("span#wob_dc", first=True).text
    print(desc)
    return f"Temperature is {temp} {unit} and {desc}"


