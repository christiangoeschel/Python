from urllib.request import urlopen

url = 'http://sixty-north.com/c/t.txt'



# This function will get the story from the specified URL
# and create a list with all the words as a single object in it
def get_story(story_url):

    global story_words
    story_words = []

    story = urlopen(url)
    
    for line in story:
        line_words = line.split()
        for words in line_words:
            story_words.append(words.decode('UTF-8'))

    story.close()



# This function takes the user defined words per list number and prints the lines with the respective word count
def print_story(word_rate):

    word_counter = 1    # Counts how many words are in a line

    for i in story_words:

        if word_counter % word_rate == 0:
            print(i + "\n")
            word_counter += 1
            
        else:
            print(i,end=" ")
            word_counter += 1

# This function will ask the user to enter a numeric value for the amount of words he wants in a line
def get_wordcount():

    global words_per_line
    words_per_line = input("How many words do you want to be in a single line ?\nEnter number: ")

    try: 
        words_per_line = int(words_per_line)

    except (TypeError, ValueError):
            print("Value Error! NaN - Please type in numeric values only.") 
            exit


get_story(url)
get_wordcount()
print_story(words_per_line)

    
