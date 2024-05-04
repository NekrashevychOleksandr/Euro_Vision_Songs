import requests
from bs4 import BeautifulSoup

def extract_youtube_urls(url):
    # Define headers with a user-agent
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    # Send a GET request to the webpage with headers
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all div elements with class "video"
        video_divs = soup.find_all('div', class_='video')
        
        # Extract YouTube video URLs from data attributes
        youtube_urls = []
        for div in video_divs:
            youtube_id = div.get('data-video-youtube')
            if youtube_id:
                youtube_url = f'https://www.youtube.com/watch?v={youtube_id}'
                youtube_urls.append(youtube_url)
        
        return youtube_urls
    else:
        print(f"Failed to fetch the webpage. Status code: {response.status_code}")
        return []

# URL of the webpage containing embedded YouTube videos
print("2024 ----------------------------------------------------------")
webpage_url = 'https://eurovisionworld.com/eurovision/songs-videos'
print(extract_youtube_urls(webpage_url))
print("2023 ----------------------------------------------------------")
webpage_url = 'https://eurovisionworld.com/eurovision/2023/songs-videos'
print(extract_youtube_urls(webpage_url))
print("2022 ----------------------------------------------------------")
webpage_url = 'https://eurovisionworld.com/eurovision/2022/songs-videos'
print(extract_youtube_urls(webpage_url))
print("2021 ----------------------------------------------------------")
webpage_url = 'https://eurovisionworld.com/eurovision/2021/songs-videos'
print(extract_youtube_urls(webpage_url))
print("2020 ----------------------------------------------------------")
webpage_url = 'https://eurovisionworld.com/eurovision/2020/songs-videos'
print(extract_youtube_urls(webpage_url))
print("2019 ----------------------------------------------------------")
webpage_url = 'https://eurovisionworld.com/eurovision/2019/songs-videos'
print(extract_youtube_urls(webpage_url))
print("2018 ----------------------------------------------------------")
webpage_url = 'https://eurovisionworld.com/eurovision/2018/songs-videos'
print(extract_youtube_urls(webpage_url))
print("2017 ----------------------------------------------------------")
webpage_url = 'https://eurovisionworld.com/eurovision/2017/songs-videos'
print(extract_youtube_urls(webpage_url))
print("2016 ----------------------------------------------------------")
webpage_url = 'https://eurovisionworld.com/eurovision/2016/songs-videos'
print(extract_youtube_urls(webpage_url))
print("2015 ----------------------------------------------------------")
webpage_url = 'https://eurovisionworld.com/eurovision/2015/songs-videos'
print(extract_youtube_urls(webpage_url))
print("2014 ----------------------------------------------------------")
webpage_url = 'https://eurovisionworld.com/eurovision/2014/songs-videos'
print(extract_youtube_urls(webpage_url))
print("2013 ----------------------------------------------------------")
webpage_url = 'https://eurovisionworld.com/eurovision/2013/songs-videos'
print(extract_youtube_urls(webpage_url))

