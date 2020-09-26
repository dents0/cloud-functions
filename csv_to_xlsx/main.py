from google.cloud import storage
import pandas as pd


def to_xlsx(event, context):
    """
    This function is triggered by uploading / updating a '.csv' file
    in a GCS bucket.

    An '.xlsx' file with the same name will appear in the specified bucket.
    """

    # Check if the uploaded file has '.txt' format
    if event['name'][-4:] != ".csv":
        print("Wrong file provided: provided file must have '.csv' extension")
        return ""


    # Instantiate a storage client
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(event['bucket'])
    blob = bucket.get_blob(event['name'])


    with open('/tmp/result.xlsx', 'w') as out:
        read_file = pd.read_csv(event['name'])
        out.write(read_file.to_excel('/tmp/result.xlsx', index = None, header=True))
        result = 'result.xlsx'
        result.upload_from_filename('/tmp/result.xlsx')
