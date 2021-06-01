def create_csql_backup(request):
  from googleapiclient import discovery
  from oauth2client.client import GoogleCredentials

  credentials = GoogleCredentials.get_application_default()

  service = discovery.build('sqladmin', 'v1beta4', credentials=credentials)

  # Project ID of the project that contains the instance.
  project = 'PROJECT_ID'

  # Cloud SQL instance ID. This does not include the project ID.
  instance = 'CLOUD_SQL_INSTANCE'

  request = service.backupRuns().insert(project=project, instance=instance)
  request.execute()

  return '!'
