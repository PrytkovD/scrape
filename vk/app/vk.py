import os
import pika
import requests

from common.api.models import *

api_access_token = os.getenv('VK_API_ACCESS_TOKEN')
api_version = os.getenv('VK_API_VERSION')

wall_get_api_method = 'https://api.vk.com/method/wall.get'
wall_get_comments_api_method = 'https://api.vk.com/method/wall.getComments'


def request_wall_get(domain: str, count: int):
    params = {
        'access_token': api_access_token,
        'v': api_version,
        'domain': domain,
        'count': count
    }

    return requests.get(wall_get_api_method, params).json()


def request_wall_get_comments(owner_id: str, post_id: str, count: int = 100):
    params = {
        'access_token': api_access_token,
        'v': api_version,
        'owner_id': owner_id,
        'post_id': post_id,
        'count': count,
        'sort': 'asc',
        'preview_length': 0
    }

    return requests.get(wall_get_comments_api_method, params).json()


def get(source: str, limit: int = 100) -> CrawlerResponse:
    wall_get_result = request_wall_get(source, limit)

    posts: List[Post] = list()

    for item in wall_get_result['response']['items']:
        wall_get_comments_result = request_wall_get_comments(item['owner_id'], item['id'])

        comments: List[Comment] = list()

        for comment_item in wall_get_comments_result['response']['items']:
            comments.append(Comment(
                text=item['text']
            ))

        posts.append(Post(
            id=item['id'],
            owner_id=item['owner_id'],
            text=item['text'],
            date=item['date'],
            view_count=item['views']['count'],
            comment_count=item['comments']['count'],
            reaction_count=list([int(item['likes']['count'])]),  # todo: maybe add other six reactions as zeros
            comments=comments
        ))

    return CrawlerResponse(posts=posts)


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()

    channel.queue_declare(queue='vk', durable=True)

    def on_request(ch, method, properties, body):
        source = body['source']

        response = get(source)

        channel.basic_publish(
            exchange='Planner',
            routing_key='vk',
            properties=pika.BasicProperties(
                correlation_id=properties.correlation_id
            ),
            body=response.json().encode('utf-8')
        )

    channel.basic_consume(queue='youtube', on_message_callback=on_request)

    channel.start_consuming()


print(get('toportg'))

if __name__ == '__main__':
    main()
