# import requests
import json
import urllib.request
import re


def find_info_from_video(video_id):
    api_key = "AIzaSyDsF7PCu8x9RuCeBaKzFOqq2NxGvlTLmHs"
    base_info_url = 'https://www.googleapis.com/youtube/v3/videos?'

    # для получения описания видео
    first_url = base_info_url + 'part=snippet&id&key={}&id={}'.format(api_key, video_id)
    inp = urllib.request.urlopen(first_url)
    resp = json.load(inp)

    match = re.findall("(https?://[^\s]+)", resp['items'][0]['snippet']['description'])

    # для получения кол-ва лайков, просмотров, комментов
    second_url = base_info_url + 'part=statistics&id&key={}&id={}'.format(api_key, video_id)
    inp = urllib.request.urlopen(second_url)
    resp = json.load(inp)

    statistics = resp['items'][0]['statistics']

    data = []
    data.append({'videoId': resp['items'][0]['id'],
                 'likes': statistics['likeCount'],
                 'viewCount': statistics['viewCount'],
                 'commentCount': statistics['commentCount'],
                 'links': match})
    return data


def get_all_videos(channel_id):
    api_key = "AIzaSyDsF7PCu8x9RuCeBaKzFOqq2NxGvlTLmHs"

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=1'.format(api_key,
                                                                                                       channel_id)

    video_links = []
    url = first_url

    # j - кол-во видео
    j = 0
    while j < 100:
        j += 1
        inp = urllib.request.urlopen(url)
        resp = json.load(inp)

        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append([base_video_url + i['id']['videoId'],
                                    i['id']['videoId']])
        try:
            next_page_token = resp['nextPageToken']
            url = first_url + '&pageToken={}'.format(next_page_token)
        except:
            break
    return video_links


youtube_channel_id = "UCRxBK1uUONfrU7roM36zuTQ"
all_video_links = get_all_videos(youtube_channel_id)

file = {}
file['video'] = []

for link in all_video_links:
    data = find_info_from_video(link[1])
    file['video'].append(data)

with open('data.txt', 'w') as outfile:
    json.dump(file, outfile)

print("Total: ", len(all_video_links))
