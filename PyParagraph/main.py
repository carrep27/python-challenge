#This code will break up a paragraph and retun approximate word count, sentence count, letter count and average sentence length

#Import regular expression
import re
#Assign the text file that needs to be evaluated as variable "textfile" and assigned variable. 
textfile = "paragraph_1.txt"
paragraph = " "
#open the text file and elimiate all carriage returns with empty spaces.  Utilize the split function to cut the paragraph up into individual words.
with open (textfile)as txt_data:
    paragraph = txt_data.read().replace("\n", " ")
    words = paragraph.split(" ") # We are splitting the paragraph into words. creating a "bucket" of all words in the paragraph
    word_count = len(words) 
    letters=[] #creating empty list "letters" which we will letters to
    for word in words: #loop through all the words in our bucket of words, obtain # of letters in each word and pass to "letters"
        letters.append(len(word))
    ttlletters = sum(letters)#sum all the letters, this will be our numerator
    lettercount = float(len(letters))#get the letter count. casting this as float so that our average is not int
    avgletters = ttlletters/lettercount
    splitsentence = re.split("(?<=[.!?]) +", paragraph)#now we will split the original paragraph into sentences. We will split based on punctuation. 
    countsentence = len(splitsentence)#obtaining sentence count
    ttlwords =[]#empty wordlist that we will append to
    for sentence in splitsentence: #loop through each sentence and return number of words per sentence to ttlwords list
        ttlwords.append(len(sentence.split(" ")))
    totalwords = sum(ttlwords)#same concept we used to get average letters per word is used for average words per sentence
    wordcount = float(len(ttlwords))
    avgsentence = totalwords/wordcount
#print out summary
    summary = (
        f"\nParagraph 1\n"
        f".................................\n"
        f"Approximate Word Count: {totalwords}\n"
        f"Approximate Sentence Count: {countsentence}\n"
        f"Average Letter Count: {avgletters}\n"
        f"Average Sentence Length: {avgsentence} \n")
print (summary)
#Repeat for second file
#Assign the text file that needs to be evaluated as variable "textfile" and assigned variable. 
textfile = "paragraph_2.txt"
paragraph = " "
#open the text file and elimiate all carriage returns with empty spaces.  Utilize the split function to cut the paragraph up into individual words.
with open (textfile)as txt_data:
    paragraph = txt_data.read().replace("\n", " ")
    words = paragraph.split(" ") # We are splitting the paragraph into words. creating a "bucket" of all words in the paragraph
    word_count = len(words) 
    letters=[] #creating empty list "letters" which we will letters to
    for word in words: #loop through all the words in our bucket of words, obtain # of letters in each word and pass to "letters"
        letters.append(len(word))
    ttlletters = sum(letters)#sum all the letters, this will be our numerator
    lettercount = float(len(letters))#get the letter count. casting this as float so that our average is not int
    avgletters = ttlletters/lettercount
    splitsentence = re.split("(?<=[.!?]) +", paragraph)#now we will split the original paragraph into sentences. We will split based on punctuation. 
    countsentence = len(splitsentence)#obtaining sentence count
    ttlwords =[]#empty wordlist that we will append to
    for sentence in splitsentence: #loop through each sentence and return number of words per sentence to ttlwords list
        ttlwords.append(len(sentence.split(" ")))
    totalwords = sum(ttlwords)#same concept we used to get average letters per word is used for average words per sentence
    wordcount = float(len(ttlwords))
    avgsentence = totalwords/wordcount
#print out summary
    summary = (
        f"\nParagraph 2\n"
        f".................................\n"
        f"Approximate Word Count: {totalwords}\n"
        f"Approximate Sentence Count: {countsentence}\n"
        f"Average Letter Count: {avgletters}\n"
        f"Average Sentence Length: {avgsentence} \n")
print (summary)