#!/usr/bin/env python
# coding: utf-8

# In[2]:


with open("brown.txt","r") as f:                                    # Opening corpus to split into training set and test set
    testfile = open("brown-test.txt","w+")
    trainfile = open("brown-train.txt","w+")
    words = f.read()
    count = 0
    for word in words.split():
        if (word == "\n" or word =="``/``" or word == "''/''"):
            {}
        else:
            if(count<2000):
                if (word == "./."):
                    count = count + 1
                testfile.write(word)
                testfile.write(" ")
            else:
                trainfile.write(word)
                trainfile.write(" ")


# In[3]:


with open("brown-train.txt","r") as train:                    # Splitting the words and tags from the training set into seperate lists
    temp = train.read()
    words = temp.split()
    tags = []
    for i in words:
        tags.append(i.split("/")[1])


# In[4]:


f=lambda n:sorted(set(n),key=n.count)[::-1]             # Finding the most frequent word-tag combination
result = f(words)                                       # Storing the sorted list in decending order by frequency


# In[6]:


train_list_with_tags = []                               
word_list = []
tag_list = []
count = 0

for i in result:
    train_list_with_tags.append(i.split("/"))                           # Creating a list of lists that contains the [word-tag] from the training set split as an element
    word_list.append(train_list_with_tags[count][0])                    # Creating a list just for the words
    tag_list.append(train_list_with_tags[count][1])                     # Creatng a list just for the tags
    count = count + 1


# In[7]:


temp1 = []                                                 # Training a unitagger that contains the most frequent tag of a word
unitagger = []
count = 0
for l in word_list:
    if(l not in temp1):
        temp1.append(l)
        unitagger.append(train_list_with_tags[count])
    count = count + 1


# In[55]:


with open ("unitagger.txt","w+") as uni:                  # Writing the unitagger results to a file
    for q in unitagger:
        uni.write(str(q))
        uni.write('\n')


# In[8]:


with open ("brown-test.txt","r") as test:                # Time for testing our unitagger on the test set
    temp2 = test.read()
    test = temp2.split()


# In[9]:


test_list_with_tags = []                                 # Creating a list for the test word-tag and a list for the test words alone
test_words = []   
count = 0

for i in test:
    test_list_with_tags.append(i.split("/"))
    test_words.append(test_list_with_tags[count][0])
    count = count + 1


# In[10]:


test_tag = []                                          # Tagging words in the test set that our unitagger hasn't seen as 'UNK' 
for t in test_words:
    if(t not in word_list):
        temp3 = [t,'UNK']
        test_tag.append(temp3)
    else:
        temp3 = [t,tag_list[word_list.index(t)]]
        test_tag.append(temp3)


# In[24]:


count = 0                                             # Counting how many times the tagger predicted the correct tag
for i in test_tag:
    if i in test_list_with_tags:
        count = count + 1


# In[25]:


unitagger_accuracy = count / len(test_tag) * 100     # Accuracy formula


# In[26]:


unitagger_accuracy                                   # Pretty accurate for a unigram tagger which ignores the unknown words


# In[15]:


original_tags = []                                  # Creating a seperate list for the predicted and true values of the tags
predicted_tags = []
for i in test_list_with_tags:
    original_tags.append(i[1])
for i in test_tag:
    predicted_tags.append(i[1])


# In[16]:


temp_confusion_matrix = []                          # Implementing the confusion matrix
temp5 = []
confusion_matrix_uni = []
count = 0
for i in original_tags:
    temp = [i,predicted_tags[count]]
    temp_confusion_matrix.append(temp)
    count = count + 1
temp_confusion_matrix1 = str(temp_confusion_matrix)


# In[17]:


for i in temp_confusion_matrix:
    if i not in temp5:
            temp5.append(i)


# In[18]:


for i in temp5:
    temp = [i[0],i[1], temp_confusion_matrix1.count(str(i))]
    confusion_matrix_uni.append(temp)


# In[19]:


g = lambda n:sorted(set(n),key=n.count)[::-1]                # Finding the most occuring tag in the training data
result_tags = f(tags)


# In[20]:


result_tags[0]


# In[21]:


count = 0                                                  # Creating another two lists with contain the unknown words alone.
total_count_of_unk = 0                                     # One list contains all the unknown words tagged as the most frequent tag in the training set
new_tags = []                                              # The other list contains the actual tag of the unknown word
actual_unk_tags = []
for i in test_tag:
    if(i[1]=='UNK'):
        total_count_of_unk = total_count_of_unk + 1
        temp = [i[0],result_tags[0]]
        temp1 = [i[0], test_list_with_tags[count][1]]
        new_tags.append(temp)
        actual_unk_tags.append(temp1)
    count = count + 1


# In[22]:


count = 0                                                 # Finding the accurary of our strategy of tagging unknown words
for i in new_tags:
    if i in actual_unk_tags:
        count = count + 1
accuracy_of_unk_words_uni = count / total_count_of_unk * 100


# In[23]:


accuracy_of_unk_words_uni


# BIGRAM : 
# 
# 

# In[95]:


count = 0
bi_tag_list = []
for tag in tags:
    if count != len(tags)-1:
        bi = [tags[count],tags[count+1]]
        bi_tag_list.append(bi)
        count = count+1


# In[105]:


unique_words =[]
for i in words:
    if i not in unique_words:
        unique_words.append(i)


# In[120]:


unique_words_split = []
for i in unique_words:
    unique_words_split.append(i.split("/"))


# In[127]:


temp5 = []
for i in unique_words_split:
    if(i[0] not in temp5):
        temp5.append(i[0])    


# In[130]:


temp6 = []
for i in temp5:
    if i == unique_words_split[]

