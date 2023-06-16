def download():
    import requests

    url = "https://www.kaggleusercontent.com/kf/125026100/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..mUENGMsYojVEXqAxQRZ9RQ.ToilM-lIk2wZNY40UeKB96hsrQZYjFSuhX7bOFgNr2GtWZL9ftbxpxVK-_rB4t_P6CXiylExaPcqQXd0N6hbc_uZMHdFHfxvjEzS5g8SFRfcp2YXgyob6Q-dMyB1MhH4KqeSmLfeFbbML3WFbXlCeYyf9VUhvJV7bMm7GPrfUZZiZSWxnh15dM5UOjGLzTfW1elxEXeb2zuB5zcEZ5wbq7LHrdmDVVbtle41Pg_PkYGYY3x6-OAKwtWb_MKM-LXi9bgpzrG-DZvwbmqHq_LNVDPj8S_j4ELmr-B3sX7Z6J4krOL0xzOuHS7S4QcSeSU5dYviKSSfhH-cmuopri8YWkaEOZ6Yky4qHBHUuHEhiT2cizxlwGhST4UhFxcJJBDd2NulQcMiF9xCiw_CziFAAy-dF5TSm3skiXX-dvSHwh3z_7DMFVAuq3yBF_MMaD3VYT1dV3IASnYGCCKaiQZYxdu7I79e2jgXsPx0bqQnIYVXoib_oJg1eDmz9RvL7Dx6v9Zx6ms35nUiZzdWYzhU3THFRrr8kdmHidinMxx41vOV8tiTBOBCaniwGX6ufMSoRT4ZdVp9RKX22swUQ7v6awE89X8Cqzjbxg-DABZvO9mlkdJxOO2ZoTcvoKmvjAfpalX_bwdRMebQqLVJwUka4DKcXL6jjG7BKRkRa_v0rBGcXawpcUeah2v8C0KM9pK1.f14eGmEMG3BDA6pz9a58iQ/saved_model/variables/variables.data-00000-of-00001"

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

    with open("models/saved_model/variables/variables.data-00000-of-00001", "wb") as file1:
        file1.write(a)

if __name__ == "__main__":
    download()
