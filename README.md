GCP Cloud Functions collection
===


**Author:** Deniss Tsokarev

**License:** *see [LICENSE.txt](https://github.com/dents0/cloud-functions/blob/master/LICENSE.txt)*


Description
---
 - [**copy_bucket_files**](https://github.com/dents0/cloud-functions/tree/master/copy_bucket_files) - 
 copies files from the bucket given in the request into the bucked defined in the function.
 
  - [**create_csql_backup**](https://github.com/dents0/cloud-functions/tree/master/create_csql_backup) - 
 Initiates the on-demand backup for a Cloud SQL instance.
 
 - [**csv_to_xlsx**](https://github.com/dents0/cloud-functions/tree/master/csv_to_xlsx) - function that converts *.csv* files to *.xlsx*; triggered by GCS *Finalize/Create* event.

 - [**displayBucketImages**](https://github.com/dents0/cloud-functions/tree/master/displayBucketImages) - 
 displays the images located in the bucket specified in the request.

 - [**displayBucketObjectsURLs**](https://github.com/dents0/cloud-functions/tree/master/displayBucketObjectsURLs) - 
 displays the URLs of the objects stored in the bucket specified in the request.

 - [**firebase_rtdb_transaction**](https://github.com/dents0/cloud-functions/tree/master/firebase_rtdb_transaction) - 
 updates the value of the counter stored in Firebase RTDB via transaction, which prevents possible race condition issues.

 - [**get_bucket_size**](https://github.com/dents0/cloud-functions/tree/master/get_bucket_size) - 
 returns the size of the bucket specified in the request, in *bytes*.

 - [**get_pip_version**](https://github.com/dents0/cloud-functions/tree/master/get_pip_version) - 
 returns the version of PIP used in the Cloud Functions environment.

 - [**listBucketObjectURLs**](https://github.com/dents0/cloud-functions/tree/master/listBucketObjectURLs) - 
 returns an array with the URLs of the objects stored in the bucket specified in the request.

 - [**motivateX**](https://github.com/dents0/cloud-functions/tree/master/motivateX) - 
 "professional motivation".

 - [**telegram_bot_message**](https://github.com/dents0/cloud-functions/tree/master/telegram_bot_message) - 
 Sends a message to the specified Telegram chat on behalf of the bot, if the user has initiated the bot.
 
  - [**text_to_speech**](https://github.com/dents0/cloud-functions/tree/master/text_to_speech) - 
 Generates an mp3 file for the uploaded/updated text file in the specified GCS bucket.
 