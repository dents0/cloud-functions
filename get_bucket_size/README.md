Description
---
Returns the size of the bucket specified in the request, in *bytes*.

An equivalent of the `gsutil du -s gs://[BUCKET_NAME]/` command.

How to call
---
Use the **trigger URL** passing the name of the bucket: `<trigger-URL>/?bucket=<name-of-the-bucket>`. 

E.g. `https://<function-region>-<project-name>.cloudfunctions.net/<function-name>/?bucket=<name-of-the-bucket>`
