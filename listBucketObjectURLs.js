exports.listBucketObjectURLs = async(req, res) => {
  let bucketName = req.body.bucket || req.query.bucket || null;
  
  // Check if the bucket's name was specified in the request
  if (bucketName === null) {
    res.status(200).send("No bucket name was provided when calling the function. Please try again.");
    return;
  };
  
  // Import the Google Cloud Storage library
  const {Storage} = require('@google-cloud/storage');
  // Initiate a Storage client
  const storage = new Storage();
  
  // Lists files in the bucket to iterate through
  const [files] = await storage.bucket(bucketName).getFiles();
  // An array to store files' URLs
  let result = [];
  files.forEach(file => {
    result.push("https://storage.cloud.google.com/" + bucketName + "/" + file.name);
  });
  
  res.status(200).send(result);
};
