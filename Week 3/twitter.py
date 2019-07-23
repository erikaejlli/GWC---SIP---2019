# '''
# In this program, we print out all the text data from our twitter JSON file.
# Please explain the comments to students as you code.
# '''

# We start by importing the JSON library to use for this project.
# Twitter data is stored in this format - this is the same format
# students learned for their Survey Project!


import json
from textblob  import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud
# Next we want to open the JSON file. We tag this file as
# "r" read only because we are only going to look at the data.
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)


tweetlist = []
for i in range(len(tweetData)):
    tempTweet =  tweetData[i]["text"]
    tweetlist.append(tempTweet)
print(tweetlist)


def wordCount(stringOfTweet, string1):
    counter =  0
    string1 = string1.lower()
    wordList = stringOfTweet.split(' ')
    for item in wordList:
        if item == string1:
            counter += 1
    # print(counter)
    return counter


wordCountList = []
for item in tweetlist:
    wordoccurrence = wordCount(item, "the")
    wordCountList.append(wordoccurrence)

# print(wordCountList)
n, bins, patches = plt.hist(wordCountList, 50)
plt.axis([min(wordCountList), max(wordCountList), 0, 50])
plt.grid(True)
plt.show()




# We use the JSON library to get data from the file as JSON data.
# text = []
# polarity_list = []
#
# for i in range(0,len(tweetData)):
#     text.append(tweetData[i]["text"]
#     polarity_list.append(TextBlob(tweetData[i]["text"]).polarity)

# n, bins, patches = plt.hist(polarity_list, 50, normed = 1, facecolor = 'g', alpha = 0.75)
'''
plt.xlabel('tweets')
plt.ylabel('sentiment')
plt.title('Histogram of sentiment')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.show()

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)
print(type(x))
'''
# x = np.array(pola)
# # print(len(polarity_list),lent(text))
# giant_string_of_tweets = ""
# for i in range(0,len(tweetData)):
#     giant_string_of_tweets = tweetData[i]["text"]
# #
#
# plt.bar([1,3,5,7,9],[5,2,7,8,2], label="Example one")
# plt.bar([2,4,6,8,10],[8,6,2,5,6], label="Example two", color='g')
# plt legend()
#
# print(type(tweetData))
# print(type(tweetData[0]))
#
# print(type(tweetData[0].keys()))
#
# print(tweetData[0]["favorite_count"])
# #
# # We can close the file now that we have locally stored the data.
# print(list(tweetData[0].keys()))
#
# text = "hello it's me Erika"
# PolarityList =[]
# for i in range(0, len(tweet)):
#     blob1 = TextBlob(tweet[i])
#     polar1 = blob1.polarity
#     PolarityList.append(polar1)
# print(polarityList)

# print(polarityList)
# print(min(polarityList), max(polarityList))
# plt.hist(polarityList)
# plt.axis([-0.55, 1.05, 0, 50])
# plt.savefig("erikaschart")




####### connies histogam #######
# tweetString = ""
# for t in tweetlist:
#     print (t)
#     tweetString += t + " "
# print(tweetString)

# wordCount(tweetString, "a")
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# letters = sorted(alpha)
#
# occurrences = []
# for letter in letters:
#     occurrences.append(wordCount(tweetString,letter))

# for i in range(0,len(tweetData)):
#     tweetlist.append(tweetData[i]["text"])

# for i in range(len(tweetData)):
#     tempTweet =  tweetData[i]["text"]
#     tweetlist.append(tempTweet)
# print(tweetlist)

# tweetString = ""
# for t in tweetlist:
#     print (t)
#     tweetString += t + " "
# print(tweetString)
# wordCount(tweetString, "a")
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# letters = sorted(alpha)

# occurrences = []
# for letter in letters:
#     occurrences.append(wordCount(tweetString,letter))
#
# favoriteCount = 0
# numberOfFavoriteCounts = 0

# avg = favoriteCount / numberOfFavoriteCounts
# print(avg)
#
# print(len(tweetData))
#

    # print(f"letter:{letter} occurrences:{countLetter(tweetstring, letter)}")
# print(occurrences)
# print(min(occurrences), max(occurrences))
# plt.hist(occurrences)
# plt.axis([min(occurrences),max(occurrences), 0, 10])
# plt.show()

# wordcloud = WordCloud(height = 1000, width = 1000).generate(tweetstring)
# plt.figure(figsize = (10, 10), facecolor = None)
# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis("off")
# plt.show()
# plt.savefig("erikachart.png")

# tb = TextBlob("You are a brilliant computer scientist")
#
# print(tb.polarity)
#
# for tweet in tweetData:
#     if "text" in tweet:
#         text = tweet["text"]
#         for index in range(26):
#         print(index)
#         nums[index] += numOfLetter(text, alpha[index])
# #

# tweetData[0]["text"]
#
# print("Tweet id: ", tweetData[0]["id"])
#
#
# print("Tweet text: ", tweetData[0]["text"])
#
#
#
# for idx in range(len(tweetData)):
# 	print("Tweet text: " + tweetData[idx]["text"])
#
#
# for tweet in tweetData:
# 	print("Tweet text: " + tweet["text"])
#
