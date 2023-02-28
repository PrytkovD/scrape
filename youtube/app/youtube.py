import os
import pika
import requests

from common.api.models import *

api_key = os.getenv('YOUTUBE_API_KEY')

search_api_method = 'https://youtube.googleapis.com/youtube/v3/search'
videos_api_method = 'https://youtube.googleapis.com/youtube/v3/videos'
comment_threads_api_method = 'https://youtube.googleapis.com/youtube/v3/commentThreads'


def request_search(channel_id: str, max_results: int, next_page_token: str = ''):
    params = {
        'key': api_key,
        'channelId': channel_id,
        'part': 'id',
        'order': 'date',
        'maxResults': max_results
    }

    if len(next_page_token) != 0:
        params['pageToken'] = next_page_token

    return requests.get(search_api_method, params).json()


def request_videos(ids: List[str]):
    params = {
        'key': api_key,
        'part': 'id,snippet,statistics',
        'id': ','.join(ids)
    }

    return requests.get(videos_api_method, params).json()


def request_comments(video_id: str):
    params = {
        'key': api_key,
        'part': 'id,snippet',
        'videoId': video_id,
        'order': 'relevance'
    }

    return requests.get(comment_threads_api_method, params).json()


def get(source: str, limit: int = 50) -> CrawlerResponse:
    max_results_per_batch = 5

    ids = []

    for i in range(0, limit, max_results_per_batch):
        search_result = request_search(source, max_results_per_batch)
        for item in search_result['items']:
            ids.append(item['id']['videoId'])

    videos_result = request_videos(ids)

    posts: List[Post] = list()

    for item in videos_result['items']:
        video_id = item['id']

        comments_result = request_comments(video_id)

        comments: List[Comment] = list()

        for comment_item in comments_result['items']:
            comments.append(Comment(
                text=comment_item['snippet']['topLevelComment']['snippet']['textOriginal']
            ))

        posts.append(Post(
            id=video_id,
            owner_id=item['snippet']['channelId'],
            text=item['snippet']['description'],
            date=item['snippet']['publishedAt'],
            view_count=item['statistics']['viewCount'],
            comment_count=item['statistics']['commentCount'],
            reaction_count=list([int(item['statistics']['likeCount']), 0]),
            comments=comments
        ))

    return CrawlerResponse(posts=posts)


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()

    channel.queue_declare(queue='youtube', durable=True)

    def on_request(ch, method, properties, body):
        source = body['source']

        response = get(source)

        channel.basic_publish(
            exchange='Planner',
            routing_key='youtube',
            properties=pika.BasicProperties(
                correlation_id=properties.correlation_id
            ),
            body=response.json().encode('utf-8')
        )

    channel.basic_consume(queue='youtube', on_message_callback=on_request)

    channel.start_consuming()


if __name__ == '__main__':
    main()
