from google.cloud import storage

def copy_bucket_files(request):
    """
    Copies files from the bucket given in the request into the bucket specified below
    """
    
    # Check if the bucket's name was specified in the request
    if request.args.get('bucket'):
        bucketName = request.args.get('bucket')
    else:
        return "The bucket name was not provided. Please try again.\n"
    
    try:
        # Initiate Cloud Storage client
        storage_client = storage.Client()
        # Define the origin bucket
        origin = storage_client.bucket(bucketName)
        # Define the destination bucket
        destination = storage_client.bucket('<destination-bucket-name>')
        
        # Get the list of the blobs located inside the specified bucket
        blobs = storage_client.list_blobs(bucketName)
        
        for blob in blobs:
            origin.copy_blob(blob, destination)

        return "Done!\n"

    except:
        return "Failed!\n"
    
