exports.displayBucketObjectsURLs = async(req, res) => {
  let bucketName = req.body.bucket || req.query.bucket || null;
  
  // Check if the bucket's name was specified in the request
  if (bucketName === null) {
    res.status(200).send("No bucket name was provided when calling the function. Please try again.<br>");
    return;
  };
  
  // Import the Google Cloud Storage library
  const {Storage} = require('@google-cloud/storage');
  // Initiate a Storage client
  const storage = new Storage();
  
  // List objects located inside the bucket to iterate through
  const [files] = await storage.bucket(bucketName).getFiles();
  // A string that will store the objects' URLs to display
  let result = "";
  files.forEach(file => {
    result = result + "https://storage.cloud.google.com/" + bucketName + "/" + file.name + "<br>";
  });
  
  res.status(200).send(result);
};
