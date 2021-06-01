Description
---
A Cloud Functions triggered by Pub/Sub. The function updates the value of the `counter` stored in Firebase RTDB.

When a message is publised to the Pub/Sub topic the function is listening to, it attempts to perform a transaction to 
update the `counter`'s value by 1. The transaction ensures that the race condition won't be an issue if several 
subscribers push messages to the topic at the same time.

I have enabled **retries** for this function, so that if a transaction fails the function gets run again until the `counter` 
is updated accordingly, so that it is incremented by 1 for every message published to the topic.
