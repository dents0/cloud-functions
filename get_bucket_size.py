from google.cloud import storage

def get_bucket_size(request):
    """
    An equivalent of the `gsutil du -s gs://[BUCKET_NAME]/` command.
    The function accepts the name of the bucket that can be passed in the request
    and returns the size of the bucket in bytes.
    
    Note: using the command mentioned above would be a more efficient way to achieve this.
    """
    
    # Check if the bucket's name was specified in the request
    if request.args.get('bucket'):
        bucketName = request.args.get('bucket')
    else:
        return "The bucket name was not provided. Please try again.\n"
    
    try:
        # Initiate Cloud Storage client
        storage_client = storage.Client()
        # Get the list of the blobs located inside the bucket
        blobs = storage_client.list_blobs(bucketName)

        # A variable that will store the size of all files
        result = 0
        for blob in blobs:
            result += blob.size

        return "Bucket '{}' is {} bytes.\n".format(bucketName, result)

    except:
        return "Check the bucket name and try again.\n"

