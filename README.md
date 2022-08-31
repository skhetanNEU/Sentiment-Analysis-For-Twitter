# Sentiment Analysis For Twitter
An end to end system for gathering tweets on a particular topic and running Sentiment analysis on it. The results can then be viewed using dashboards created on Qlikview.

## Prerequisites : 
1. Tweepy
2. Pandas
3. Numpy
4. sklearn
5. nltk

## How to run : 

When we want to stream data from twitter on any particular topic these are the steps that should be executed:
1. src folder contains the code files.
2. Make an account on twitter and generate keys and access tokens for your account
3. Open streaming.py
4. Change the consumer_key,consumer_secret,access_key,access_token with the keys and tokens from your account
5. Change the accountvar's value to the hashtag of the topic that you want to search for
6. Open the terminal and run streaming.py
7. It will start streaming tweets which contains the hashtag specified in the accountvar and store the data in an excel file
8. To stop the streaming press Ctrl+Z

The same steps can be repeated for ecommerce_streaming.py and mobiles.py , but we should specify the handle names such as
@flipkartSupport, @SamsungSupport in the accountvar variable instead of the hashtags.

Once the data has been streamed and we have the excel file ready then to count the most frequent hashtags we can run
count_words_calc.py that will create another excel file with top 10 most frequently used hashtags in the tweets related to
the original topic.

To Observe the analysis open the Qlikview file named Twitter_Analysis.
It is mandatory to have a licensed version of qlikview to open this file.

Once it is opened you will have to change the file name to the new excel sheet that has been created for some topic
To do that follow these steps:

1. Press Ctrl+E to edit the script.
2. Change The location of the file written in FROM to the location of the new file.
3. Similarily if required, do it for ecommerce_streaming as well as mobiles
4. Once the location is changes press Ctrl+R to reload the new data.

Once the new data has been reloaded you can observe and analyze the data from twitter.v
