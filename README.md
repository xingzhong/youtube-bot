Youtube-bot
===========

**Youtube-bot** is a Python program that can be used to upload videos to a YouTube channel. 

##Getting started

1. Download the code. Click on the **Download Zip** button on the right. Extract the .zip file.

2. **Configure your Google account**. Create a new project after logging into the [Google Developers Console](https://console.developers.google.com/). Configure the project by following [these instructions](https://developers.google.com/youtube/registering_an_application).

3. **Save authorisation file**. Choose the project created in the step above > select Credentials under APIs&auth > select **Download JSON**. Rename this file to `client_secrets.json` and save it alongside `uploadVideo.py` in the folder you extracted in step 1.

4. **Configuration is done!** Open a bash prompt and navigate to the path of the extracted folder. Run this command:

      ```./uploadVideo.py --file <pathToVideo> --title "Tom and Jerry" --description "Tom tries to kill Jerry! Again!"  --keywords "funny"```

##Bugs

Please report any bugs or enhancements to this project by [creating GitHub issues](https://github.com/chirayu11/youtube-bot/issues).
