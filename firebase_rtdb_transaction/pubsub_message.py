""" A code snippet for publishing messages to the Pub/Sub topic. """

from google.cloud import pubsub_v1


project_id = 'PROJECT_ID'
topic_id = 'PUB_SUB_TOPIC_ID'  # Taken from 'projects/PROJECT_ID/topics/TOPIC_ID'


publisher = pubsub_v1.PublisherClient.from_service_account_json('key.json')
topic_path = publisher.topic_path(project_id, topic_id)

for n in range(1000):
    data = 'Message number {}'.format(n)
    # Data must be a bytestring
    data = data.encode('utf-8')
    future = publisher.publish(topic_path, data)
    print(future.result())

print(f'Published messages with custom attributes to {topic_path}.')
