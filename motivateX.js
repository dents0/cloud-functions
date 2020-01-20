exports.motivateX = (req, res) => {
  let name = req.body.name || req.query.name || "employee";
  let lang = req.body.lang || req.query.lang;
  
  // Greek
  if (lang == "gr") {
    res.status(200).send(`επιστρέψη στη δουλειά σου, ${name}!`);
    // Romanian
  } else if (lang == "ro") {
    res.status(200).send(`Treci inapoi la munca, ${name}!`);
    // Spanish
  } else if (lang == "es") {
    res.status(200).send(`Vete a trabajar, ${name}!`);
    // Russian
  } else if (lang == "ru") {
    res.status(200).send(`Возвращайтесь к работе, ${name}!`);
    // English
  } else if (lang == "en") {
    res.status(200).send(`Get back to work, ${name}!`);
    // Language not specified
  } else {
	res.status(200).send(`Dub Qap Suq, ${name}!`);
  } 
  
};
