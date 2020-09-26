exports.displayBucketImages = async(req, res) => {
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
  
  // Get a list of the files located inside the bucket to iterate through
  const [files] = await storage.bucket(bucketName).getFiles();
  // A sting that will store the <img> tags to display the images within the bucket
  let result = "";
  
  files.forEach(file => {
      // Check the file's extention
      file_extension = file.name.slice((file.name.lastIndexOf(".") - 1 >>> 0) + 2);
      // Check if the file is an image
      if ( ["png", "jpg", "jpeg"].includes(file_extension.toLowerCase()) ) {
        imgUrl = "https://storage.cloud.google.com/" + bucketName + "/" + file.name;
        result += `<strong>${file.name}</strong><br>` + `<img src='${imgUrl}'/><br><br>`;
      };
  });
  
  res.status(200).send(result);
};
