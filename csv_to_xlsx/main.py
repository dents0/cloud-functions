from google.cloud import storage
import pandas as pd


def to_xlsx(event, context):
    """
    This function is triggered by uploading / updating a '.csv' file
    in a GCS bucket.

    An '.xlsx' file with the same name will appear in the specified bucket.
    """

    # When triggered by '.xlsx' file creation.
    if event['name'][-5:] == ".xlsx":
        return
    # Check if the uploaded file has '.csv' format.
    elif event['name'][-4:] != ".csv":
        print("Wrong file provided: {}. Provided file must have '.csv' extension".format(event['name']))
        return
    # CSV file has been uploaded.
    else:
        # Instantiate a storage client
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(event['bucket'])

        with open('/tmp/{}.xlsx'.format(event['name'][:-4]), 'w'):
            read_file = pd.read_csv("gs://{}/{}".format(event['bucket'], event['name']))
            read_file.to_excel('/tmp/{}.xlsx'.format(event['name'][:-4]), index = None, header=True)
            result = bucket.blob('{}.xlsx'.format(event['name'][:-4]))
            result.upload_from_filename('/tmp/{}.xlsx'.format(event['name'][:-4]))

        print("File {}.xlsx created.".format(event['name'][:-4]))
        return
