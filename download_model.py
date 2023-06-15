def deneme():
    print("a")

def download():
    import requests


    url = "https://www.kaggleusercontent.com/kf/125026100/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..Ks8dL7xf0ZF0wcA8mopzdA.V9juVYZRxBhM2hQAgeYhjPVp3JCSaoQ_KtPrfF6nTzHQ_hSR4xKyD3a5Y-OC9YDq-MkpllBKNFTWEWjO9VbyaZ7D0hbbd5DBv3CIFw33yLLGMSBiSWs4mpMmh6mbN9FoPWDy_Zxmk5G0bw6socQuvgueJYcGvtyL7-boobQOC9qNHlYy7F8P1_EjTVqYI3mrEWaFp3g08xvKsuYXec11FkGeCjmBsjxf5P33FAz6ljYPjON7qxSTDMROjslLWdaSHSgroO0A1q9ftz8wLnl7I4u_7d-Tl_iqOnkUsOJwJEXc_StoH5oQOuC29dzSG0GXUFwiUCvJYzDEuLMrxc0RaqYZVbzbqNuC-83i46vFBe63VozxZzS25YMVPYgiZYveEd2mKRKF9xSAoc8pg2R0IS_IovId_uEj4qnxg__1Ns2ui6fTqVmcoAgHUJqVb2Od9_ktnIzZ3Ncsa4bRKgs0wpSS7jTzCedIZY87U-NFewLFevw0lIeKn3zUwxAP-_xjGkQew7ahZgzIZ5DU3OBAyhQqpPyDPBgkoCdLVuL89A8W8pK5X1RtQgoQJN9keOALBJwB7OCzFDwztluHBU41RQsQbi-rAr5NMpwLgM2R_UTrCEMSoF0hk6bpCSat1nzfi4VWOi6M0QBQAFhiw-jEvcFaNz17gFXPCeI7I7ULPStcpLGbIyAoPVgxnB5pqJed.f5KDBRGDg_J8TAzRG9pv1A/saved_model/variables/variables.data-00000-of-00001"

    payload = {}
    headers = {
    'authority': 'www.kaggleusercontent.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://www.kaggle.com/',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Brave";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    a = response.content

    with open("model/saved_model/variables/variables.data-00000-of-00001", "wb") as file1:
        file1.write(a)